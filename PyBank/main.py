import os
import csv
from datetime import date

csvpath = os.path.join("budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    lines = 0
    profit_loss_total = 0
    previous_profit=0
    greatest_profit_increase = 0
    greatest_profit_decrease = 0
    total_profit_changes = 0

    for row in csvreader:
        lines = lines + 1
        
        profit_loss_total = profit_loss_total + int(row[1])

        if previous_profit == 0:
            previous_profit = int(row[1])

        else:
            profit_change = int(row[1]) - int(previous_profit)
            total_profit_changes = total_profit_changes + profit_change
            average_profit_change = total_profit_changes / (int(lines) -1)
            previous_profit = int(row[1])
                
            if profit_change > greatest_profit_increase:
                greatest_profit_increase = profit_change
                greatest_increase_date = row[0]


            if profit_change < greatest_profit_decrease:
                greatest_profit_decrease = profit_change 
                greatest_decrease_date = row[0]
                    
    print('Financial Analysis')
    print('-----------------------------------------------------------')
    print(f'Total Months: {lines}')
    print(f'The total Profits/Losses: {profit_loss_total}')
    print(f'Greatest Increase in Profits: {greatest_profit_increase} on {greatest_increase_date}')
    print(f'Greatest Decrease in Profits: {greatest_profit_decrease} on {greatest_decrease_date}')





