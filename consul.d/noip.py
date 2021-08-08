#!/usr/bin/python3
# consul check for noip
from nslookup import Nslookup
from requests import get
import sys
try:
    domain = "mrsalehi.ddns.net"
    ip = get('https://api.ipify.org').text
    dns_query = Nslookup(dns_servers=["1.1.1.1"])
    ips_record = dns_query.dns_lookup(domain)
except:
    sys.exit(1)
for i in ips_record.answer:
    if(i == ip):
        print(f"no-ip : {i}")
        print(f"your-ip : {ip}")
        sys.exit(0)
    else:
        print(f"no-ip : {i}")
        print(f"your-ip : {ip}")
        sys.exit(3)
