import requests
import json
from pprint import pprint

#################### LOGIN ####################
url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"
        }
    }
}

headers = {"content-type": "application/json"}

response = requests.post(
    url,
    data=json.dumps(payload),
    headers=headers,
    verify=False
).json()

# print(json.dumps(response, indent=2, sort_keys=True))

token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]

cookies = {}
cookies['APIC-cookie'] = token

#################### GET LIST OF APN ####################

url = "https://sandboxapicdc.cisco.com/api/class/fvAp.json"

headers = {'cache-control': 'no-cache'}

get_response = requests.get(
    url,
    headers=headers,
    cookies=cookies,
    verify=False
).json()

# pprint(json.dumps(get_response, indent=2, sort_keys=True))

#################### GET APN ####################

url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Lab-Tenant/ap-Lab-App-Profile.json"

headers = {'cache-control': 'no-cache'}

get_response = requests.get(
    url,
    headers=headers,
    cookies=cookies,
    verify=False
).json()

# print(json.dumps(get_response, indent=2, sort_keys=True))

#################### UPDATE APN DESCRIPTION ####################

post_payload = {
    "fvAp": {
        "attributes": {
            "descr": "Python Demo",
            "dn": "uni/tn-Lab-Tenant/ap-Lab-App-Profile"
        }
    }
}

post_response = requests.post(
    url,
    headers=headers,
    data=json.dumps(post_payload),
    cookies=cookies,
    verify=False
).json()

print(json.dumps(post_response, indent=2, sort_keys=False))




