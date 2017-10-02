#Rosseman sales prediction
library(data.table)
library(dplyr)
library(ggplot2)
train<-fread(('C:/Users/Akala/Desktop/DataPlay/Rossemann 20170913/2. Prepared Data/train.csv'))
test<-fread(('C:/Users/Akala/Desktop/DataPlay/Rossemann 20170913/2. Prepared Data/test.csv'))
store<-fread(('C:/Users/Akala/Desktop/DataPlay/Rossemann 20170913/2. Prepared Data/store.csv'))

train[, Date := as.Date(Date)]
test[, Date := as.Date(Date)]
train <- train[order(Date)]
test <- test[order(Date)]
summary(train)
summary(test) #11 na in open

#missing data
test[is.na(test$Open), ] # all na come from store 622
test$Open[test$Store == 622]# have a closer look
test[test$Store ==622]
test[is.na(test)] <- 1 #assume the 622 is open 

train[, lapply(.SD, function(x) length(unique(x)))]
