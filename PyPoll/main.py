
import os
import csv

hwfile = os.path.join("election_data.csv")

totalvotes = 0 
CandidateList = []

with open(hwfile, newline="") as ElectionData:
    csvreader = csv.reader(ElectionData, delimiter=",")


#The total number of votes cast
    header = next(csvreader)
    for row in csvreader:
        totalvotes = totalvotes + 1
        
#A complete list of candidates who received votes
        
        if row[2] not in CandidateList:
            CandidateList.append(row[2])
            
print(CandidateList)

#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.