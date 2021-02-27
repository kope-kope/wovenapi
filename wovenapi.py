import requests
import time
import random
import string
import json

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

requestId2 = get_random_string(8)
cust = get_random_string(10)
base_url = 'https://api.woven.finance'
api_key = 'vb_ls_bfac75fe54a952841971b6918d06aeb2659523dc92d6'
requestId = time.time()

url = "{}/v2/api/vnubans/create_customer".format(base_url)

payload= {
        "customer_reference": cust,
        "name":"Oladokun Oluwatosin",
        "email":"tosin.oladokun@woven.finance",
        "mobile_number":"08012345678",
        "expires_on":"2021-02-28",
        "use_frequency":"5",
        "min_amount":2000,
         "max_amount":12000,
        "callback_url":"http://requesturl.com",
         "meta_data":{"somedatakey":"somedatavalue"}, "destination_nuban":""
}
headers = {
    'api_secret': api_key,
    'requestId': str(requestId),
    'Content-Type': 'application/json'
    }

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)

url = "{}/v2/api/vnubans/9101110164".format(base_url)

payload={}
headers = {
  'requestId': str(requestId2),
  'api_secret': 'vb_ls_bfac75fe54a952841971b6918d06aeb2659523dc92d6',
  'Cookie': '__cfduid=d2536ee6400a13b04b27b48cd6e65a3711613903352'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
