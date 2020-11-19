# PyBank Analysis

# importing needed modules
import csv
import os

# Connect to the source file and read it
budget_data_path = 'Resources/budget_data.csv'

# creating empty list to hold all rows while executing for loop
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
        
#Alternative method to calculate change
pl_change = [int(rows[i+1][1]) - int(rows[i][1]) for i in range(len(rows)-1)]
print(min(pl_change))
print(max(pl_change))

# Calculating Average Change
pl_start = int(rows[0][1])
pl_end = int(rows[number_of_months-1][1])
ave_pl_change = float((pl_end - pl_start)/(number_of_months-1))

# print(f'Financial Analysis')
# print('-' * 50)
# print(
# f'Total Months: {number_of_months}\n'
# f'Total: ${net_total}\n'
# f'Average Change: ${ave_pl_change:.2f}\n'
# f'Greatest Increase in Profits: '
# f'Greatest Decrease in Profits: '
# )





    
    


