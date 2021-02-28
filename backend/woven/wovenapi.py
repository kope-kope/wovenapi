import faker
import requests
import time
import random
import string
import json
import datetime
from faker import Faker
import os

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

base_url = 'https://api.woven.finance'
api_key = os.environ.get('WOVENAPISECRET')

def create_nuban():
  
  cust = get_random_string(10)
  requestId = time.time()
  faker = Faker()

  url = "{}/v2/api/vnubans/create_customer".format(base_url)

  payload= {
  "customer_reference": cust,
  "name": faker.name(),
  "email": faker.email(),
  "mobile_number": "08123258600",
  "expires_on": str(datetime.date.today() + datetime.timedelta(days=1)),
  "use_frequency": "5",
  "min_amount": 2000,
  "max_amount": 12000,
  "callback_url": "http://requesturl.com",
  "meta_data":{"somedatakey": "somedatavalue"}, "destination_nuban":""
  }

  headers = {
    'api_secret': api_key,
    'requestId': str(requestId),
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

  return response.status_code, response.json()

def get_nuban(nuban):
  requestId2 = get_random_string(8)
  url = "{}/v2/api/vnubans/{}".format(base_url, nuban)

  payload={}
  headers = {
    'requestId': str(requestId2),
    'api_secret': 'vb_ls_bfac75fe54a952841971b6918d06aeb2659523dc92d6',
    'Cookie': '__cfduid=d2536ee6400a13b04b27b48cd6e65a3711613903352'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  return response.status_code, response.json()
