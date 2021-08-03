install.packages('rJava')
install.packages('memoise')
install.packages('multilinguer')
install.packages('remotes')
remotes::install_github('haven-jeon/KoNLP', upgrage='never', INSTALL_opts=c('--no-multiarch'))

library(RColorBrewer)
library(wordcloud)
library(KoNLP)

setwd('/Users/intaewoo/Desktop')

txt <- readLines("연설문.txt")noun <- sapply(txt,extractNoun,USE.NAMES=F)head(unlist(noun),50)write (unlist(noun), "연설문.txt")kim <- read.table("연설문.txt")nrow(kim)words <- table(kim)library(RColorBrewer)palete <- brewer.pal(5,"Set1")wordcloud(names(words),freq=words,scale=c(10,0,10),rot.per=0.5,min.freq=1, random.order=F,random.color=T,colors=palete)