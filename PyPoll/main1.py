
# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to track candidate names and vote counts

# Open the CSV file and process it
with open(file_to_load, newline='') as election_data:
    reader = csv.reader(election_data)
    header = next(reader)  # Skip the header row
    
    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        cand_name = row[2]
       # print(". ", end="")

        # Add candidate to dictionary if not already there, and increment vote count
        if cand_name not in candidate_votes:
            candidate_votes[cand_name] = 1
        else:
            candidate_votes[cand_name] += 1

# Winning Candidate and Winning Count Tracker
winner = ""
winner_count=0
for votes in candidate_votes:
    if votes> winner_count:
        winner_count= votes


# Print results to terminal after processing all rows
print("\nElection Results:")
for cand_name, votes in candidate_votes.items():
    #vote_percent = votes/total_votes *100
    vote_percent = round(votes/total_votes *100, 2)
    print(f"{cand_name}:  {vote_percent}% , ({votes})")




# Write results to the output file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for cand_name, votes in candidate_votes.items():
        txt_file.write(f"{cand_name}: {votes} votes\n")
    txt_file.write("-------------------------\n")
