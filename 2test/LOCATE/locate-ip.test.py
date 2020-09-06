from nose.tools import *
import pyipinfodb
import secrets

apikey = "d5aeba4d69afabb0e0dea9290be727132a1fff3c2a04ce64e00f3563a0e2125d"
i = pyipinfodb.IPInfo(apikey)

def test_country():
    ideal = {
        u'countryName': u'United States',
        u'ipAddress': u'155.33.148.202',
        u'countryCode': u'US',
        u'statusMessage': u'',
        u'statusCode': u'OK'
    }
    test = i.get_country('155.33.148.202')
    assert_equal(ideal, test)

def test_city():
    ideal = {u'cityName': u'Mountain View',
         u'countryCode': u'US',
         u'countryName': u'United States',
         u'ipAddress': u'8.8.8.8',
         u'latitude': u'37.406',
         u'longitude': u'-122.079',
         u'regionName': u'California',
         u'statusCode': u'OK',
         u'statusMessage': u'',
         u'timeZone': u'-07:00',
         u'zipCode': u'94043'
    }
    test = i.get_city('8.8.8.8')
    assert_equal(ideal, test)

test = i.get_country('155.33.148.202')
print(test)
test = i.get_city('8.8.8.8')
print("\n")
print(test)
