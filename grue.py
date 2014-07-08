#!/usr/bin/env python
import urllib2
import urllib
from cookielib import CookieJar
from datetime import datetime
import json
import knockknock

commands = ['GLOBAL THERMONUCLEAR WAR', 'turn on flashlight', 'west', 'use keypad', 'admin                         .',
	    'west', 'take matches', 'light match', 'light candle', 'move carpet', 'use lock', '3592', 'down', 'look at paper', 
	    'n', 'use touch screen', 'CONTRA', 'push button', 'push button', 's', 
	    's', 'use touch screen', 'FROGGER', 'push button', 'push button', 'n',
	    'w', 'use touch screen', 'FLOWER', 'push button', 'e', 'e', 'use touch screen', 'NITRO', 'push button', 'w', 'w',
	    'push button', 'e', 'e', 'push button', 'w', 'push green button', 'use laptop'
	   ]

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

def parsedate(date):
	#"Tue, Jul 08, 2014  10:19:02 AM"
	dt = datetime.strptime(date, '%a, %b %d, %Y  %H:%M:%S %p')
	if (dt.second < 30):
	    dt = datetime.strptime(date.rpartition(':')[0] + ":00", '%a, %b %d, %Y  %H:%M:%S')
	else:
	    #dt.second = 30
	    dt = datetime.strptime(date.rpartition(':')[0] + ":30", '%a, %b %d, %Y  %H:%M:%S')
	return dt.strftime("%m%d%Y%H%M%S")

def send(command, raw = True):
	# input-type values from the html form
	if raw:
	    formdata = { "inprompt" : command.upper()}
	else:
	    formdata = { "inprompt" : command}
	data_encoded = urllib.urlencode(formdata)
	response = opener.open("https://bsjtf.com/command.php", data_encoded)
	content = response.read()
	return content

def start():
    for command in commands:
	print send(command)
	

def endgame():
	command = "date"
	r = json.loads(send(command))
	date=r['DISPLAY'].replace('&nbsp;', " ")
	now = parsedate(date)
	firsthacker = "Nevil Maskelyne"
	rats = ".-. .-- ..."
	year = "1903"
	passcode = knockknock.getaccess(firsthacker, rats, year, now)
	print send('nc 10.2.1.3 4444')
	print send(passcode, False)

def restart():
    print send('restart')


start()
endgame()

# Code used to brute the code..

#counter = 0
#for combo in range(9999):
#	formdata = { "inprompt" : "%04d" % combo}
#	data_encoded = urllib.urlencode(formdata)
#	response = opener.open("https://bsjtf.com/command.php", data_encoded)
#	content = response.read()
#	print content
#	if content.startswith("That"):
#	    break
#	counter += 1
#	if counter == 5:
#	    counter = 0
#	    restart()
#	    start()


