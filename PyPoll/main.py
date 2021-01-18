import os
import csv
import locale
import copy

election_results = os.path.join("Resources","election_data.csv")

total_votes = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OtooleyVotes = 0 
votes = []
percentages = []
names = ["Khan", "Correy","Li","O'Tooley"]
vote_Index = []
# candidates = {"Khan":KhanVotes,"Correy":CorreyVotes,"Li":LiVotes,"O'Tooley":OtooleyVotes}

with open(election_results, newline='') as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=',') 
    csv_header = next(csvreader)
    # print(csv_header)

    for row in csvreader:
        if row[2] == 'Khan':
            KhanVotes = KhanVotes+1
            total_votes = total_votes+1
        elif row[2] == 'Correy':
            CorreyVotes = CorreyVotes+1
            total_votes = total_votes+1
        elif row[2] == 'Li':
            LiVotes = LiVotes+1
            total_votes = total_votes+1
        elif row[2] == "O'Tooley":
            OtooleyVotes = OtooleyVotes+1
            total_votes = total_votes+1
    
    votes.append(KhanVotes)
    votes.append(CorreyVotes)
    votes.append(LiVotes)
    votes.append(OtooleyVotes)

    percentages.append((KhanVotes/total_votes)*100)
    percentages.append((CorreyVotes/total_votes)*100)
    percentages.append((LiVotes/total_votes)*100)
    percentages.append((OtooleyVotes/total_votes)*100)

    # print(percentages)

    votes.sort(reverse=True)

    i_Khan = votes.index(KhanVotes)
    i_Correy = votes.index(CorreyVotes)
    i_Li = votes.index(LiVotes)
    i_OTooley = votes.index(OtooleyVotes)

    vote_Index.append(i_Khan)
    vote_Index.append(i_Correy)
    vote_Index.append(i_Li)
    vote_Index.append(i_OTooley)

    election_final = zip(names,percentages,votes,vote_Index)
    election_set = list(election_final)
    # print(election_set[0][2])

    print("```text")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(election_set[0][0]+": {:.3f}% ({:})".format(election_set[0][1], election_set[0][2]))
    print(election_set[1][0]+": {:.3f}% ({:})".format(election_set[1][1], election_set[1][2]))
    print(election_set[2][0]+": {:.3f}% ({:})".format(election_set[2][1], election_set[2][2]))
    print(election_set[3][0]+": {:.3f}% ({:})".format(election_set[3][1], election_set[3][2]))
    print("-------------------------")
    print("Winner: "+ election_set[0][0])
    print("-------------------------")
    print("```")

output_file = os.path.join("analysis","PyPoll_Analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
   
    writer.writerow(["```text"])
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["-------------------------"])
    writer.writerow([election_set[0][0]+": {:.3f}% ({:})".format(election_set[0][1], election_set[0][2])])
    writer.writerow([election_set[1][0]+": {:.3f}% ({:})".format(election_set[1][1], election_set[1][2])])
    writer.writerow([election_set[2][0]+": {:.3f}% ({:})".format(election_set[2][1], election_set[2][2])])
    writer.writerow([election_set[3][0]+": {:.3f}% ({:})".format(election_set[3][1], election_set[3][2])])
    writer.writerow(["-------------------------"])
    writer.writerow(["Winner: "+ election_set[0][0]])
    writer.writerow(["-------------------------"])
    
