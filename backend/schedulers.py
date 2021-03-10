from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models.query_utils import Q
from .settings import BASE_DIR
from woven.models import CreateVirtualNuban, GetVirtualNuban, APIRequest, MandateId
from woven.wovenapi import (
    create_nuban, get_nuban, initiate_payout, 
    list_settlements, list_transactions, list_vnuban,
    create_mandate
)
import json

import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)


# The "apscheduler." prefix is hard coded
scheduler = BackgroundScheduler({
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///' + (BASE_DIR / 'db.sqlite3').as_posix()
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': 'UTC',
})

scheduler.start()
scheduler.remove_all_jobs()

def get_status(status_code):
    if status_code in [200, 201]:
        return 'successful'
    return 'failed'

def create_nuban_and_get_nuban():
    status_code, response, start_time, end_time = create_nuban()
    if status_code == 200:
        CreateVirtualNuban.objects.create(
            bank_name=response['data']['bank_name'],
            vnuban=response['data']['vnuban'],
            body=json.dumps(response)
        )
        APIRequest.objects.create(
            call_type='create_vnuban',
            start_time=start_time,
            end_time=end_time,
            status='successful',
            status_message=json.dumps(response)
        )
        scode, res, stime, etime = get_nuban(response['data']['vnuban'])
        if scode == 200:
            GetVirtualNuban.objects.create(
                body=json.dumps(res)
            )
            APIRequest.objects.create(
                call_type='get_vnuban',
                start_time=stime,
                end_time=etime,
                status='successful',
                status_message=json.dumps(res)
            )
        else:
            APIRequest.objects.create(
                call_type='get_vnuban',
                start_time=stime,
                end_time=etime,
                status='failed',
                status_message=json.dumps(res)
            )
    else:
        APIRequest.objects.create(
            call_type='get_vnuban',
            start_time=start_time,
            end_time=end_time,
            status='failed',
            status_message=json.dumps(response)
        )
    status_code, response, start_time, end_time = initiate_payout()
    APIRequest.objects.create(
        call_type='initiate_payout',
        start_time=start_time,
        end_time=end_time,
        status=get_status(status_code),
        status_message=json.dumps(response)
    )
    status_code, response, start_time, end_time = list_settlements()
    APIRequest.objects.create(
        call_type='list_settlements',
        start_time=start_time,
        end_time=end_time,
        status=get_status(status_code),
        status_message=json.dumps(response)
    )
    status_code, response, start_time, end_time = list_transactions()
    APIRequest.objects.create(
        call_type='list_transactions',
        start_time=start_time,
        end_time=end_time,
        status=get_status(status_code),
        status_message=json.dumps(response)
    )
    status_code, response, start_time, end_time = list_vnuban()
    APIRequest.objects.create(
        call_type='list_vnuban',
        start_time=start_time,
        end_time=end_time,
        status=get_status(status_code),
        status_message=json.dumps(response)
    )
    status_code, response, start_time, end_time = create_mandate()
    APIRequest.objects.create(
        call_type='create_mandate',
        start_time=start_time,
        end_time=end_time,
        status=get_status(status_code),
        status_message=json.dumps(response)
    )
    if (status_code == 201):
        MandateId.objects.create(mandate_id=response["body"]["mandate_reference"])

scheduler.add_job(create_nuban_and_get_nuban, trigger='interval', minutes=60)
