# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv") 
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path
# Initialize variables to track the election data

total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts

candidate_votes = {} 

# Winning Candidate and Winning Count Tracker

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)    
    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it

    for row in reader :
        total_votes += 1
        cand_name = row[2]
        print(". ", end="")
    if cand_name not in candidate_votes:
        candidate_votes[cand_name] = 1  # Initialize with the first vote
    else:
        candidate_votes[cand_name] += 1  # Increment vote count
        # Get the candidate's name from the row
    
    #The percentage of votes each candidate won



# Open a text file to save the output


    # Print the total vote count (to terminal)
    
    # Open the CSV file and process it
with open(file_to_load, newline='') as election_data:
    reader = csv.reader(election_data)
    header = next(reader)  # Skip the header row
    
    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        cand_name = row[2]
        print(". ", end="")

        # Add candidate to dictionary if not already there, and increment vote count
if cand_name not in candidate_votes:
            candidate_votes[cand_name] = 1
else:
            candidate_votes[cand_name] += 1
    

# Print results to terminal
print("\nComplete list of Candidates who received votes:")
for cand_name, votes in candidate_votes.items():
    print(f"{cand_name}: {votes} votes")

# Write results to the output file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for cand_name, votes in candidate_votes.items():
        txt_file.write(f"{cand_name}: {votes} votes\n")
    txt_file.write("-------------------------\n")

    # Write the total vote count to the text file

   # with open(file_to_output,'w') as txt_file:
     
        

    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage
        

    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file

  #  with open(file_to_output, "w") as txt_file:
       # txt_file.write("ABCDDD")