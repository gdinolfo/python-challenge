import os
import csv

bankCSV = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
months = []
profit = []
change = []
date = []
#calculate lists
with open(bankCSV, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    total = 0
    for row in csvreader:
        total += int(row[1])
        months.append(row[0])
        profit.append(float(row[1]))
        date.append(row[0])
       

print('Financial Analysis')
print('--------------------')
print('Total Months:', len(months))
print('Total: $', total)
#calculate changes
for num in range(1,len(profit)):
    change.append(profit[num] - profit[num-1])   
    profit_change = sum(change)/len(change)

    max_profit_diff = max(change)
    min_profit_diff = min(change)
    
    max_profit_diff_date = str(date[change.index(max(change))])
    min_profit_diff_date = str(date[change.index(min(change))])

print("Average Change: $", round(profit_change,2))
print("Greatest Increase in Profit:", max_profit_diff_date,"($", round(max_profit_diff),")")
print("Greatest Decrease in Profit:", min_profit_diff_date,"($", round(min_profit_diff),")")