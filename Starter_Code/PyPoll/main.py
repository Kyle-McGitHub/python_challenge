
import csv

#Pull the data
election_data = r"C:\Users\Kyle_McDaniel_Python\Desktop\Columbia_Analytics_Bootcamp\python_challenge\starter_code\pypoll\resources\election_data.csv"
results = r"C:\Users\Kyle_McDaniel_Python\Desktop\Columbia_Analytics_Bootcamp\python_challenge\starter_code\pypoll\results.txt"

#Ballot_id = 0
#County = 0
#Candidate = 0
election_dataset = []

with open(election_data, "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        election_dataset.append(row)

#for row in election_dataset[:5]:
    #print(row)

ballot_ids = set()
for row in election_dataset:
    ballot_ids.add(row['Ballot ID'])

count_ballot_ids = len(ballot_ids)

count_charles = 0
count_diana = 0
count_raymon = 0

for row in election_dataset:
    if row['Candidate'] == 'Charles Casper Stockham':
        count_charles += 1
    if row['Candidate'] == 'Diana DeGette':
        count_diana += 1
    if row['Candidate'] == 'Raymon Anthony Doane':
        count_raymon += 1

percent_charles = (count_charles/count_ballot_ids)*100
percent_diana = (count_diana/count_ballot_ids)*100
percent_raymon = (count_raymon/count_ballot_ids)*100

candidates = {"Charles Casper Stockham": percent_charles,
              "Diana DeGette": percent_diana,
              "Raymon Anthony Doane": percent_raymon
              }
f_percent_charles = f"{percent_charles:.3f}"
f_percent_diana = f"{percent_diana:.3f}"
f_percent_raymon = f"{percent_raymon:.3f}"

winner = max(candidates, key=candidates.get)

print("Election Results")
print("Total Votes:", count_ballot_ids)
print("Charles Casper Stockham:", f_percent_charles, '%', '(', count_charles, ')')
print("Diana DeGette:", f_percent_diana, '%', '(', count_diana, ')')
print("Raymon Anthony Doane:", f_percent_raymon,'%','(',count_raymon,')')
print("Winner:", winner)

with open(results, 'w') as file:
    file.write(f"Election Results\n")
    file.write(f"Total Votes: {count_ballot_ids}\n")
    file.write(f"Charles Casper Stockham: {f_percent_charles}% ({count_charles})\n")
    file.write(f"Diana DeGette: {f_percent_diana}% ({count_diana})\n")
    file.write(f"Raymon Anthony Doane: {f_percent_raymon}% ({count_raymon})\n")
    file.write(f"Winner: {winner}\n")

print("Poll results have been written to results.txt!")