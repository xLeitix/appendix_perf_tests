library(reshape2)
library(magicaxis)
library(beanplot)
library(plyr)
library(effsize)
library(ggplot2)
library(viridis)
# read the metrics file with collected metrics
metrics = read.table("~/performance_tests_study/metrics_appended.csv", header=TRUE, sep=";")
metrics_sensitive = metrics[metrics$sensitive=="y",]
metrics_nonsensitive = metrics[metrics$sensitive=="n",]


# some simple stats about the number of perf test committers

hist(metrics$no_perftest_committers)
hist(metrics$no_project_committers)

######################################################################
# beanplot with project developers vs. performance test developers
######################################################################
pdf("~/performance_tests_study/paper/img/beanplot_developers.pdf", useDingbats=FALSE, width=9, height=6)
beanplot(metrics$no_perftest_committers, metrics$no_project_committers,
         what=c(0,1,1,0),
         col=list(c("#646464"),c("#C8C8C8")),
         beanlines = "median",
         cutmin = log(min(metrics$no_perftest_committers, metrics$no_project_committers)),
         cutmax = log(max(metrics$no_perftest_committers, metrics$no_project_committers)),
         horizontal = TRUE,
         side="both",
         axes = FALSE) +
  theme_bw(base_size=30)

magaxis(side=1, cex.axis = 1.5)
mtext(side=1, "# of developers", line=2, cex = 1.5)

legend("topright", fill = c("#C8C8C8", "#646464"), cex=1.3,
       legend = c("Project developers", "Performance test developers"), box.lty=0)
box()
dev.off()

######################################################################################
# boxplot to show performance test developers, project developers, test developers
######################################################################################
developers = data.frame(metrics$no_perftest_committers, metrics$no_test_committers, metrics$no_project_committers)
labels_developers = c("Performance test developers", "Test developers", "Project developers")

developers.df = melt(developers)

developers_meds <- ddply(developers.df, .(variable), summarise, med = round(median(value),2))


pdf("~/performance_tests_study/paper/img/boxplot_developers.pdf", useDingbats=FALSE, width=9, height=6)
ggplot(developers.df, aes(x=variable, y=value)) +
  geom_boxplot() +
  scale_x_discrete(labels=labels_developers) +
  scale_y_continuous(trans='log10') +
  ylab("# of developers") +
  xlab("") +
  scale_fill_viridis(discrete=TRUE, guide=FALSE) +
  geom_text(data = developers_meds, aes(x = variable, y = med, label = med),
            size = 6, vjust = -1) +
  theme_classic(base_size=20)
dev.off()

############################################################
# ratio of performance test developers
############################################################
ratio_committers_project = metrics$no_perftest_committers/metrics$no_project_committers
ratio_committers_tests = metrics$no_perftest_committers/metrics$no_test_committers

ratio_committers = data.frame(ratio_committers_project, ratio_committers_tests)
labels_ratio_committers = c(expression(frac("# of performance test developers", "total # of developers in project")),
                            expression(frac("# of performance test developers", "total # of test developers in project")))
ratio_committers.df = melt(ratio_committers)

ratio_committers_meds <- ddply(ratio_committers.df, .(variable), summarise, med = round(median(value),2))

# par(mfrow=c(1,1))
pdf("~/performance_tests_study/paper/img/boxplot_ratio_developers.pdf", useDingbats=FALSE, width=9, height=6)
ggplot(ratio_committers.df , aes(x=variable, y=value)) +
  geom_boxplot() +
  scale_x_discrete(labels=labels_ratio_committers) +
  ylab("Proportion of\n performance test developers") +
  xlab("") +
  scale_fill_viridis(discrete=TRUE, guide=FALSE) +
  geom_text(data = ratio_committers_meds, aes(x = variable, y = med, label = med),
            size = 6, vjust = -1) +
  theme_classic(base_size=20)
dev.off()

wilcox.test(ratio_committers_project, ratio_committers_tests, paired=TRUE)
cliff.delta(ratio_committers_project, ratio_committers_tests)
#####################################################################
# % of performance test developers that are top developers
#####################################################################
perc_perf_test_topdevs = metrics$perc_perf_test_topdevs
perc_test_topdevs = metrics$perc_test_topdevs

perc_topdevs = data.frame(perc_perf_test_topdevs, perc_test_topdevs)
labels_perc_topdevs = c("Performance test developers", "Test developers")
perc_topdevs.df = melt(perc_topdevs)

perc_topdevs_meds <- ddply(perc_topdevs.df, .(variable), summarise, med = round(median(value),2))

pdf("~/performance_tests_study/paper/img/boxplot_top_devs.pdf", useDingbats=FALSE, width=9, height=6)
ggplot(perc_topdevs.df, aes(x=variable, y=value)) +
  geom_boxplot() +
  scale_x_discrete(labels=labels_perc_topdevs) +
  ylab("Proportion of test developers \nwho are core developers of the project") +
  xlab("") +
  scale_fill_viridis(discrete=TRUE, guide=FALSE) +
  geom_text(data = perc_topdevs_meds, aes(x = variable, y = med, label = med),
            size = 6, vjust = -.5) +
  theme_classic(base_size=20)
dev.off()

wilcox.test(perc_perf_test_topdevs, perc_test_topdevs, paired=TRUE)
cliff.delta(perc_perf_test_topdevs, perc_test_topdevs)


####################################################################
# boxplot with commits
####################################################################
commits = data.frame(metrics$perftest_commits, metrics$test_commits-metrics$perftest_commits)
labels_commits = c("Performance tests", "Tests", "Performance tests\n(PS)", "Tests\n(PS)", "Performance tests\n(Not PS)", "Tests\n(Not PS)")
commits.df = melt(commits)


