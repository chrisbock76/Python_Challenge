import os
import csv

PyPoll_csv = os.path.join("..", "Resources", "election_data.csv")

#define arrays/variables
total = 0
candidates = []
Khan = []
Li = []
Correy = []

# Open and read csv
with open(PyPoll_csv, newline="", encoding= 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvfile)

    # Create candidate array and determine total votes
    for row in csvreader:
        candidates.append(row[2])
        total_votes = len(candidates)

    #iterate through candidates list and determine votes per candidate
    #for name in candidates:
        #if name == "Khan":
            #Khan.append(name)
            #Votes_Khan = len(Khan)
        #print(Votes_Khan)

# count element 'Khan', 'Li', 'Correy'
Votes_Khan = candidates.count('Khan')
Votes_Li = candidates.count('Li')
Votes_Correy = candidates.count('Correy')
Votes_OTooley = candidates.count("O'Tooley")

Percent_Khan = round(Votes_Khan / total_votes *100, 2)
Percent_Li = round(Votes_Li / total_votes *100, 2)
Percent_Correy = round(Votes_Correy / total_votes *100, 2)
Percent_OTooley = round(Votes_OTooley / total_votes *100, 2)

print(total_votes)
print(Votes_Khan)
print(Votes_Li)
print(Votes_Correy)
print(Votes_OTooley)
print(Percent_Khan)
print(Percent_Li)
print(Percent_Correy)
print(Percent_OTooley)