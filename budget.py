#!/bin/python

#Insert income amounts here
print "Welcome. Please enter your income per month here."
income1 = int(raw_input())
print "Please enter any extra income here."
income2 = int(raw_input())

total_income = income1 + income2

print total_income

#Insert expenses here
print "Please enter your expenses per month here."
print "Car: "
car = int(raw_input())
print "Home: "
home = int(raw_input())
print "Gas: "
gas = int(raw_input())
print "Utilities: "
utilities = int(raw_input())
print "Groceries: "
groceries = int(raw_input())
print "Insurance: "
insurance = int(raw_input())
print "Entertainment: "
entertainment = int(raw_input())
print "Retirement: "
retirement = int(raw_input())

total_expenses = car + home + gas + utilities + groceries + insurance + entertainment + retirement

print total_expenses
leftover = total_income - total_expenses
print "Your leftover money for the month is: "
print leftover
print "Thank you for using this program."
