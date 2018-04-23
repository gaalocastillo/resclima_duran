import datetime
import time, threading, urllib2
import time
from multiprocessing.dummy import Pool as ThreadPool 


def getTokens(filename):
	f = open(filename)
	tokens = []
	for token_line in f:
		token_line = token_line.strip()
		if len(token_line) > 0:
			tokens.append(token_line)
	f.close()
	return tokens

def printLines(linea):
	print linea
	print datetime.datetime.now().time()
	x = datetime.datetime.now().time()
	x = time.sleep(5)

def bloomsky_client(frequency, filename):
	while(True):
		tokens = getTokens(filename)
		n = len(tokens)
		pool = ThreadPool(n)
		results = pool.map(printLines, tokens)
 		pool.close() 
		pool.join()
		print 'FIN LAZO\n'
			

FILENAME = './lineas.txt'
FREQUENCY = 10
bloomsky_client(FREQUENCY, FILENAME)
