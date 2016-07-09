Out.put.bar.plot <- read.csv("E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/experiments/output/Out put bar plot.txt", header=FALSE)
library(lattice)
#counts <- table(Out.put.bar.plot$V1, Out.put.bar.plot$V4)
#barplot(counts, main="Car Distribution by Gears and VS",
#        xlab="Number of Gears", col=c("darkblue","red"),
#        legend = rownames(counts), beside=TRUE)

barchart(Out.put.bar.plot$V2~Out.put.bar.plot$V1,groups=Out.put.bar.plot$V4, 
         scales=list(x=list(rot=90,cex=0.8)),ylab = 'precision',
         auto.key=list(space="top", columns=4, 
                       title="similarity and precision graph ", cex.title=1))
#legend(x=3.5,y=14,legend= c('lmd','vsm','lmj','bm25'),col=c(2,4,6,5))


barchart(Out.put.bar.plot$V3~Out.put.bar.plot$V1,groups=Out.put.bar.plot$V4, 
         scales=list(x=list(rot=90,cex=0.8)),ylab = 'recall',
         auto.key=list(space="top", columns=4, 
                       title="similarity and recall graph ", cex.title=1))
