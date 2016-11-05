#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 01:43:32 2016

@author: Hassan Shamim
"""
from hashlib import md5

secret = 'ckczppom'
n=6


i = 1
while md5((secret + str(i)).encode('utf-8')).hexdigest()[:n] != '0'*n:
    i += 1
print(i)