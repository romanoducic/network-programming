import smtplib
import smtpd

SERVER = 'localhost'
PORT = 1025

FROM = "9r9o99@gmail.com"
TO = ["myemailaddress@something.com"]
SUBJECT = "LV8"
TEXT = "Test"

message = """\
Sender: %s
Reciver: %s
Subject: %s
%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP(SERVER, PORT)
server.sendmail(FROM,TO,message)
server.quit()