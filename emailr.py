import json

import smtplib
from time import sleep

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from RepeatedTimer import RepeatedTimer

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

with open('config.json', 'r') as f:
    config = json.load(f)
    print(config)

server.login(config['username'], config['password'])

import os
ip = 'ifconfig'

myCmd = os.popen('ifconfig').read()

server.sendmail("bmahlbrand@gmail.com", "bmahlbrand@gmail.com", ''.join(e for e in myCmd if e.isalnum() or e.isspace() or e is '.'))



rt = RepeatedTimer(1, hello, "World") # it auto-starts, no need of rt.start()
try:
    sleep(5) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!