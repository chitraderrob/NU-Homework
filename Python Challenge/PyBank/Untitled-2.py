import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")
#Import csv
with open(csvpath, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(reader)
    print(f"CSV Header: {csv_header}")

    # use of next to skip first title row in csv file
    next(reader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    # #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    # for i in range(1,len(revenue)):
    #     rev_change.append(revenue[i] - revenue[i-1])   
    #     avg_rev_change = sum(rev_change)/len(rev_change)

    #     max_rev_change = max(rev_change)

    #     min_rev_change = min(rev_change)

    #     max_rev_change_date = str(date[rev_change.index(max(rev_change))])
    #     min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    # print("Avereage Revenue Change: $", round(avg_rev_change))
    # print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    # print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")"