import datetime
import csv
allData = []
with open("311-service-requests-pot-holes-reported.csv",'r') as file:
	data = csv.reader(file,delimiter=',')
	for i in data:
		allData.append(i)
		

startDate = "2018-01-01T00:00:00"
date = datetime.datetime.strptime(startDate,"%Y-%m-%dT%H:%M:%S")
linenumber = 0
newData = []
for i in allData:
	if(linenumber!=0):
		if(datetime.datetime.strptime(i[0],"%Y-%m-%dT%H:%M:%S") > date):
			if(i[8] != ""):
				newData.append(i)
	linenumber += 1
print(date.strftime("%Y-%m-%d"))

with open("potHoles.csv",'w+',newline='') as file:
	writer = csv.writer(file, delimiter=',')
	for i in newData:
		writer.writerow(i)