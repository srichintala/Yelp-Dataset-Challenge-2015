#thai.word.cloud <- read.csv("E:/Study stuff/Subjects and courses/Z 534 info retrival/Project/Project stuff/Task 1/thai word cloud.txt", header=FALSE)




#wordcloud(words=thai.word.cloud$V1,freq = thai.word.cloud$V2, scale=c(5,0.5), max.words=200, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, 'Dark2'))

#wordcloud(words=thai.word.cloud$V1,freq = thai.word.cloud$V2, scale=c(5,0.5), max.words=150, random.order=TRUE, colors=brewer.pal(8, 'Dark2'))

#family <- as.factor(data[,4])

col.list <- c("red","slategray","seagreen",'green',"blue",'black')
palette(col.list)
#plot(plot75_lmj$V2,plot75_lmj$V3,xlab = 'Precision',ylab = 'Recall',main = 'Precission  VS recall',pch=19,col=col.list)
plot(plot75_lmj$V2,plot75_lmj$V3,xlab = 'Precission',ylab = 'Recall',main = 'Precission  VS recall',type='n')
#k <- plot100[plot100$V2 > 0.45 && plot100$V3 > 0.45]
text(plot75_lmj$V2,plot75_lmj$V3,plot75_lmj$V1)
