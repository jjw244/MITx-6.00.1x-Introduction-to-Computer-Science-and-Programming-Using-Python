# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:06:06 2016

@author: ericgrimson
"""

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
