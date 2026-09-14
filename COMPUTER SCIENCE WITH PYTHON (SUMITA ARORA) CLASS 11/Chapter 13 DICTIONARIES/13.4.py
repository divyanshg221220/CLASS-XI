#13.4
n=int(input("Enter a number:"))
d={}
for i in range(n):
    name=input("Enter team name:")
    wins=int(input("Enter number of wins:"))
    losses=int(input("Enter number of losses:"))
    d[name]=(wins,losses)
print(d)
while True:
    print("1. Using the dictionary created above, allow the user to enter a team name and print out the team's winning percentage.")
    print("2. Using the dictionary, create a list whose entries are the number of wins of each team.")
    print("3. Using the dictionary, create a list of all those teams that have winning reconds.")
    print("4. EXIT")
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        name=input("Enter team name to find winning percentage:")
        wins,losses=d[name]
        total_games=wins+losses
        print("Winning percentage:",wins/total_games*100)
    elif choice==2:
        l=[]
        for team in d:
            wins,losses=d[team]
            l.append(wins)
        print("Number of wins of each team:",l)
    elif choice==3:
        l=[]
        for team in d:
            wins,losses=d[team]
            if wins>losses:
                l.append(team)
        print("Teams with winning records:",l)
    elif choice==4:
        print("EXITED BY USER")
        break
    print()