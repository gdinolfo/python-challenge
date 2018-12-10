import os
import csv
from collections import Counter

pollCSV = os.path.join('Resources', 'election_data.csv')

# Lists to store data
votes = []
candidate = []

with open(pollCSV, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        votes.append(row[0])
                
print('Election Results')
print('--------------------')
print('Total Votes:', len(votes))
print( '-' * 20)

#find Candidate's votes
with open(pollCSV, 'r',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        candidate.append(row[2])
        vote_count = Counter(candidate)
    for key,val in vote_count.items():
        print(key, round(val / (len(votes)) * 100, 2),'%', '(',val,')')

print( '-' * 20)

#find winner
counter = {}
maxItemCount = 0
for item in candidate:
    try:
        counter[item]
        counter[item] += 1
    except KeyError:
        counter[item] = 1

    if counter[item] > maxItemCount:
        maxItemCount = counter[item]
        mostPopularItem = item

print('Winner:', mostPopularItem)