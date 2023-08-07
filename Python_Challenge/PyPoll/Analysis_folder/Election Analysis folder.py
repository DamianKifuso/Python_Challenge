#import module and csv file

import os
import csv

#File path
filepath = os.path.join("C:/","Users","wambu","Desktop","Python_Challenge","PyPoll","Resources_folder","election_data.csv")

#Open the CSV
with open(filepath, newline='') as csvfile:
    #CSV reader
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the first row (header)
    csv_header = next(csvreader)

    #Listing candidates with number of votes
    candidate_list = [candidate[2] for candidate in csvreader]

#Total votes
total_votes = len(candidate_list)

candidates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

#Listing candidates with the number of the votes
candidates_info = sorted(candidates_info, key=lambda x: x[1], reverse=True)

#Printing the results
print('Election Results')
print('---------------------')
print(f'Total Votes: {total_votes}')
print('---------------------')

for candidate in candidates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print('--------------------')
print(f'Winner: {candidates_info[0][0]}')
print('----------------------')

#Results print to text file
#File path
filepath = os.path.join("C:/","Users","wambu","Desktop","Python_Challenge","PyPoll","Analysis_folder","Poll_Analysis.txt")
with open(filepath, 'w') as text_file:
    print('Election Results', file=text_file)
    print('----------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print('---------------------', file=text_file)

    for candidate in candidates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print('--------------------', file=text_file)
    print(f'Winner: {candidates_info[0][0]}', file=text_file)
    print('----------------------', file=text_file)