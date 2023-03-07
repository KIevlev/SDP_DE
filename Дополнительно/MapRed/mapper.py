#! /usr/bin/env python3

import sys
import re
from random import randrange

for line in sys.stdin:
    try:
        words = line.strip().split('\n')
    except ValueError as e:
        print(e)
    for word in words:
        num = randrange(10000000, 99999999)
        print("{},{}".format(str(num)+word,1))
