# R Packages

# RODBC : DBMS에 연결을 위한 패키지
# sqldf : database의 문법을 사용 가능
# ggplot2 : 구글에서 제공하는 여러 plot
# rgoogleMaps : 구글에서 제공하는 지도

# sqldf
install.packages('sqldf')
install.packages('googleVis')
library(sqldf)
library(googleVis)
Fruits

sqldf("select * from Fruits")
sqldf("select * from Fruits where Profit > 13")

# correlation Analysis(상관분석)
mtcars
mtcolor <- cor(mtcars); round(mtcolor, 2)
install.packages('ggplot')
install.packages('corrplot')
library(corrplot)
library(ggplot2)
ggplot(mtcars,aes(disp,cvl)) + geom_point() # 계수가 0.902인 disp와 cvl 에 대한 산점도 그리기
(마력과 엔진 실린더와의 상관관계)
corrplot(mtcolor, method='shade', shade.col = NA, tl.col='blue', tl.srt=90)