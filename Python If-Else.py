#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input().strip())

if n % 2 == 0 and (n > 20 or (n < 5 and n > 1)) :
    print("Not Weird")
elif n > 6 and n < 20 :
    print("Weird")
else:
    print("Weird")
