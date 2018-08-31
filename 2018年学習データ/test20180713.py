# -*- coding: utf-8 -*-
import requests
"""
Created on Fri Jul 13 16:39:49 2018

@author: T6014250
"""

rq=requests.get('http://cybersec.hatenadiary.jp/')
rq_conv=rq.text
print(rq_conv)