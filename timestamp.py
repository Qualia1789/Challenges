#!/bin/python

import math
import os
import random
import re
import sys

raw_input_string = ''' 2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000 '''

raw_input_list = raw_input_string.split('\n')

def raw_input():
    return raw_input_list.pop(0)

# Complete the time_delta function below.
def time_delta(t1, t2):
    print(t1)
    

    
  

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in range(t):
        t1 = raw_input()

        t2 = raw_input()

        delta = time_delta(t1, t2)

    #    fptr.write(delta + '\n')

    #fptr.close()
