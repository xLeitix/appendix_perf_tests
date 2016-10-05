from urllib import urlencode

import urllib2
import time

from BeautifulSoup import BeautifulSoup


class Searcher:

    URL_PATTERN = u"https://github.com/search?q=%s+path%s+extension%s+size%s%d..%d&type=Code&ref=searchresults&p=%d"
    GITHUB_PREFIX = "http://www.github.com/"


    def __init__(self, start, end, step, args):
        self.start = start
        self.end = end
        self.step = step
        self.searchstring = args.searchstring
        self.path = args.path
        self.filename = args.filename
        self.delay = args.delay

    def searchrange(self):
        s, e = self.start, self.end
        while s < e:
            next_s = s + self.step
            yield (s, next_s)
            s = next_s

    def search(self, startsize, endsize, page, results):
        url = Searcher.URL_PATTERN % (self.searchstring, self.path, self.filename, "%3A", startsize, endsize, page)
        print "Executing query %s" % url
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        self._parse_results(soup, results)

    def _parse_results(self, soup, all_results):

        if len(soup.find_all(id="code_search_results")) == 0:
                raise NameError('No more results')

        for results in soup.find_all(id="code_search_results"):

            if len(results.find_all("div", "code-list-item-public")) == 0:
                raise NameError('No more results')

            for r in results.find_all("div", "code-list-item-public"):
                p = r.find_next("p", "title")
                repo_link = p.find_all("a")[0]
                repo = repo_link.text
                github_link = Searcher.GITHUB_PREFIX+repo
                filename = p.find_all("a")[1]['title']
                snippet = r.find_next("table", "highlight").prettify()
                if repo in all_results.projects:
                    print "Skipping result %s" % repo
                    continue
                else:
                    # now we need to get to the details - query the repo link
                    watched, starred, commits, contribs, git = Searcher.parse_repo_details(github_link)
                    print "Saving result %s" % repo
                    all_results.add(repo, github_link, snippet, filename, watched, starred, commits, contribs, git)
                    time.sleep(self.delay)

    @staticmethod
    def parse_repo_details(link):
        print "Executing query %s" % link
        response = urllib2.urlopen(link)
        html = response.read()
        soup = BeautifulSoup(html)
        # with open("/Users/philipp/Downloads/tmp.html", "w") as file:
        #      file.write(str(soup))
        # basic stats
        try:
            watched = int(soup.find("a", {"class" : "social-count"}).text.replace(",",""))
        except ValueError:
            watched = -1
        try:
            starred = int(soup.find("a", {"class" : "social-count js-social-count"}).text.replace(",",""))
        except ValueError:
            starred = -1
        # summary numbers
        summary_lis = soup.find("ul", {"class" : "numbers-summary"})
        try:
            commits = int(summary_lis.contents[1].find("a").find("span").text.replace(",",""))
        except ValueError:
            commits = -1
        try:
            contributors = int(summary_lis.contents[7].find("a").find("span").text.replace(",",""))
        except ValueError:
            contributors = -1
        # Git link
        git_link = soup.find("div", {"class" : "input-group js-zeroclipboard-container"}).find("input")['value']
        print "Found %d watched, %d starred, %d commits, %d contributors, and link %s" % (watched, starred, commits, contributors, git_link)
        return (watched, starred, commits, contributors, git_link)
