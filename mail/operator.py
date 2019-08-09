from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from django_apscheduler.jobstores import register_events, DjangoJobStore
import time
from .views import send_meilmail


def start():
    scheduler=BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    @scheduler.scheduled_job('cron', minute = '*/5', name = 'auto_mail')
    def auto_mail():
        send_meilmail()
    scheduler.start()