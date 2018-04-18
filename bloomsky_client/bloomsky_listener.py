import time, threading, urllib2 

def getToken():
	f = open('./tokens/tokens.txt')
	token = ''
	for token_line in f:
		token = token_line.strip()
	f.close()
	return token

def foo():
	print(time.ctime())
	token = getToken()
	print token
#	url = 'https://api.bloomsky.com/api/skydata/.?unit=intl'
	url = 'https://api.bloomsky.com/api/skydata/.?unit=intl'
	headers = {'Authorization:': token}
	req = urllib2.Request(url, None, headers=headers)
	req = urllib2.Request(url, None)
	resp = urllib2.urlopen(req).read(0)



#	contents = urllib2.urlopen("http://example.com/foo/bar").read()
#	print type(resp)
#   threading.Timer(10, foo).start()

foo()



