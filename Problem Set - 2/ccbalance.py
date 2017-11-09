#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 08:10:32 2017

@author: newpooter
"""
def ccbalance(balance, annualInterestRate, monthlyPaymentRate):
   """
   balance - the outstanding balance on the credit card
   annualInterestRate - annual interest rate as a decimal
   monthlyPaymentRate - minimum monthly payment rate as a decimal
   """
   month = 0
   while month < 12:
      balance += (balance*(annualInterestRate/12) - (monthlyPaymentRate*balance))
      month += 1
   print ("Month " + str(month) + " Remaining balance: " + str(round(balance, 2)))

#ccbalance(42, 0.2, 0.04)
ccbalance(484, 0.2, 0.04)