df <- data.frame(country =c('KR','JP','CN'),
			cost1=c(11,16,19),
			cost2=c(28,14,37));
df
install.packages('ggplot2');

library(googleVis);
df
Line <- gvisLineChart(df);
plot(Line);

Line5 <- gvisLineChart(df, "country",c('cost1','cost2'),
options = list(gvis.editor = 'Edit me!'));
plot(Line5);

Bar <- gvisBarChart(df)
plot(Bar);

popu <- data.frame(area = c('Gyeonggi-do','Gangwon-do','Chungcheongnam-do',
'Chumgcheongbuk-do','Gyeongsangnam-do','Gyeongsangbuk-do','Jellanam-do','Jeollabuk-do','Jeju-do'),
population =c(1280,155,212,159,338,269,190,185,650))
popu

pie <- gvisPieChart(popu)
plot(pie);

Gauge <- gvisGauge(popu,
options = list(min=0, max=800, greenFrom=500, greenTo=800, yellowFrom=300, yellowTo=500, redFrom=0, redTo=300, width=400, height=300))
plot(Gauge)

Intencity <- gvisIntencityMap(df)

library(googleVis)
setwd('/Users/intaewoo/Downloads')
df <- read.csv('2018temp.csv', header=T) ## read.csv로 3년간 날씨 입력
df$dates <- as.Date(df$dates, format = '%Y-%m-%d');



Cal <- gvisCalendar(df, datevar='dates', numvar = 'temp', 
			options = list(
					title = 'Daily temperature in Seoul', 
					height = 320, 
					calendar = "{yearLabel: {fontName : 'Times-Roman',
					fonsize:32, color: '#1A8763', bold:trrue}, 
					cellSize : 10, 
					cellColor : {stroke :'red',strokeOpacity:0.2},
					focusedCellColor:{stroke:'red'}}'') )
			