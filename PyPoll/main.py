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
    candidates = []

    for row in election_reader:
        #Calculating total number of votes
        total_votes +=1

        #Compiling list of unuque candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        
    
    
    
    
    print(candidates)



    

    
    
