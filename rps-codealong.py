# welcome players and giving instructions
print("Welcome Players 1 and 2\n When asked for your choice please enter 'r', 'p', or 's'")
# print("When asked for your choice please enter 'r', 'p', or 's'")
# getting players input
playerOneInput = input("player one select: r, p or s; ")
playerTwoInput = input("player two select: r, p or s; ")

print("player one input: " + playerOneInput + "\n" + "player two input: " + playerTwoInput)
# compare player input to determine result. Either player1 wins, or player2 wins, or a tie
if playerOneInput == "s":
    if playerTwoInput == "s":
        print("its a tie!")
    if playerTwoInput == "r":
        print("player two wins!")
    if playerTwoInput == "p":
        print("play one wins!")

