import ipinfo
access_token = '4c2d655ecc6909'
handler = ipinfo.getHandler(access_token)
ip_address = '216.239.36.21'
details = handler.getDetails(ip_address)
print(details.city + " " + details.country + " " + details.country_name)
