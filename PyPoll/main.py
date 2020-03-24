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

    candidate_list = list(set(all_named_votes))

    votes_for = 0
    winning_vote_count = 0
    winner = ""

    for candidate in candidate_list:
        for row in csvreader: 
            if candidate = row[2]        
                votes_for += 1

        votes_by_candidate[candidate] = votes_for       

            if votes_for > winning_vote_count:
                winner = candidate
                winning_vote_count = votes_for
    
        votes_for = 0