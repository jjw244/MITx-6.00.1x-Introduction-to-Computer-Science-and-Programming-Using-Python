#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:15:24 2017

course: MITx 6.00.1x: Introduction to Computer Science and Programming Using Python
source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017
"""

"""
Problem Set 2 - Problem 2 - Paying Debt Off in a Year

Instructions:
    
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Problem 2 Test Cases
Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

Test Cases:

	      Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
      

	      Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440
      

	      Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
"""


"""Solution"""
def calculate_balance(balance, annualInterestRate, monthlyPaymentRate):

    totalPaid = 0
    remainingBalance = balance

    for month in range(1,13):
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = round((monthlyPaymentRate * remainingBalance),2)
        totalPaid += minimumMonthlyPayment
        monthlyUpaidBalance = remainingBalance - minimumMonthlyPayment
        remainingBalance = round(monthlyUpaidBalance + (monthlyInterestRate * monthlyUpaidBalance),2)

        print("Month:", month)
        print("Minimum monthly payment:", (minimumMonthlyPayment))
        print("Remaining Balance:", (remainingBalance))

    print("Total paid:", round(totalPaid, 2))
    print("Remaining Balance:", remainingBalance)

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
calculate_balance(balance, annualInterestRate, monthlyPaymentRate)