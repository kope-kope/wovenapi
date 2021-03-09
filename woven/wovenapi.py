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

def create_mandate():
  requestId2 = get_random_string(8)
  url = "{}/v1/api/directdebits/mandates".format(base_url)
  faker = Faker()

  payload = {
    "customer_name": faker.name().split()[0] + " " + get_random_number(),
    "customer_email": faker.email(),
    "customer_mobile": "08012345678",
    "customer_reference": get_random_string(10),
    "account_number": str(os.getenv("DD_BENEFICIARY_NUBAN")),
    "amount": get_amount(),
    "currency": "NGN",
    "call_back_url": "",
    "mandate_type": "direct",
    "narration": "automated direct debit",
    "bank_code": "044"
  }

  # payload=" {\r\n    \"customer_name\": \"$Jared Bednar V\",\r\n    \"customer_email\": \"$Hillary36@hotmail.com\",\r\n    \"customer_mobile\": \"08012345678\",\r\n    \"customer_reference\": \"$1750f9ed-95e9-40d8-ae02-3444bf732edd\",\r\n    \"account_number\": \"1227140382\",\r\n    \"bank_code\": \"044\",\r\n    \"amount\": 100,\r\n    \"currency\": \"NGN\",\r\n    \"call_back_url\": \"\",\r\n    \"mandate_type\": \"direct\",\r\n    \"narration\": \"automated direct debit\"\r\n  }"

  headers = {
    'requestId': str(requestId2),
    'api_secret': api_key,
    'Content-Type': 'application/json'
  }
  start_time = get_time()
  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
  stop_time = get_time()

  print(response.json())

  return response.status_code, response.json(), start_time, stop_time

def verify_mandate(otp, mandate_ref):
  print(otp)
  requestId2 = get_random_string(8)
  url = "{}/v1/api/directdebits/mandates/{}".format(base_url, mandate_ref)
  faker = Faker()

  payload = {
    "otp": otp
  }

  headers = {
    'requestId': str(requestId2),
    'api_secret': api_key,
    'Content-Type': 'application/json'
  }
  start_time = get_time()
  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
  stop_time = get_time()

  print(response.json())

  return response.status_code, response.json(), start_time, stop_time