# PyPoll Analysis

# importing needed modules
import csv
import os

# connect to the source file and read it
election_path = os.path.join('Resources', 'election_data.csv')

with open(election_path) as election_file:
    election_reader = csv.reader(election_file, delimiter=',' )
    
    # moving next method movving through header
    election_header = next(election_reader)

    # Setting initial variables for for loop
    total_votes = 0
    candidates_unique = []
    candidates_all_records = []

    for row in election_reader:
        #Calculating total number of votes
        total_votes +=1
        
        #create list of all rows so it can be manipulated later
        candidates_all_records.append(row[2])

        #Compiling list of unuque candidates_unique
        if row[2] not in candidates_unique:
            candidates_unique.append(row[2])
        
    
# Calculating number of votes for each candidate    
candidate_0_votes = sum(1 for i in candidates_all_records if i == candidates_unique[0])
candidate_1_votes = sum(1 for i in candidates_all_records if i == candidates_unique[1])
candidate_2_votes = sum(1 for i in candidates_all_records if i == candidates_unique[2])
candidate_3_votes = sum(1 for i in candidates_all_records if i == candidates_unique[3])


# Calculating % of votes for each candidate
candidate_0_percent = "{:.2%}".format(candidate_0_votes/total_votes)
candidate_1_percent = "{:.2%}".format(candidate_1_votes/total_votes)
candidate_2_percent = "{:.2%}".format(candidate_2_votes/total_votes)
candidate_3_percent = "{:.2%}".format(candidate_3_votes/total_votes)

candidates_perecent = [candidate_0_percent, candidate_1_percent, candidate_2_percent, candidate_3_percent]

# combine each candidate with its votes percentage
candidates_and_percent = list(zip(candidates_unique, candidates_perecent))

# determine winner
winner = [i[0] for i in candidates_and_percent if i[1] == max(candidates_perecent)]

print(winner)
   
    



    

    
    
