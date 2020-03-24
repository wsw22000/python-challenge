import os
import csv
from datetime import date

csvpath = os.path.join("election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    total_votes_cast = 0
    all_named_votes = []
    candidate_list = []
    votes_by_candidate = {}

    for row in csvreader:
        total_votes_cast += 1
        all_named_votes.append(row[2])

    import pandas as pd

    # df = pd.DataFrame({'A':all_named_votes})
    # candidate_list = df['A'].unique()
    
    candidate_list = list(set(all_named_votes))

    votes_for = 0
    winning_vote_count = 0
    winner = ""

    for candidate in candidate_list:
        for vote in all_named_votes: 
            if candidate == vote:       
                votes_for += 1

        votes_by_candidate[candidate] = votes_for       

        if votes_for > winning_vote_count:
            winner = candidate
            winning_vote_count = votes_for
    
        votes_for = 0

print('Election Results')
print('--------------------')
print(f'Total Votes: {total_votes_cast}')
print('--------------------')
for candidate in sorted(votes_by_candidate, key=votes_by_candidate.get, reverse=True):
    print(f'{candidate}: {round(votes_by_candidate[candidate]/total_votes_cast*100,3)}% ({votes_by_candidate[candidate]})')
print('--------------------')
print(f'Winner: {winner}')    
print('--------------------')

output_path = open('election_results.txt', 'w')

output_path.write(f'Election Results\n')
output_path.write(f'--------------------\n')
output_path.write(f'Total Votes: {total_votes_cast}\n')
output_path.write(f'--------------------\n')
for candidate in sorted(votes_by_candidate, key=votes_by_candidate.get, reverse=True):
    output_path.write(f'{candidate}: {round(votes_by_candidate[candidate]/total_votes_cast*100,3)}% ({votes_by_candidate[candidate]})\n')
output_path.write('--------------------\n')
output_path.write(f'Winner {winner}\n')
output_path.write('--------------------\n')