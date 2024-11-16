# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources","budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
monthly_change = 0
profit_loss_changes = [] # list
previous_profit_loss = None
greatest_increase = ("", 0)  # Tuple
greatest_decrease = ("", 0)
    
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:
        # Track the total months
        total_months += 1   
        # Track the net total
        profit_loss = int(row[1])  # Convert profit/loss to integer
        total_net += profit_loss  
        
        # Track the changes in profit/loss
        if previous_profit_loss is not None:
            monthly_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(monthly_change)
      
            # Check for greatest decrease in Profits
            if monthly_change > greatest_increase[1]:
                greatest_increase = (row[0], monthly_change)
            if monthly_change < greatest_decrease[1]:
                greatest_decrease = (row[0], monthly_change) 
                       
            #Update previous profit/loss
        previous_profit_loss = profit_loss
            
 # Calculate average change
    average_change = sum(profit_loss_changes) / len(profit_loss_changes) if profit_loss_changes else 0
    average_change = round(average_change,2)
# Print the output
print("Financial Analysis")
print(f"Total month:{total_months}")
print(f"Total:{total_net}")
print(f"Average:${average_change}")
print(f"Greatest increase in Profits:{greatest_increase}")
print(f"Greatest decrease in Profits:{greatest_decrease}")

# Write the results to a text file

with open(file_to_output,'w') as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: {total_net}\n")
    txt_file.write(f"Average Change: {average_change}\n")
    txt_file.write(f"Greatest increase in Profits: {greatest_increase}\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease}\n")
    
