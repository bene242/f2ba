import ipinfo
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("access_token", help="please provide access-token from ipinfo.io")
args = parser.parse_args()

if args.access_token:
    accesstoken = args.access_token
    handler = ipinfo.getHandler(accesstoken)
    ip_address = '216.239.36.21'
    details = handler.getDetails(ip_address)
    print(details.city + " " + details.country + " " + details.country_name)
