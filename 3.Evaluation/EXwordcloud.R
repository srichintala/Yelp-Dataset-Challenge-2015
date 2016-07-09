text <- Corpus(VectorSource(QueryFile))
text <- tm_map(text, PlainTextDocument)

text <- tm_map(text, removePunctuation)
text <- tm_map(text, removeWords, stopwords('english'))

text <- tm_map(text, stemDocument)

#wordcloud(text, max.words = 500, random.order = FALSE,colors=pal)

wordcloud(text, scale=c(5,0.5), max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, 'Dark2'))
