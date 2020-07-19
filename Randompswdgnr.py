# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:02:08 2020

@author: wwwds
"""


import random
s = "abcdefghijkl\
    mnopqrstuwxyz1234\
    567890ABCDEFGHIJKLM\
    NOPQRSTUVWXYZ!@$%^^*\
    ()_-+[]{};/';.,"
passwordlen=16
password="".join(random.sample(s,passwordlen))
print(password)