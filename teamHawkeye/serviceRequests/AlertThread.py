from geopy.geocoders import Nominatim
from geopy.distance import distance
import pymysql.cursors
from email.mime.text import MIMEText
import smtplib
import ssl

def distanceCheck(request=None):
    print(request)
    geolocator = Nominatim(user_agent="Team Hawkeye")
    location =  geolocator.geocode("{} {} {}".format(request['address'],request['city'],request['state']))
    #location = geolocator.geocode("1387 gander ln crystal lake IL")
    "A pot hole 311 service Request has beer reprted in you area at {} {} {}\n  "
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        passwd="myPassword",
        database="teamHawkeye"
    )
    mycursor = mydb.cursor()
    sql = "SELECT b.*, a.email FROM auth_user a,users_profile b WHERE a.id = b.user_id AND address IS NOT NULL AND email <> '' AND b.user_id <> {}".format(request['user_id'])

    mycursor.execute(sql)
    for i in mycursor.fetchall():
        print(i)
        userLocation = geolocator.geocode(i[3] + " " + i[4] + " " + i[5])
        if(distance((userLocation.longitude,userLocation.latitude),(location.longitude,location.latitude)).miles < 5):
            sendAlert(i[10],request)
    mycursor.close()

def sendAlert(email,request):
    subject = 'A 311 service request has been reported in your Area'
    body = "A service Request has beer reported in you area at {} {}, {}".format(request['address'],request['city'], request['state'])

    gmail_user = 'teamhawkeyeuiuc@gmail.com'
    gmail_password = 'myPassword'

    try:
        msg = MIMEText(body, "html")
        msg['From'] = "Chicago311@teamhawkeye.com"
        msg['To'] = email
        msg['CC'] = ""
        msg['Subject'] = subject
        msg['Content-Transfer-Encoding'] = 'base64'
        server = smtplib.SMTP_SSL('smtp-relay.gmail.com', 465 )

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(
                msg['From'], email, msg.as_string()
            )

        print('Email sent! to ' + str(email))
    except Exception as e:
        print(e)
    return
