import argparse
import csv
import json

def parse_cmd_params():
    '''
    Wrap the ugly cmd param parsing into a separate function.
    '''
    parser = argparse.ArgumentParser(description='Analyze test metrics for collected projects.')
    parser.add_argument('-i', '--inputfile', type=str, dest='inputfile', default="metrics.csv")
    parser.add_argument('-o', '--outputfile', type=str, dest='outputfile', default="metrics_appended.csv")
    return parser.parse_args()


# >>> x = ast.literal_eval(x)


'''
Beginning of main script.
'''


# parse commandline parameters
args = parse_cmd_params()

print "Metric collector. Here are your arguments:"
print str(args)

with open(args.inputfile, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    with open(args.outputfile, 'w') as csv_outfile:
        csvwriter = csv.writer(csv_outfile, delimiter=';', quotechar='|')
        # skip headers
        header = csvreader.next()
        header.append("perc_perf_test_topdevs")
        header.append("perc_test_topdevs")
        header.append("one_timers_perf_test")
        header.append("one_timers_test")
        csvwriter.writerow(header)

        for row in csvreader:
            # header = "project;project_commits;project_committers;no_project_committers;test_loc;test_comments;test_commits;test_committers;no_test_committers;perftest_loc;perftest_comments;perftest_commits;perftest_committers;no_perftest_committers\n".replace(';', args.delimiter)
            project_committers = json.loads(row[2])
            test_committers = json.loads(row[7])
            no_test_committers = float(row[8])
            perf_test_committers = json.loads(row[12])
            no_perf_test_committers = float(row[13])

            rank = 0
            perf_test_topdevs = 0
            test_topdevs = 0
            one_timers_perf_test = 0
            one_timers_test = 0

            for c in perf_test_committers:
                for i, p in enumerate(project_committers):
                    if c[1] == p[1]:
                        rank = rank + 1
                        # check if this is a project top developer
                        if i < no_perf_test_committers:
                            perf_test_topdevs = perf_test_topdevs + 1
                        break
                    rank = rank + 1
                if c[0] == 1:
                    one_timers_perf_test = one_timers_perf_test + 1


                #print "%s, %s: %s" % (perf_test_committers, project_committers, rank)
            # calculate the percentage of test developers who are top developers

            for c in test_committers:
                for i, p in enumerate(project_committers):
                    if c[1] == p[1]:
                        # check if this is a project top developer
                        if i < no_test_committers:
                            test_topdevs = test_topdevs + 1
                        break
                if c[0] == 1:
                    one_timers_test = one_timers_test + 1

            print row[0]
            print perf_test_committers
            print test_committers
            print project_committers
            print "Cumulative rank: %s" % rank
            print "Percentage of performance test developers in top-%d: %f" % (no_perf_test_committers, perf_test_topdevs/no_perf_test_committers)
            print "Percentage of test developers in top-%d: %f" % (no_test_committers, test_topdevs / no_test_committers)
            print "One-timers: performance %d, test %d" % (one_timers_perf_test, one_timers_test)
            print "-----------------------------------------"

            row.append(perf_test_topdevs/no_perf_test_committers)
            row.append(test_topdevs/no_test_committers)
            row.append(one_timers_perf_test)
            row.append(one_timers_test)
            csvwriter.writerow(row)

