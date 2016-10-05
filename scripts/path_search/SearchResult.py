class SearchResults:

    def __init__(self, db):
        self.db = db
        self.projects = {}

    def add(self, name, url, snippet, filename, watched, starred, commits, contribs, git):
        self.projects[name] = ProjectWithPerfTest(name, url, snippet, filename, watched, starred, commits, contribs, git)
        self._save_result_to_db(self.projects[name])

    def _save_result_to_db(self, result):
        c = self.db.cursor()
        c.execute('INSERT INTO performance_tests (repo, repo_link, snippet, filename, watched, starred, commits, contributors, git) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                  (result.name, result.url, result.snippet, result.filename, result.watched, result.starred, result.commits, result.contribs, result.git))
        self.db.commit()

    def load_from_db(self):
        print "Defrosting previous results from database"
        self.projects = {}
        c = self.db.cursor()
        c.execute(
               '''CREATE TABLE IF NOT EXISTS performance_tests(
               repo TEXT NOT NULL,
               repo_link TEXT NOT NULL,
               snippet TEXT NOT NULL,
               filename TEXT NOT NULL,
               watched INTEGER NOT NULL,
               starred INTEGER NOT NULL,
               commits INTEGER NOT NULL,
               contributors INTEGER NOT NULL,
               git TEXT NOT NULL)'''
        )
        vals = c.execute('SELECT * FROM performance_tests')
        for repo, link, snippet, filename, watched, starred, commits, contributors, git in vals:
            self.projects[repo] = ProjectWithPerfTest(repo, link, snippet, filename, watched, starred, commits, contributors, git)
        print "Found %d previous results" % len(self.projects)


    def clear_db(self):
        c = self.db.cursor()
        c.execute(
               '''CREATE TABLE IF NOT EXISTS performance_tests(
               repo TEXT NOT NULL,
               repo_link TEXT NOT NULL,
               snippet TEXT NOT NULL,
               filename TEXT NOT NULL,
               watched INTEGER NOT NULL,
               starred INTEGER NOT NULL,
               commits INTEGER NOT NULL,
               contributors INTEGER NOT NULL,
               git TEXT NOT NULL)'''
        )
        c.execute(
               '''DELETE FROM performance_tests'''
        )
        self.db.commit()

class ProjectWithPerfTest:

    def __init__(self, name, url, snippet, filename, watched, starred, commits, contribs, git):
        self.name = name
        self.url = url
        self.snippet = snippet
        self.filename = filename
        self.watched = watched
        self.starred = starred
        self.commits = commits
        self.contribs = contribs
        self.git = git
