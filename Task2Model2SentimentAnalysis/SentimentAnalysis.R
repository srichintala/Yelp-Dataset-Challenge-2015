# Code to analyze train data class distribution, visualization of word cloud for 
# generated features as per ratings and run different regression algorithms
# Author : Nayana Charwad

# histogram to analyze class distribution
hist(traindata$stars,main="Rating Frequencies Train Data",xlab="Review Ratings",col="slateBlue")

# Word cloud for all ratings
install.packages('wordcloud')
library('wordcloud')

# Rating 1
one <- read.csv('1.csv')
wordcloud(one$Feature, one$Count,scale=c(5,0.5),colors=brewer.pal(7,"Dark2"), max.words=200, random.order=FALSE)

# Rating 2
two <- read.csv('2.csv')
wordcloud(two$Feature, two$Count,scale=c(5,0.5),colors=brewer.pal(7,"Dark2"), max.words=200, random.order=FALSE)

# Rating 3
three <- read.csv('3.csv')
wordcloud(three$Feature, three$Count,scale=c(5,0.5),colors=brewer.pal(7,"Dark2"), max.words=200, random.order=FALSE)

# Rating 4
four <- read.csv('4.csv')
wordcloud(four$Feature, four$Count,scale=c(5,0.5),colors=brewer.pal(7,"Dark2"), max.words=200, random.order=FALSE)

# Rating 5
five <- read.csv('5.csv')
wordcloud(five$Feature, five$Count,scale=c(5,0.5),colors=brewer.pal(7,"Dark2"), max.words=200, random.order=FALSE)

# Read train and test data files
traindata <- read.csv('OutputTrainUniBi.csv')
testdata <- read.csv('OutputTestUniBi.csv')

# Run random forest regression algorithm 
install.packages('randomForest')
library('randomForest')
rf <- randomForest(stars~.,data=traindata,ntree=100)
predictionrf <- predict(rf,testdata,type="response")
write.csv(predictionrf,file="predictionrf.csv")

# Run svm regression algorithm 
install.packages('e1071')
library('e1071')
svm <- svm(stars~.,data=traindata)
predictiosvm <- predict(svm,testdata)
write.csv(predictiosvm,file="predictiosvm.csv")

# Compute RMSE for all algorithms
install.packages('hydroGOF')
library('hydroGOF')
simi <- read.csv('Prediction.csv',header=TRUE,nrows=1000)
obs <- read.csv('OutputTest.csv',header=TRUE,nrows=1000)
rmse(simi$x,obs$stars)

