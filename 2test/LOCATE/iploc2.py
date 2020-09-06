# locate ip with databsase from https://lite.ip2location.com/
import os
import IP2Location

'''
    Cache the database into memory to accelerate lookup speed.
    WARNING: Please make sure your system have sufficient RAM to use this feature.
'''
# database = IP2Location.IP2Location(os.path.join("data", "IPV6-COUNTRY.BIN"), "SHARED_MEMORY")

database = IP2Location.IP2Location(os.path.join("../../../../", "IP2LOCATION-LITE-DB3.BIN"))

rec = database.get_all("19.5.10.1")

print(rec.country_short)
print(rec.country_long)
print(rec.region)
print(rec.city)
print(rec.isp)
print(rec.latitude)
print(rec.longitude)
print(rec.domain)
print(rec.zipcode)
print(rec.timezone)
print(rec.netspeed)
print(rec.idd_code)
print(rec.area_code)
print(rec.weather_code)
print(rec.weather_name)
print(rec.mcc)
print(rec.mnc)
print(rec.mobile_brand)
print(rec.elevation)
print(rec.usage_type)
