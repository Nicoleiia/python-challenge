import csv 
import os

#csv file
with open("Resources/election_data.csv") as file:
    #print(file.read())
    
    csvread = csv.reader(file)
    header = next(csvread)
    print(header)
    
    #Dictionary used for candidate name and vote count.
    poll = {}
    #Sets variable, total votes, to zero for count.
    total_votes = 0
    
    
    #Keeps a total vote count by counting up 1 for each loop 
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
    
    #Empty list for candidates and their vote count
    candidates = []
    num_votes = []
    
    #Dictionary keys and values and dumps them into the lists, 
    #Candidates and num_votes
    for key, value in poll.items():
        candidates.append(key)
        num_votes.append(value)
    
    #Vote percent list
    vote_percent = []
    for n in num_votes:
        vote_percent.append(round(n/total_votes*100, 1))
    
    #Zips candidates, num_votes, vote_percent into tuples
    clean_data = list(zip(candidates, num_votes, vote_percent))
    
    #Winner list to show winners
    winner_list = []
    
    for name in clean_data:
        if max(num_votes) == name[1]:
            winner_list.append(name[0])
    
    #Creates winner_list a string with the first entry
    winner = winner_list[0]
    
    #Runs if there is a tie and puts additional winners into a string separated by commas
    if len(winner_list) > 1:
        for w in range(1, len(winner_list)):
            winner = winner + ", " + winner_list[w]
    
    #Will prints to terminal
    print('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
          '\n-------------------------')
    #Will print using loop of tuples
    for entry in clean_data:
        print(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')')
    print('------------------------- \nWinner: ' + winner + '\n-------------------------')
    
   