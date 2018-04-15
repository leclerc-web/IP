# -*-coding:Latin-1 -*

# API
import json
import urllib2
# IMPORT VARIABLE OS CLEAR
import os
# COULEUR TABLEAU
from colorclass import Color

# INPUT STRING
IP = raw_input("ENTER IP : ")



api_ip = 'http://ip-api.com/json/' + IP
query = json.load(urllib2.urlopen(api_ip))


if query and query['status'] == 'success' :

	os.system('cls' if os.name == 'nt' else 'clear')
	
	print "Code Pays : " + Color('{autored}' + query['countryCode'] + "{/autored}\n")
	print "Timezone : " + Color('{autored}' +  query['timezone'] + "{/autored}\n")
	print "Pays : " + Color('{autored}' + query['country'] + "{/autored}\n")
	print "Ville : " + Color('{autored}' + query['city'] + "{/autored}\n")
	print "Region : " + Color('{autored}' + query['regionName'] + "{/autored}\n")
	print "Code postal : " + Color('{autored}' + query['zip'] + "{/autored}\n")
	print "Longitude : " + Color('{autored}' + str(float(query['lon'])) + "{/autored}\n")
	print "Latitude : " + Color('{autored}' + str(float(query['lat'])) + "{/autored}\n")
	print "F.A.I : " + Color('{autored}' + query['org'] + "{/autored}\n")
	print "F.A.I AS NUMBER : " + Color('{autored}' + query['as'] + "{/autored}\n")
	print "IP : " + Color('{autored}' + query['query'] + "{/autored}\n")
	
else :

	print "error"
			