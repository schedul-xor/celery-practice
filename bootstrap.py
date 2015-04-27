#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tasks import add
import celery

ids = []
for i in range(1000):
    ids.append(i)

rs = []
for i in ids:
    r = add.s([i,2],[i+1,3])
    rs.append(r)
    
jobs = celery.group(rs)
results = jobs.apply_async()
print results.get()
