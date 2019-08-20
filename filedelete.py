# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

file = os.listdir(os.getcwd())
for i in file:
    if i.startswith("新建文本文档"):
        with open('deletefile.txt', 'a') as f:
            f.write(i + '\n')

if os.path.exists('deletefile.txt'):
    with open('deletefile.txt', 'r') as f:

        a = f.readlines()
        for i in a:
            i = i.strip('\n')
            if os.path.exists(i):
                os.remove(i)

    if os.path.exists('deletefile.txt'):
        os.remove('deletefile.txt')
