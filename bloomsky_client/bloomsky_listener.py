import time, threading, urllib2 

def foo():
	print(time.ctime())
#	url = 'https://api.bloomsky.com/api/skydata/.?unit=intl'
	url = 'https://api.bloomsky.com/api/skydata/.?unit=intl'
	headers = {'Authorization:': 'tdbDpM7ktbTRos6iv3C76dQ='}
	req = urllib2.Request(url, None, headers=headers)
	req = urllib2.Request(url, None)
	resp = urllib2.urlopen(req).read(0)



#	contents = urllib2.urlopen("http://example.com/foo/bar").read()
#	print type(resp)
#   threading.Timer(10, foo).start()

foo()



