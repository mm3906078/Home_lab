#!/usr/bin/python3
import requests
import json
import sys


IP_API = 'https://api.ipify.org?format=json'
# Get CF API Key: https://support.cloudflare.com/hc/en-us/articles/200167836-Where-do-I-find-my-Cloudflare-API-key-
CF_API_KEY = 'REPLACE ME'
# Your cloudflare email address
CF_EMAIL = 'REPLACE@ME.COM'
# Your zone id is located on the main cloudflare domain dashboard
ZONE_ID = 'REPLACE ME'
# Run script once without this set and it'll retrive a list of records for you to find the ID to update here
RECORD_ID = ''



if not RECORD_ID:
    resp = requests.get(
        'https://api.cloudflare.com/client/v4/zones/{}/dns_records'.format(ZONE_ID),
        headers={
            'X-Auth-Key': CF_API_KEY,
            'X-Auth-Email': CF_EMAIL
        })
    print(json.dumps(resp.json(), indent=4, sort_keys=True))
    print('Please find the DNS record ID you would like to update and entry the value into the script')
    sys.exit(0)

resp = requests.get(IP_API)
ip = resp.json()['ip']


resp = requests.put(
    'https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}'.format(
        ZONE_ID, RECORD_ID),
    json={
        'type': 'A',
        'name': 'test',
        'content': ip,
        'proxied': False
    },
    headers={
        'X-Auth-Key': CF_API_KEY,
        'X-Auth-Email': CF_EMAIL
    })
assert resp.status_code == 200

print('updated dns record for {}'.format(ip))
