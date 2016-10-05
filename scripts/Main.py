import argparse
import sys
import sqlite3
import time
from urllib2 import HTTPError

from path_search.Search import Searcher
from path_search.SearchResult import SearchResults


def parse_cmd_params():
    '''
    Wrap the ugly cmd param parsing into a separate function.
    '''
    parser = argparse.ArgumentParser(description='Find projects with performance tests on GitHub.')
    parser.add_argument('-o', '--dbfile', type=str, dest='dbfile', default="searchresults.db")
    parser.add_argument('-f', '--fromsize', dest='start', type=int, default=1)
    parser.add_argument('-t', '--tosize', dest='end', type=int, default=sys.maxint)
    parser.add_argument('-s', '--step', dest='step', type=int, default=100)
    parser.add_argument('--filetype', dest='filename', type=str, default='%3Ajava')
    parser.add_argument('--path', dest='path', type=str, default='%3Asrc%2Ftest')
    parser.add_argument('--searchstring', dest='searchstring', type=str, default='perf+OR+bench')
    parser.add_argument('-nc', '--no-continue', dest='cont', action='store_false')
    parser.add_argument('-d', '--delay', dest='delay', type=int, default=12)
    return parser.parse_args()

'''
Beginning of main scraper script.
'''

# parse commandline parameters
args = parse_cmd_params()

print "Welcome to Scrapytown :) Here are your arguments:"
print str(args)

with sqlite3.connect(args.dbfile) as conn:

    # load old results if required
    results = SearchResults(conn)
    if args.cont:
        print "Loading previous results from the DB"
        results.load_from_db()
    else:
        print "Clearing DB - please confirm with <ENTER>"
        raw_input()
        results.clear_db()

    print "We are starting with %d results already in the database" % len(results.projects)

    searcher = Searcher(args.start, args.end, args.step, args)

    for beginsize, endsize in searcher.searchrange():

        for page in range(1,101):

            print "Looking at sizes %d - %d, page %d" % (beginsize, endsize, page)
            try:
                searcher.search(beginsize, endsize, page, results)
            except NameError:
                print "Apparently we ran out of pages. Let's continue with the next size"
                break
            time.sleep(args.delay)
