from __future__ import absolute_import

from celery import Celery

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
BACKEND_URL = 'redis://localhost'

app = Celery('app', broker=BROKER_URL, backend=BACKEND_URL, include=['tasks'])

app.conf.update(
    CELERY_ACCEPT_CONTENT=['pickle', 'json'],
    CELERY_ACKS_LATE=True,
    CELERY_TASK_RESULT_EXPIRES=(4 * 3600),
    CELERYD_TASK_SOFT_TIME_LIMIT=500,
    CELERYD_TASK_TIME_LIMIT=800,
    CELERYD_MAX_TASKS_PER_CHILD=2,
    # CELERY_ALWAYS_EAGER=True,
    # CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
    # CELERYBEAT_SCHEDULE=schedule,
)

if __name__ == '__main__':
    app.start()
