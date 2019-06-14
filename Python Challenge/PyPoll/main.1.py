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
    votes_dict={}
    

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
        if i not in votes_dict:
            votes_dict[i] = 1
        else:
            votes_dict[i] += 1
    sorted_votes_dict=dict(sorted(votes_dict.items(), key=lambda x: x[1], reverse=True))

    print(sorted_votes_dict)

    # print(list(votes_dict)[0])
    candidate_list=list(sorted_votes_dict)
    first=candidate_list[0]
    second=candidate_list[1]
    third=candidate_list[2]
    fourth=candidate_list[3]
    print(candidate_list)
    # # print(dict.values())
    # # print(dict.keys())
    votes_list=list(sorted_votes_dict.values())
    print(votes_list)
    first_votes=(votes_list[0])
    second_votes=votes_list[1]
    third_votes=votes_list[2]
    fourth_votes=votes_list[3]
    
    
    first_vote_percentage=format(first_votes/total_votes*100,'.3f')
    second_vote_percentage=format(second_votes/total_votes*100,'.3f')
    third_vote_percentage=format(third_votes/total_votes*100,'.3f')
    fourth_vote_percentage=format(fourth_votes/total_votes*100,'.3f')
    print(first_vote_percentage)

print("Election Results")
print("------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------")
print(f'{first}: {first_vote_percentage}% ({first_votes})')
print(f'{second}: {second_vote_percentage}% ({second_votes})')
print(f'{third}: {third_vote_percentage}% ({third_votes})')
print(f'{fourth}: {fourth_vote_percentage}% ({fourth_votes})')
print("------------------------------")
print(f'Winner: {first}')
print("------------------------------")



