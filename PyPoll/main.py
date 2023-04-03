# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources","election_data.csv")
# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    row_count = 0
    candidate_list = []
    total_votes = 0
    percent_votes = 0.0
    candidate_dict = {}
    value = 0
        
    # Read the header row first 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        #Total No of Votes cast
        row_count += 1
        
        #A complete list of candidates who received votes and 
        #Calculate The total number of votes each candidate won   
        candidate_name = row[2]
        if candidate_name not in candidate_dict.keys():
            total_votes = 0
            total_votes += 1
            candidate_dict[candidate_name] = total_votes
        else:
            value = candidate_dict.get(candidate_name)
            total_votes = value + 1
            candidate_dict[candidate_name] = total_votes

# Specify the file to write to
output_path = os.path.join("analysis","Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtwriter:

    max_votes = 0
    max_name = ""
    
    # Write the first line
    txtwriter.write('Election Results\n')
    print('Election Results')

    # Write the second line
    txtwriter.write('---------------------------\n')
    print('---------------------------')
    
    # Write the Total Votes
    txtwriter.write('Total Votes: ' + str(row_count) + '\n')
    print(f"Total Votes: {row_count}")
    
    # Write the next line
    txtwriter.write('---------------------------\n')
    print('---------------------------')
    #Write and calculate The percentage of votes each candidate won
    for key in candidate_dict:
        votes = candidate_dict.get(key)
        if votes > max_votes:
            max_votes = votes
            max_name = key

        #The percentage of votes each candidate won
        percent_votes = round((candidate_dict.get(key) / row_count * 100) , 3 )

         # Write the The percentage of votes each candidate won
        txtwriter.write( key + ': '+ str(percent_votes) + '%' +' (' + str(votes) + ')\n')
        print(f" {key} :{percent_votes}% ({votes})")
    
    # Write the next line
    txtwriter.write('---------------------------\n')
    print('---------------------------')
    # Write the Winner's Name
    txtwriter.write( 'Winner: '+ max_name + '\n')
    print(f"Winner: {max_name}")
    # Write the next line
    txtwriter.write('---------------------------\n')
    print('---------------------------')
    