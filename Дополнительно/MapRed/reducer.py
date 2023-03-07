#! /usr/bin/env python3

import sys
from random import randrange

words = []
num = -1
sum_count = 0
n = randrange(1,6)
flag = True
for line in sys.stdin:
    try:
        word, count = line.strip().split(',')
    except ValueError as e:
        continue
    if n > 0 and flag == False:
        print(',' + word[8:], end = '')
        n-=1
    elif n > 0 and flag == True:
        print(word[8:], end = '')
        n-=1
        flag = False
    else:
        print()
        n = randrange(1,6)
        flag = True
