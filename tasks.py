from __future__ import absolute_import

from time import sleep

from celeryapp import app
from celery import chord, group


@app.task()
def pipeline():
    (begin.si() | middle.si() | end.si()).delay()

@app.task()
def begin():
    sleep(5)
    print "inizio"
    sleep(5)

@app.task()
def middle():
    tasks = []
    for i in range(10):
        tasks.append(single.si(i))
    (group(tasks) | (single.si(10).set(countdown=5))).delay()

@app.task()
def single(i):
    print i
    sleep(2)


@app.task()
def end():
    print "fine"
