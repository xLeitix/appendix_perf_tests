'''
First attempt to automate the collection of metrics.
'''
import argparse
import csv
from collect_metrics.Tests import Tests
from subprocess import check_output
import json

def parse_cmd_params():
    '''
    Wrap the ugly cmd param parsing into a separate function.
    '''
    parser = argparse.ArgumentParser(description='Collect test metrics for collected projects.')
    parser.add_argument('-o', '--metricsfile', type=str, dest='metricsfile', default="metrics.csv")
    parser.add_argument('-i', '--inputfile', type=str, dest='inputfile', default="projects2.csv")
    parser.add_argument('-r', '--repodir', type=str, dest='repodir', default="/home/corpaul/workspace/repos/")
    parser.add_argument('-d', '--delimiter', type=str, dest='delimiter', default=';')

    return parser.parse_args()


def get_loc(self, repodir, tests, perftests, inclusive):
    cmd = "cd %s && cloc --csv %s | grep Java" % (repodir, tests)
    tests_loc = self.parse_cloc_output(check_output(cmd, shell=True))
    cmd = "cd %s && cloc --csv %s | grep Java" % (repodir, perftests)
    perftests_loc = self.parse_cloc_output(check_output(cmd, shell=True))

    if inclusive:
        self.comments = tests_loc['comments'] - perftests_loc['comments']
        self.code = tests_loc['code'] - perftests_loc['code']

    print "%s: tests loc: %s, performance tests loc: %s" % (project, tests_loc, perftests_loc)

    return

'''
Beginning of main script.
'''


# parse commandline parameters
args = parse_cmd_params()

print "Metric collector. Here are your arguments:"
print str(args)

with open(args.inputfile, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    with open(args.metricsfile, 'w') as outfile:
        header = "project;project_commits;project_committers;no_project_committers;test_loc;test_comments;test_commits;test_committers;no_test_committers;perftest_loc;perftest_comments;perftest_commits;perftest_committers;no_perftest_committers\n".replace(';', args.delimiter)
        outfile.write(header)
        for row in csvreader:
            project = row[0]
            fp = True if row[1] is "y" else False
            perftests = row[2]
            tests = row[3]
            inclusive = True if row[4] is "1" else False

            # fp or no project so skip
            if project is "" or fp or perftests is '?':
                continue

            # tmp (tests not filled in yet)
            if "/" not in tests:
                continue


            tests = Tests(project, tests, False, args.repodir)
            performance_tests = Tests(project, perftests, True, args.repodir)

            # Get LOC
            tests.get_loc()
            performance_tests.get_loc()

            # Get committers
            tests.get_committers()
            performance_tests.get_committers()

            tests.get_committers_project()

            print tests
            print performance_tests

            print json.loads(json.dumps(performance_tests.committers))[0][1]

            #outfile.write(tests.get_csv(args.delimiter))
            #outfile.write(performance_tests.get_csv(args.delimiter))
            # output a merged CSV file instead, is easier to use in R
            output = "%s;%d;%s;%d;%s;%s;%s;%s;%d;%s;%s;%s;%s;%d\n" \
                     % (tests.project, tests.commits_project, json.dumps(tests.committers_project), len(tests.committers_project), tests.loc, tests.comments, tests.commits, json.dumps(tests.committers), \
                        len(tests.committers), performance_tests.loc, performance_tests.comments, performance_tests.commits, \
                        json.dumps(performance_tests.committers), len(performance_tests.committers))
            outfile.write(output)