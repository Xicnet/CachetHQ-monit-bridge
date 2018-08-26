#!/usr/bin/python
import requests
import sys

service          = sys.argv[1]
component_status = int(sys.argv[2])

with open('components') as f:
   for line in f:
       name, _id = line.split(":")
       if name == service:
           component_id = _id.strip()

url = "https://status.fair.coop/api/v1/incidents"

if component_status == 1:
    status = "up"
if component_status == 2:
    status = "issue"

name = "%s %s" % (service, status)
message = "%s %s" % (service, status)

headers = {'X-Cachet-Token': '5cEgd3u4drfag2HUd8sG', 'content-type': 'application/json'}
payload = "{\"name\":\"%s\",\"message\":\"%s\",\"visible\":1,\"status\":1,\"component_id\":%s,\"component_status\":%s,\"notify\":\"true\",\"created_at\":\"\"}" % (name, message, component_id, component_status)
response = requests.request("POST", url, headers=headers, data=payload)

print("incident ID: ", response.text)
#import ipdb;ipdb.set_trace()
print "payload: ", payload
print "response: ", response
print

incident_id = response.json()['data']['id']

text_file = open(service, "w")
text_file.write("%s" % incident_id)
text_file.close()
