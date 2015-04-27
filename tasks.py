#!/usr/bin/env python
# -*- coding:utf-8 -*-

from celery import task

@task
def add(x,y):
    print x+y
    return x[0]+y[0]
