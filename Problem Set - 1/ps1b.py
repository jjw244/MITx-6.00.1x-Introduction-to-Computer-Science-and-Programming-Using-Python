#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:15:24 2017

course: MITx 6.00.1x: Introduction to Computer Science and Programming Using Python
source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017
"""

"""
Problem Set 1 - Problem 2
Instructions:
    
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print:

Number of times bob occurs is: 2
"""


"""Solution"""
s = 'psdvhymwnxvtlwxkz'
#s = 'pojeabobayrsjhd'
#s = 'vaqobobbobowboob'
#s = 'obobboobboeogwbobobboob'
#s = 'kbooxbobbvbooboobobbbobobtboobw'
#s = 'kcqtrbnaobobnbobbboboboowgkobob'
#s = 'rioboboobwbobobbobbcbbobbocxbob'
#s = 'bobobbosoobboobboobobojobobofboobbobbbobbobo'
#s = 'rbooboboobobbboboobhrfobobobobbbobbob'
#s = 'bobobobobobobobobob'
#s = 'lbobobobobboobboobbobobobooxooboboobooobbobbybobmk'

count = 0
i = 0
for word in s:
 if s[i:i+3] == 'bob':
  count += 1
  i += 1
 else:
  i += 1
print("Number of times bob occurs is: " + str(count))