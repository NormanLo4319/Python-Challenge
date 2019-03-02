#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment 3 Python Basic
# The assignment has two part, PyBank and PyPool

# Part 1:  PyBank Assignment
# Create Python script that analyzes the records to calculate each of the following:# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Import the data 
import os
import csv

print(os.path.join(".", "Assignment_3", "budget_data.csv"))
pybank = os.path.join(".", "Assignment_3", "budget_data.csv")

with open(pybank, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    print(header)
#   print(csvreader)
#    print("CSV Data")
#    for row in csvreader:
#        print(row)

# Find the total number of months in the data
# Alternate to count number of rows, "print(sum(1 for line in csvfile))""
    months = 0
    profit = 0
    profit_list = []
    profit_change = [867884]
    sum_change = 0
    avg_profit = 0
    rows = 0
    i = 0
    
    for row in csv_reader:
        months += 1
# Find the total amount of profit / losses over the entire period
        profit += float(row[1])
# print(profit)
# print(month)
# List all profit / losses in an array called "profit_list"
        profit_change.append(row[1])
        change = int(profit_change[rows + 1]) - int(profit_change[rows])
        profit_list.append(change)
        
#print(profit_list[0])
#print(profit_list[1])
# Find the greatest increase in profit with date and amount
        max_profit = max(profit_list)
        if profit_list[rows] == max_profit:
            max_date = row[0]
            
# Find the greatest decrease in losses with data and amount
        min_profit = min(profit_list)
        if profit_list[rows] == min_profit:
            min_date = row[0]
# Find sum of changes            
        changes = int(profit_list[rows])
        sum_change += changes        
            
# Move to the next row in profit list
        rows += 1
# print(max_date)
# print(min_date)
# print(max_profit)
# print(min_profit)

# Find the average of the changes in profit / losses 
avg_profit = round(sum_change / (months - 1), 2)
print(avg_profit)

# Create a financial analysis summary table,
print("Financial Analysis")
print("---------------------------------------")
print("Total Months: " + str(months))
print("Average Change: " + "$" + str(avg_profit))
print("Greatest Increase in Profits: " + max_date + " (" + max_profit + ")")
print("Greatest Decrease in Profits: " + min_date + " (" + min_profit + ")")

