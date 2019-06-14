import os
import csv


#Lists
date = []
rev_change = []
profit = []

#Variables
month = 0
opening_profit = 0
profit_change = 0
total_profit = 0

#Open CSV
csvpath = os.path.join("..", "Resources", "budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

# The total number of months included in the dataset
    for row in csv_reader:
        profit.append(float(row[1]))
        date.append(row[0])
    
        print(month)
       
        
# The net total amount of "Profit/Losses" over the entire period        
    total_revenue = sum(profit)
    print(total_revenue)

# # The average of the changes in "Profit/Losses" over the entire period        
#         close_profit = int(row[1])
#         profit_change = close_profit - opening_profit
#         profit_change.append(profit_change)
#         total_profit = total_profit + profit_change
#         opening_profit = close_profit
#         average = int(total_profit/month)

# # The greatest increase in profits (date and amount) over the entire period
#         greatest_increase = max(profit_change)
#         greatest_increase_date = date[profit_change.index(greatest_increase)]

# # The greatest decrease in losses (date and amount) over the entire period        
#         greated_decrease = min(profit_change)
#         greated_decrease_date = date[profit_change.index(greated_decrease)]

# # Print 
#     print("Financial Analysis")
#     print("----------------------------")
#     print(f"Total Monts: {month}")
#     print(f"Total: ${total_profit}")
#     print(f"Average Change: ${profit_change}")
#     print(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}")
#     print(f"Greatest Decrease in Profits: {greated_decrease_date} {greated_decrease}")


# #Export
# analysis = os.path.join('..', 'Resources', 'analysis.txt')
# with open(analysis, 'w') as text:
#     analysis.write("Financial Analysis")
#     analysis.write("----------------------------")
#     analysis.write(f"Total Monts: {month}")
#     analysis.write(f"Total: ${total_profit}")
#     analysis.write(f"Average Change: ${profit_change}")
#     analysis.write(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}")
#     analysis.write(f"Greatest Decrease in Profits: {greated_decrease_date} {greated_decrease}")