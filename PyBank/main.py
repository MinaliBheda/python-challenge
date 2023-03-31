# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("/Users/minali.pinto/Desktop/Homework/python-challenge/PyBank/Resources","budget_data.csv")

total_profitloss = 0
row_count = 0
pnlChange = 0.0
mylist = []
mydate = []
mylist_row = 0
pnl_average = 0.0

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        #Total profit and loss
        total_profitloss = total_profitloss + int(row[1])
        
        #find number of total months without header
        row_count+=1
        
        #Calculate Profit/Losses change over the entire period
        if row_count == 1:
            prevrow = int(row[1])
            
        else:                       
            nextrow = int(row[1])
            date = row[0]
            pnlChange = nextrow - prevrow
            mylist.append( pnlChange)
            mydate.append(row[0])
            mylist_row += 1
            prevrow = nextrow
    

#Calculate the Average of Profit/Loses Changes and Round the average to two digits
pnl_average = round((sum(mylist)/len(mylist)),2)

#Calculate the Greatest Increase Profit/Loses and the Date
max_increase = max(mylist)
index = mylist.index(max_increase)
max_date = mydate[index]

#Calculate the Greatest Decrease Profit/Loses and the Date
max_decrease = min(mylist)
index = mylist.index(max_decrease)
min_date = mydate[index]

# Specify the file to write to
output_path = os.path.join("/Users/minali.pinto/Desktop/Homework/python-challenge/PyBank/analysis","Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtwriter:


    # Write the first line
    txtwriter.write('Financial Analysis\n')

    # Write the second line
    txtwriter.write('---------------------------\n')

    # Write the Total Months
    txtwriter.write('Total Months:' + str(row_count) + '\n')

    # Write the Total
    txtwriter.write('Total: $' + str(total_profitloss) + '\n')

    # Write the Average Change
    txtwriter.write('Average Change: $' + str(pnl_average) + '\n')

    # Write the Greatest Increase in Profits
    txtwriter.write('Greatest Increase in Profits: ' + max_date + ' ($'+ str(max_increase) + ')' + '\n')

    # Write the Greatest Decrease in Profits
    txtwriter.write('Greatest Decrease in Profits: ' + min_date + ' ($'+ str(max_decrease) + ')' + '\n')


