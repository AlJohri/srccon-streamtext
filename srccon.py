# pip install requests

import requests, urllib, sys, time

last = 1
session = sys.argv[1]

while True:

	try:
		response = requests.get('http://www.streamtext.net/text-data.ashx?event=SRCCON%s&last=%d' % (session, last) )
		data = response.json()
		last = data['lastPosition']
		stuff = " ".join(map(lambda x: x['d'], data['i']))
		print urllib.unquote(stuff)
		time.sleep(2)
	except ValueError:
		print "Session %s is not running at the moment." % session
		break

sys.exit()