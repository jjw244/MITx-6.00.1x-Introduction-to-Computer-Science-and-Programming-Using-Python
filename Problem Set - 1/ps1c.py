#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:15:24 2017

course: MITx 6.00.1x: Introduction to Computer Science and Programming Using Python
source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017
"""

"""
Problem Set 1 - Problem 3
Instructions:
    
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print:

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print:

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a break and cleared your head.
"""


"""Solution"""
s = 'spdfhymwnxvtljxkz'
#s = 'zyxwvutsrqponmlkjihgfedcba'
#s = 'razeznbh'
#s = 'njkcugedgfvjrhjmkocphje'
#s = 'jsckxwnwgsvx'
#s = 'rqmrraejplpqgrwzzelbjec'
#s = 'oxjvgbwisghotxgqaihf'
#s = 'eemwaootkaahepwhdfgklry'
#s = 'ywhuygyewfmjptwpomnmgnz'
#s = 'mgiybpdyqsozxixm'
#s = 'abcdefghijklmnopqrstuvwxyz'

longest = ''
temp = ''
for i in range(len(s)-1):
 if s[i] <= s[i+1]:
  temp += s[i]
  if 1 != len(s[len(s)-1:i+2]) and s[i] <= s[i+1] > s[i+2]:
   temp += s[i+1]
   print(temp, longest, s[i])
  if 1 == len(s[len(s)-1:i+2]) and temp[len(temp)-1:len(temp)] <= s[len(s)-1:len(s)]:
   temp += s[i+1]
 elif s[i] > s[i+1]:
  if len(temp) > len(longest):
   longest = temp
  temp = ''
if len(temp) == 0:
  temp = s[0]
if len(longest) == 0 or len(longest) == 1 or len(temp) > len(longest):
  longest = temp
print("Longest substring in alphabetical order is: " + longest)