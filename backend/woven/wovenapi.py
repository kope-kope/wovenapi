import faker
import requests
import time
import random
import string
import json
import datetime
from faker import Faker
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

def get_time():
  current = datetime.datetime.now()
  return current.strftime("%H:%M:%S:%f")

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_number():
  numbers = list(range(10))
  result_str = ''.join(str(random.choice(numbers)) for i in range(5))
  return result_str

base_url = os.getenv('BASE_URL')
api_key = os.getenv('API_KEY')

def create_nuban():
  
  cust = get_random_string(10)
  requestId = get_time()
  faker = Faker()

  url = "{}/v2/api/vnubans/create_customer".format(base_url)

  payload= {
  "customer_reference": cust,
  "name": faker.name().split()[0] + " " + get_random_number(),
  "email": faker.email(),
  "mobile_number": "08123258600",
  "expires_on": str(datetime.date.today() + datetime.timedelta(days=1)),
  "callback_url": os.getenv("CALLBACK_URL"),
  "meta_data":{"somedatakey": "somedatavalue"}, "destination_nuban":""
  }

  headers = {
    'api_secret': api_key,
    'requestId': str(requestId),
    'Content-Type': 'application/json'
  }
  start_time = get_time()
  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
  stop_time = get_time()
  return response.status_code, response.json(), start_time, stop_time

def get_nuban(nuban):
  
  requestId2 = get_random_string(8)
  url = "{}/v2/api/vnubans/{}".format(base_url, nuban)

  payload={}
  headers = {
    'requestId': str(requestId2),
    'api_secret': api_key,
  }

  start_time = get_time()
  response = requests.request("GET", url, headers=headers, data=payload)
  stop_time = get_time()

  return response.status_code, response.json(), start_time, stop_time

def get_amount():
  value = random.random() * 100
  if value < 50:
    return 50
  return int(value)

def initiate_payout():
  requestId2 = get_random_string(8)
  url = "{}/v2/api/payouts/request?command=initiate".format(base_url)

  payload = {
    "source_account": os.getenv("SOURCE_ACCOUNT"),
    "PIN": os.getenv("PIN"),
    "beneficiary_account_name": os.getenv("BAN"),
    "beneficiary_nuban": os.getenv("BENEFICIARY_NUBAN"),
    "beneficiary_bank_code": os.getenv("BENEFICIARY_BANK_CODE"),
    "bank_code_scheme": "NIP",
    "currency_code": "NGN",
    "narration": "Automated payout",
    "amount": get_amount(),
    "reference": get_random_string(10),
    "callback_url": os.getenv("CALLBACK_URL")
  }

  headers = {
    'requestId': str(requestId2),
    'api_secret': api_key,
  }
  start_time = get_time()
  response = requests.request("POST", url, headers=headers, data=payload)
  stop_time = get_time()

  print(response.json())

  return response.status_code, response.json(), start_time, stop_time

def list_settlements():
  requestId2 = get_random_string(8)
  url = "{}/v2/api/settlements".format(base_url)

  payload = {
  }

  headers = {
    'requestId': str(requestId2),
    'api_secret': api_key,
  }
  start_time = get_time()
  response = requests.request("GET", url, headers=headers, data=payload)
  stop_time = get_time()

  print(response.json())

  return response.status_code, response.json(), start_time, stop_time


def list_transactions():
  requestId2 = get_random_string(8)
  url = "{}/v1/api/transactions".format(base_url)

  payload = {
  }

  headers = {
    'requestId': str(requestId2),
    'api_secret': api_key,
  }
  start_time = get_time()
  response = requests.request("GET", url, headers=headers, data=payload)
  stop_time = get_time()

  print(response.json())

  return response.status_code, response.json(), start_time, stop_time


def list_vnuban():
  requestId2 = get_random_string(8)
  url = "{}/v2/api/vnubans".format(base_url)

  payload = {
  }

  headers = {
    'requestId': str(requestId2),
    'api_secret': api_key,
  }
  start_time = get_time()
  response = requests.request("GET", url, headers=headers, data=payload)
  stop_time = get_time()

  print(response.json())

  return response.status_code, response.json(), start_time, stop_time
