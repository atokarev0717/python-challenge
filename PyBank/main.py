# PyBank Analysis

# importing needed modules
import csv
import os

# Connect to the source file and read it
budget_data_path = './Resources/budget_data.csv'

with open(budget_data_path) as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter=',')

    # using to next method moving through header
    budget_data_header = next(budget_data_reader)
    #Calculating number of months and net total using for loop
    number_of_months = 0
    net_total = 0    
    for row in budget_data_reader:
        number_of_months += 1
        net_total += int(row[1])

# Resetting csv reader to construct list of rows
with open(budget_data_path) as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter=',')
    budget_data_header = next(budget_data_reader)    
    budget_rows = list(budget_data_reader)
print(budget_rows[0][1])
print(number_of_months)
print(net_total)
    
    


