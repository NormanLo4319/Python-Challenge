#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PyPoll Assignment
# Import the data 
import os
import csv

# Create a variable for counting the votes
total_votes = 0

# Create dictionary to store the summary data
results = {"vote": [0, 0, 0, 0], 
            "percentage": [0, 0, 0, 0]}

# Create a list for candidates
candidate = ["Khan", "Correy", "Li", "O'Tooley"]

#print(os.path.join(".", "Assignment_3", "election_data.csv"))
pypoll = os.path.join(".", "Assignment_3", "election_data.csv")

with open(pypoll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)
    header = next(csvreader)
    #for row in csvreader:
    #    print(row)

# Create loop to check the total number of voters by row
    for row in csvreader:
        total_votes += 1
#print(total_votes)
        if row[2] == "Khan":
            results["vote"][0] += 1
        elif row[2] == "Correy":
            results["vote"][1] += 1
        elif row[2] == "Li":
            results["vote"][2] += 1
        else:
            results["vote"][3] += 1

#print(results["vote"])

for i in range(4):
    results["percentage"][i] = (results["vote"][i] / total_votes) * 100
    results["percentage"][i] = round(results["percentage"][i], 3)
    if results["vote"][i] == max(results["vote"]):
        winner = candidate[i]


#print(max(results["vote"]))
#print(winner)
#print(results["percentage"])


# Create a election poll summary table,
print("Election Results")
print("---------------------------------------")
print(f'Total Votes: {total_votes}')
print("---------------------------------------")
print(f'Khan: {results["percentage"][0]}% ({results["vote"][0]})')
print(f'Correy: {results["percentage"][1]}% ({results["vote"][1]})')
print(f'Li: {results["percentage"][2]}% ({results["vote"][2]})')
print("O'Tooley: " + str(results["percentage"][3]) + "%" + " " + "(" + str(results["vote"][3]) + ")")
print("---------------------------------------")
print("Winner: " + winner)
print("---------------------------------------")

