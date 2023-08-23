print("Welcome To The Voting Center")
nominee1 = input("Enter the nominee 1 name : ")
nominee2 = input("Enter the nominee 2 name : ")
nominee1Votes = 0
nominee2Votes = 0
voterId = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numberOfVoters = len(voterId)
while True:
    if voterId == []:
        print("Voting session is over !!!")
        if nominee1Votes > nominee2Votes:
            percent = (nominee1Votes/numberOfVoters)*100
            print(f"{nominee1} has won the election with {percent} %.")
            break

        elif nominee2Votes > nominee1Votes:
            percent = (nominee2Votes/numberOfVoters)*100
            print(f"{nominee2} has won the election with {percent} %.")
            break

        else:
            print("Both have got equal number of votes !! Heigher authority will decide the final result, Thankyou !!")
            break
    
    voterIdDetection = int(input("Enter your voter id : "))
    if voterIdDetection in voterId:
        print("You are a genuine voter ")
        voterId.remove(voterIdDetection)
        print("______________")
        print(f"To give a vote to {nominee1} Press 1 : ")
        print(f"To give a vote to {nominee2} Press 2 : ")
        print("______________")
        vote = int(input("Enter your precious vote : "))
        if vote == 1:
            nominee1Votes += 1
            print(f"{nominee1}, Thanks you to give me your important vote !! ")
        elif vote == 2:
            nominee2Votes += 1
            print(f"{nominee2}, Thanks you to give me your important vote !! ")
        elif vote > 2:
            print("Check your presed key is it right or wrong !!")
        else:
            print("You are not a genuine voter OR You have already voted ")
    else:
        print("You are not a genuine voter OR You have entered wrong Voter ID , else you already give your precious vote.")
print(" Thanks for giving your valuable time and vote.")