# add the commits for performance sensitive projects
commits_sensitive = data.frame(metrics_sensitive$perftest_commits, metrics_sensitive$test_commits-metrics_sensitive$perftest_commits)
labels_commits_sensitive = c("sensitive_commits", "sensitive_tests_commits")
names(commits_sensitive) = labels_commits_sensitive
commits_sensitive.df = melt(commits_sensitive)
commits.df = rbind(commits.df, commits_sensitive.df)


# add the LOC for performance sensitive projects
commits_nonsensitive = metrics[metrics$sensitive=="n",]
commits_nonsensitive = data.frame(metrics_nonsensitive$perftest_commits, metrics_nonsensitive$test_commits-metrics_nonsensitive$perftest_commits)
labels_commits_nonsensitive = c("nonsensitive_commits", "nonsensitive_tests_commits")
names(commits_nonsensitive) = labels_commits_nonsensitive
commits_nonsensitive.df = melt(commits_nonsensitive)
commits.df = rbind(commits.df, commits_nonsensitive.df)

commits_meds <- ddply(commits.df, .(variable), summarise, med = round(median(value),2))

pdf("~/performance_tests_study/paper/img/boxplot_commits.pdf", useDingbats=FALSE, width=9, height=6)
ggplot(commits.df, aes(x=variable, y=value)) +
  geom_boxplot() +
  scale_x_discrete(labels=labels_commits) +
  scale_y_continuous(trans='log10') +
  ylab("Number of commits") +
  xlab("") +
  scale_fill_viridis(discrete=TRUE, guide=FALSE) +
  geom_text(data = commits_meds, aes(x = variable, y = med, label = med),
            size = 6, vjust = 1.5) +
  theme_classic(base_size=20)
dev.off()


####################################################################
# boxplot with LOC
####################################################################
loc = data.frame(metrics$perftest_loc, metrics$test_loc-metrics$perftest_loc)
labels_loc = c("Performance\n tests", "Tests", "Performance\n tests (PS)", "Tests\n(PS)", "Performance\n tests(Not PS)", "Tests\n(Not PS)")
loc.df = melt(loc)

# add the LOC for performance sensitive projects
loc_sensitive = data.frame(metrics_sensitive$perftest_loc, metrics_sensitive$test_loc-metrics_sensitive$perftest_loc)
labels_loc_sensitive = c("sensitive_loc", "sensitive_tests_loc")
names(loc_sensitive) = labels_loc_sensitive
loc_sensitive.df = melt(loc_sensitive)
loc.df = rbind(loc.df, loc_sensitive.df)


# add the LOC for performance sensitive projects
loc_nonsensitive = data.frame(metrics_nonsensitive$perftest_loc, metrics_nonsensitive$test_loc-metrics_nonsensitive$perftest_loc)
labels_loc_nonsensitive = c("nonsensitive_loc", "nonsensitive_tests_loc")
names(loc_nonsensitive) = labels_loc_nonsensitive
loc_nonsensitive.df = melt(loc_nonsensitive)
loc.df = rbind(loc.df, loc_nonsensitive.df)

loc_meds <- ddply(loc.df, .(variable), summarise, med = round(median(value),2))

pdf("~/performance_tests_study/paper/img/boxplot_loc.pdf", useDingbats=FALSE, width=9, height=6)
ggplot(loc.df, aes(x=variable, y=value)) +
  geom_boxplot() +
  scale_x_discrete(labels=labels_loc) +
  scale_y_continuous(trans='log10') +
  ylab("Source Lines of Code (SLOC)") +
  xlab("") +
  scale_fill_viridis(discrete=TRUE, guide=FALSE) +
  geom_text(data = loc_meds, aes(x = variable, y = med, label = med),
            size = 6, vjust = 1.5) +
  theme_classic(base_size=20)
dev.off()

wilcox.test(loc_sensitive$sensitive_loc, loc_nonsensitive$nonsensitive_loc)


############################################################
# Some useful metrics
############################################################

# projects that have 1 performance test commit (i.e. no maintenance)
nrow(metrics[metrics$perftest_commits == 1,])
# projects that have 1 performance test developer and more than 10 developers
nrow(metrics[(metrics$no_perftest_committers==1 & metrics$no_project_committers > 9), c("project", "no_perftest_committers", "perc_perf_test_topdevs", "no_project_committers")])
# projects that have 1 performance test developer which is the top developer
nrow(metrics[(metrics$no_perftest_committers==1 & metrics$perc_perf_test_topdevs == 1), c("project", "no_perftest_committers", "perc_perf_test_topdevs", "no_project_committers")])


# beanplot for PS vs non-PS LOC
beanplot(loc_nonsensitive$nonsensitive_loc, loc_sensitive$sensitive_loc,
         what=c(0,1,1,0),
         col=list(c("#646464"),c("#C8C8C8")),
         beanlines = "median",
         cutmin = log(min(loc_nonsensitive$nonsensitive_loc, loc_sensitive$sensitive_loc)),
         cutmax = log(max(loc_nonsensitive$nonsensitive_loc, loc_sensitive$sensitive_loc)),
         horizontal = TRUE,
         side="both",
         axes = FALSE) +
  theme_bw(base_size=30)

magaxis(side=1, cex.axis = 1.5)
mtext(side=1, "# of developers", line=2, cex = 1.5)

legend("topright", fill = c("#C8C8C8", "#646464"), cex=1.3,
       legend = c("Project developers", "Performance test developers"), box.lty=0)
box()
