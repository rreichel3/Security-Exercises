##Exercise Summary:
An exploration of a good and bad login CAPTCHA implementation, that helps to illustrate how unhelpful bad implementations are. A CAPTCHA is a program intended to distinguish human from machine input as a way of thwarting spam and automated extraction of data from websites.

##Instructions:
1. The student should first have Docker and python installed and the Docker daemon running on a linux computer. (https://docs.docker.com/engine/installation/)
2. Next the student should run the script (startApacheContainer.sh) enclosed in the exercise folder to start up the container. 
3. Once the container is started they should navigate to http://127.0.0.1:8080/index.html and will be greeted with a basic page that points to the two login pages to play around with. One of these pages uses Google’s ReCAPTCHA to mitigate logins the other implements a not so secure method. 
4. Navigate to the bad CAPTCHA page and begin to play around.  Try logging in, etc and see view the source to see how it all works.
5. After playing around and noticing that it is using HTTP POST’s to try to login, check out the requests package (http://docs.python-requests.org/en/master/user/quickstart/) - it quickly allows POST requests. Using the provided wordlist.txt, write a short python program that attempts to brute force the bad example. Write down the password found on the line: ____________________________
6. Now try your program on the page using Google’s ReCAPTCHA and see what happens.
7. Discuss the cost and benefits to this type of verification. What might this help mitigate against? What are potential areas that an attacker can still exploit within the domain of a login?


*note the password list comes from https://github.com/danielmiessler/SecLists/ 
