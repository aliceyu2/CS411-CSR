import pymysql.cursors
import datetime
import csv


allData = []
id = 1
with open("potHoles.csv",'r') as file:
    data = csv.reader(file,delimiter=',')
    for i in data:
        crDate = datetime.datetime.strptime(i[0], "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%d')
        if(i[2]==""):
            allData.append(tuple([str(id),crDate,None,i[4],i[1],1,i[8],i[9],"Chicago","Illinois",1]))
        else:
            comDate = datetime.datetime.strptime(i[2], "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%d')
            allData.append(tuple([str(id), crDate, comDate, i[4], i[1], 1, i[8], int(i[9]), "Chicago","Illinois",1]))
        id+=1
print(allData)

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="myPassword",
  database="teamHawkeye"
)
mydb.ping(True)
mycursor = mydb.cursor()

sql = "INSERT INTO servicerequests_request (requestNumber, creationDate,completionDate,requestType,status,priority,address,zipCode,city,state,user_id) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s)"

print(mycursor.executemany(sql,allData))

mydb.commit()
mycursor.close()