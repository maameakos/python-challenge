# Author Mina Agyen
import csv

# Read election data from CSV file
with open('Resources/election_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    total_num_votes = 0
    candidate_votes = {}

# Analyzing election data to calculate some summary statistics and perform analysis
    for row in reader:
        total_num_votes += 1
        candidate_name = row['Candidate']
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

percentages = {candidate_name: (votes / total_num_votes) * 100 for candidate_name, votes in candidate_votes.items()}

# Finding the winner 
winner = max(candidate_votes, key=candidate_votes.get)

# Print results to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(total_num_votes))
print("-------------------------")
for candidate_name, votes in candidate_votes.items():
    print(candidate_name + ": " + "{:.3f}%".format(percentages[candidate_name]) + " (" + str(votes) + ")")
print("-------------------------")
print("Winner: "+ str(winner))
print("-------------------------")

# Writing results to a text file
with open('analysis/analysis.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-----------------------------------\n")
    output_file.write("Total Votes: "+ str(total_num_votes) +"\n")
    output_file.write("-------------------------\n")
    for candidate_name, votes in candidate_votes.items():
        output_file.write(candidate_name + ": " + "{:.3f}%".format(percentages[candidate_name]) + " (" + str(votes) + ")\n")
    output_file.write("-------------------------\n")
    output_file.write("Winner: "+ str(winner) +"\n")
    output_file.write("-------------------------\n")
