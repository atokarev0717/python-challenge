# PyBank Analysis

# importing needed modules
import csv
import os

# Connect to the source file and read it
budget_data_path = './Resources/budget_data.csv'

rows = []
with open(budget_data_path) as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter=',')

    # using next method to move through header
    budget_data_header = next(budget_data_reader)
    #Calculating number of months and net total using for loop
    number_of_months = 0
    net_total = 0    
    for row in budget_data_reader:
        number_of_months += 1
        net_total += int(row[1])
        #Constructing list of rows to be able to access all values later
        rows.append(row)

print(net_total)
print(number_of_months)
pl_start = rows[0][1]
pl_end = rows[number_of_months-1][1]
print(pl_start)
print(pl_end)




    
    


