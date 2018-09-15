
import os
import csv

hwfile = os.path.join("election_data.csv")

totalvotes = 0 
CandidateList = []
KhanList = []

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
#create a list of only votes that relate to a certain candidate
        if row[2] == "Khan":
            KhanList.append(row[0])
        print(KhanList)

#The total number of votes each candidate won


#The winner of the election based on popular vote.