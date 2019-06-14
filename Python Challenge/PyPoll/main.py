import os
import csv

#Import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    #Define the lists/dicts
    voter_count=[]
    candidates=[]
    votes_dict={}
    
    #Append csv columns to lists
    for row in csvreader:
        voter_count.append(row[0])
        candidates.append(row[2])

    #Get count of total votes
    total_votes= len(voter_count)
    
    #Create dictionary of candidates and vote total, sorted in descending value
    for i in candidates:
        if i not in votes_dict:
            votes_dict[i] = 1
        else:
            votes_dict[i] += 1
    sorted_votes_dict=dict(sorted(votes_dict.items(), key=lambda x: x[1], reverse=True))

    #Create candidate list off of sorted dictionary, assign each to a variable
    candidate_list=list(sorted_votes_dict)
    first=candidate_list[0]
    second=candidate_list[1]
    third=candidate_list[2]
    fourth=candidate_list[3]
    
    #Create corresponding votes list off of sorted dictionary, assign each to a variable
    votes_list=list(sorted_votes_dict.values())
    first_votes=(votes_list[0])
    second_votes=votes_list[1]
    third_votes=votes_list[2]
    fourth_votes=votes_list[3]
    
    #Calculate vote percentages and format
    first_vote_percentage=format(first_votes/total_votes*100,'.3f')
    second_vote_percentage=format(second_votes/total_votes*100,'.3f')
    third_vote_percentage=format(third_votes/total_votes*100,'.3f')
    fourth_vote_percentage=format(fourth_votes/total_votes*100,'.3f')



#Print out results to terminal
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

#Print out results to file
txtpath = os.path.join("..", "Resources", "election_results.txt")
with open(txtpath, 'w') as f:
    print("Election Results",file=f)
    print("------------------------------",file=f)
    print(f'Total Votes: {total_votes}',file=f)
    print("------------------------------")
    print(f'{first}: {first_vote_percentage}% ({first_votes})',file=f)
    print(f'{second}: {second_vote_percentage}% ({second_votes})',file=f)
    print(f'{third}: {third_vote_percentage}% ({third_votes})',file=f)
    print(f'{fourth}: {fourth_vote_percentage}% ({fourth_votes})',file=f)
    print("------------------------------",file=f)
    print(f'Winner: {first}',file=f)
    print("------------------------------",file=f)


