#!/usr/bin/python
import requests
import sys

service          = sys.argv[1]
component_status = sys.argv[2]

with open('components') as f:
   for line in f:
       name, _id = line.split(":")
       if name == service:
           component_id = _id.strip()

print("service: ", service)
url = "https://status.fair.coop/api/v1/incidents"

headers = {'X-Cachet-Token': '5cEgd3u4drfag2HUd8sG', 'content-type': 'application/json'}
payload = "{\"name\":\"Odoodown\",\"message\":\"odoooverload\",\"visible\":1,\"status\":1,\"component_id\":%s,\"component_status\":%s,\"notify\":\"true\",\"created_at\":\"\"}" % (component_id, component_status)
response = requests.request("POST", url, headers=headers, data=payload)

incident_id = response.json()['data']['id']

text_file = open(service, "w")
text_file.write("%s" % incident_id)
text_file.close()
