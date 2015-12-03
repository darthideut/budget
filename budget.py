#!/bin/python

budget_menu = 0
budget_income = []
budget_expense =[]
while budget_menu != 7:
	print "--------------------------"
	print "1. Add Income"
	print "2. Remove Income"
	print "3. Add Expenses"
	print "4. Remove Expenses"
	print "5. Totals"
	print "6. Save Report"
	print "7. Exit"
	budget_menu = input("Pick an item from the menu: ")
	
	if budget_menu == 1:
		print "Please name this source of this income."
		inc_name = raw_input()
		print "Please enter the amount of this income."
		inc_amount =  float(raw_input())
		budget_income.append((inc_name, inc_amount))

	elif budget_menu == 2:
		for index in range(1, ((len(budget_income)) + 1)):
			(inc_name, inc_amount) = budget_income[index - 1]
			print str(index) + ": " + inc_name + " (" + str(inc_amount) + ")"
		print "Which one would you like to remove?"
		del_index = int(raw_input())
                if (del_index <= len(budget_income)) and (del_index >= 1):
                        budget_income.pop(del_index - 1)
				
	elif budget_menu == 3:
		print "Please name this source of this expense."
		exp_name = raw_input()
		print "Please enter the amount of this expense."
		exp_amount =  float(raw_input())
		budget_expense.append((exp_name, exp_amount))

	elif budget_menu == 4:
		for index in range(1, ((len(budget_expense)) + 1)):
			(exp_name, exp_amount) = budget_expense[index - 1]
			print str(index) + ": " + exp_name + " (" + str(exp_amount) + ")"
		print "Which one would you like to remove?"
		del_index = int(raw_input())
		if (del_index <= len(budget_expense)) and (del_index >= 1):
                        budget_expense.pop(del_index - 1)

	elif budget_menu == 5:
                sum_inc = 0.0
                sum_exp = 0.0
                sum_leftover = 0.0
                for (inc_name, inc_amount) in budget_income:
                        sum_inc = inc_amount + sum_inc
                for (exp_name, exp_amount) in budget_expense:
                        sum_exp = exp_amount + sum_exp
                sum_leftover = sum_inc - sum_exp
                print "The total amount of income is: " + str(sum_inc)
                print "The total amount of expenses is: " + str(sum_exp)
                print "The total amount leftover is: " + str(sum_leftover)

        elif budget_menu == 6:
                filename = raw_input("File name to save: ")
                out_file = open(filename, "w")
                sum_inc = 0.0
                sum_exp = 0.0
                sum_leftover = 0.0
                out_file.write("Budget Report" + "\n" + "INCOME:" + "\n")
                for (inc_name, inc_amount) in budget_income:
                        sum_inc = inc_amount + sum_inc
                        out_file.write( inc_name + ": " + str(inc_amount) + "\n")
                out_file.write("EXPENSES:" + "\n")
                for (exp_name, exp_amount) in budget_expense:
                        sum_exp = exp_amount + sum_exp
                        out_file.write( exp_name + ": " + str(exp_amount) + "\n")
                sum_leftover = sum_inc - sum_exp
                out_file.write("TOTALS:" + "\n")
                out_file.write("The total amount of income is: " + str(sum_inc) + "\n")
                out_file.write("The total amount of expenses is: " + str(sum_exp) + "\n")
                out_file.write("The total amount leftover is: " + str(sum_leftover))
                out_file.close()         
                
