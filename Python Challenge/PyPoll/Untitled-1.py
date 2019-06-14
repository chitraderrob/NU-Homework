import os
import csv
import collections

csvpath = os.path.join("..", "Resources", "election_data.csv")
#Import csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #Define the lists
    voter_count=[]
    candidates=[]
    dict={}
    

    for row in csvreader:
        voter_count.append(row[0])
        candidates.append(row[2])

    total_votes= len(voter_count)
    print(total_votes)

    # khan_votes=candidates.count("Khan")
    # li_votes=candidates.count("Li")
    # correy_votes=candidates.count("Correy")
    # otooley_votes=candidates.count("O'Tooley")
    # print(khan_votes)
    # print(li_votes)
    # print(correy_votes)
    # print(otooley_votes)

    

    # counter=collections.Counter(candidates)
    # print(counter.most_common)
    # # Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
    # print(counter.values())
    # # [4, 4, 2, 1, 2]
    # print(counter.keys())
    # # [1, 2, 3, 4, 5]
    # print(counter.most_common(3))
    # # [(1, 4), (2, 4), (3, 2)]
    counter=0

    for i in candidates:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    sorted(dict.values())
    print(dict)
    


    print(list(dict[1]))