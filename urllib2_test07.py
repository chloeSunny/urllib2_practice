#Filename:urllib2_test07.py

from urllib2 import Request,urlopen,URLError,HTTPError

req = Request('http://bbs.csdn.net/callmewhy')
try:
    response = urlopen(req)
except HTTPError,e:
    print('The server couldn\'t fulfill the request.')
    print('Error code:',e.code)
except URLError,e:
    print('We failed to reach a server.')
    print('Reason:',e.reason)
else:
    print('No exception was raised.')


#the HTTPError must be before the URLError
#urllib2_test05.py is a better way
