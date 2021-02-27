from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models.query_utils import Q
from .settings import BASE_DIR
from woven.models import VirtualNuban, GetVirtualNuban
from woven.wovenapi import create_nuban, get_nuban
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

def create_nuban_and_get_nuban():
    status_code, response = create_nuban()
    if status_code == 200:
        VirtualNuban.objects.create(
            bank_name=response['data']['bank_name'],
            vnuban=response['data']['vnuban'],
            body=json.dumps(response)
        )
        scode, res = get_nuban(response['data']['vnuban'])
        if scode == 200:
            GetVirtualNuban.objects.create(
                body=json.dumps(res)
            )
    print(response)
        

scheduler.add_job(create_nuban_and_get_nuban, trigger='interval', minutes=1)
