# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. Find the percentage of votes each candidate won
#4. Find the total number of votes each candidate won
#5. The winner of the election based on popular vote

#Add our dependencies.
import csv
#Assign a variable to load the file from a path
file_to_load = 'Resources/election_results.csv'
#Assign a variable to save the file to a path
file_to_save = 'Analysis/election_analysis.txt'

# Assign a variable for Total Votes equal to 0
total_votes = 0
# Assign an empty list for different candidates.
candidate_options = []
# Assign an empty dictionary for candidate votes.
candidate_votes = {}
# Determine the winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform and read analysis data.
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Iterate each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        # Print the candidates name from the row and append the candidate to the list
        candidate_name = row[2]
       
        if candidate_name not in candidate_options:
            #Add it to the list 
            candidate_options.append(candidate_name)
            # Begin tracking that candidates vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidates count.    
        candidate_votes[candidate_name] += 1

# Use the with statement to open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by LOOPING through the counts
    # 1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print candidates name, vote count, and % of votes to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine the winning candidate and winning count tracker
        # 1. Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. IF true, then set winning count = votes and winning % = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set winning candidate = the candidates name
            winning_candidate = candidate_name

    # Print candidates name, vote count, and % of votes to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary, end="")
    txt_file.write(winning_candidate_summary)
        
    # Close the file.
    election_data.close()


    # # Use the with statement to open the file as a text file
    #with open(file_to_save, "w") as txt_file:
        #   #Save final vote count to txt file
        #  txt_file.write(election_results)
