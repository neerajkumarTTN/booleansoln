game=int(input("Enter the number of game you want plays: "))
playerA_score=0
playerB_score=0
for game in range(0,game):
    playerA=input("PlayerA enter yours choice: ")
    playerB=input("PlayerB enter yours choice: ")
    if playerA==playerB:
        print("DRAW")
    elif playerA=="R":
        if playerB=="S":
            print("A WINS")
            playerA_score+=1
        elif playerB=="P":
            print("B WINS")
            playerB_score+=1
    elif playerA=="P":
        if playerB=="R":
            print("A WINS")
            playerA_score+=1
        elif playerB=="S":
            print("B WINS")
            playerB_score+=1
    elif playerA=="S":
        if playerB=="P":
            print("A WINS")
            playerA_score+=1
        elif playerB=="R":
            print("B WINS")
            playerB_score+=1
    else:
        print("Enter wright choice")

if playerA_score ==playerB_score:
    print("Tournament Draw")
elif playerA_score > playerB_score:
    print("A WINS TOURNAMENT")
else:
    print("B WINS TOURNAMENT")