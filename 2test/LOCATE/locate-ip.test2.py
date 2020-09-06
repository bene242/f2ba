#from nose.tools import *
import pyipinfodb
import secrets

apikey = "d5aeba4d69afabb0e0dea9290be727132a1fff3c2a04ce64e00f3563a0e2125d"
i = pyipinfodb.IPInfo(apikey)

test = i.get_country('91.121.165.13')
print(test)
#test = i.get_city('91.121.165.13')
#print("\n")
#print(test)
