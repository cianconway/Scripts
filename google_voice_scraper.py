import urllib
from googlevoice import Voice
from googlevoice.util import input
import time
voice = Voice()
voice.login("cian.conway@outlook.com","password")
phoneNumber = "240-330-xxxx"
text = "Found available on page"
i=0
site = "" # Site URL
a=urllib.urlopen(site).read()
 
while a.find("0 available") != -1:
        time.sleep(60)
        a=urllib.urlopen(site).read()
        print a.find("0 available")
       
 
while i < 10:
        voice.send_sms(phoneNumber, text)
        time.sleep(60)
        i = i + 1