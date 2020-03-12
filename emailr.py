import json

import smtplib
from time import sleep

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from RepeatedTimer import RepeatedTimer

from datetime import datetime


with open('config.json', 'r') as f:
    config = json.load(f)
    print(config)

server = smtplib.SMTP(config['server'], config['port'])
server.starttls()

server.login(config['username'], config['password'])

import os
ip = 'ifconfig'

myCmd = os.popen('ifconfig').read() 

timestamp = datetime.now().strftime("%m/%d/%y")
subject = "ifconfig for {}".format(timestamp)
messageText = ''.join(e for e in myCmd if e.isalnum() or e.isspace() or e is '.')

message = 'Subject: {}\n\n{}'.format(subject, messageText)

server.sendmail(config['sender'], config['recipient'], message )


 
# rt = RepeatedTimer(1, hello, "World") # it auto-starts, no need of rt.start()
# try:
#     sleep(5) # your long-running job goes here...
# finally:
#     rt.stop() # better in a try/finally block to make sure the program ends!