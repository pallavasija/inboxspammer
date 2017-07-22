#InboxSpammer (Python)

#Importing SMTP library

import time
import smtplib

#Specifying the From and To addresses

toadd = raw_input("Enter email address of the recipient [to]: ")

#Login credentials

uname = raw_input ('Enter your GMAIL username: ')
pwd = raw_input ('Enter your GMAIL password: ')

#Asking the user for the contents of the email(s)

message = raw_input ('Enter the message you want to send [body]: ')

#Connecting to GMAIL
print "Running for the first time? Check your email. Make sure to enable authentication for less secure apps"
time.sleep(3)
server =smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(uname,pwd)

#Specifying number of emails
num = int(raw_input("Enter the number of emails you want to send to the target: "))
for num in range (0,num):
 server.sendmail(uname,toadd,message)
 print "mail %d  sent" %(num+1)

#closing the connection
server.quit()

