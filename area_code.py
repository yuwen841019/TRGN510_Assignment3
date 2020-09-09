#!/usr/bin/python
import fileinput
import re
import sys

phone = re.compile(r'\d{3}')
for Line in open(sys.argv[1], 'r').readlines():
    mo = phone.search(Line)
    print (mo.group())
