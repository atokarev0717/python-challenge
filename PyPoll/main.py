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
        
    
    
candidate_0_votes = sum(1 for i in candidates_all_records if i == candidates_unique[0])
    
print(candidate_0_votes)
print(candidates_all_records[0])
   
    



    

    
    
