#14.5
players=[(103,"Ritika",3001),(104,"John",2819),(101,"Razia",3451),(105,"Tarandeep",2971)]
n=len(players)
for i in range(n-1):
    for j in range(n-1-i):
        if players[j][2]<players[j+1][2]:
            players[j],players[j+1]=players[j+1],players[j]
print(players)