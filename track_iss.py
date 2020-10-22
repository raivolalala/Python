#!/usr/bin/python3

import urllib.request
import json

req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen(req)

obj = json.loads(response.read())

print(obj['timestamp'])
# print(obj['iss_position']['latitude'], obj['data']['iss_position']['latitude'])
print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])
