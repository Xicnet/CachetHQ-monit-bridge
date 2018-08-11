#!/usr/bin/python
import requests
import sys
import json

url = "https://status.fair.coop/api/v1/components"

headers = {'X-Cachet-Token': '5cEgd3u4drfag2HUd8sG', 'content-type': 'application/json'}
response = requests.request("GET", url, headers=headers)

data = response.json()['data']

components_fd = open("components", "w")
for i in data:
    c = "%s:%s\n" % (i['name'], i['id'])
    components_fd.write(c)
components_fd.close()
