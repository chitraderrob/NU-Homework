import os
import csv
import sys

# stdoutOrigin=sys.stdout 
# sys.stdout = open("log.txt", "w")

csvpath = os.path.join("..", "Resources", "budget_data.csv")
#Import csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #Define the lists
    date=[]
    pl=[]
    pl_change=[]

    #Get Total Months
    for row in csvreader:
        date.append(row[0])
        pl.append(float(row[1]))
    
    total_months=len(date)

    #Get Total PL
    total_pl=sum(pl)

    #Get Average PL Change
    for i in range(1,len(pl)):
        pl_change.append(pl[i]-pl[i-1])
        avg_pl_change=sum(pl_change)/len(pl_change)

    #Get Max and Min PL
    max_pl=max(pl_change)
    min_pl=min(pl_change)

    #Get Dates for PL Changes
    max_pl_date =str(date[pl_change.index(max_pl)+1])
    min_pl_date=str(date[pl_change.index(min_pl)+1])

#Print out results to terminal
print("Financial Analysis")
print("---------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: {int(total_pl)}')
print(f'Average Change: ${round(avg_pl_change,2)}')
print(f'Greatest Increase in Profits: {max_pl_date} (${int(max_pl)})')
print(f'Greatest Decrease in Profits: {min_pl_date} (${int(min_pl)})')


#Print out results to file
txtpath = os.path.join("..", "Resources", "financial_analysis.txt")
with open(txtpath, 'w') as f:
    print("Financial Analysis",file=f)
    print("---------------------------------",file=f)
    print(f'Total Months: {total_months}',file=f)
    print(f'Total: {int(total_pl)}',file=f)
    print(f'Average Change: ${round(avg_pl_change,2)}',file=f)
    print(f'Greatest Increase in Profits: {max_pl_date} (${int(max_pl)})',file=f)
    print(f'Greatest Decrease in Profits: {min_pl_date} (${int(min_pl)})',file=f)


#Print results to text file
# sys.stdout.close()
# sys.stdout=stdoutOrigin