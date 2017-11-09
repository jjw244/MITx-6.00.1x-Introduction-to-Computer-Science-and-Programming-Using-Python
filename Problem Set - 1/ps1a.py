#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:15:24 2017

course: MITx 6.00.1x: Introduction to Computer Science and Programming Using Python
source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017
"""

"""
Problem Set 1 - Problem 1

Instructions:
    
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""


"""Solution"""
s = 'psdvhymwnxvtlwxkz'
#s = 'pnnxeb'
#s = 'zwfxqiiktp'
#s = 'vopgaSqhkdiyg'
#s = 'aemiifvhl'
#s = 'yuylluxrojbrrei'
#s = 'idatdcnjeixshyfexu'
#s = 'fibyeutnfbduepkavnbwafgz'
#s = 'okfemuszaqrdobnuudsvoy'
#s = 'tilitprutorataoiqbbej'
#s = 'giuurinzobgrcignedafua'

count = 0
for v in s:
    if v == 'a' or v== 'e' or v == 'i' or v == 'o' or v == 'u':
        count +=1
print("Number of vowels: " + str(count))