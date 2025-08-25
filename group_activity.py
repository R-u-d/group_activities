# Waqar - Rock Paper Scissors
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "scissors" and p2 == "paper") or \
         (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    
print(rps("scissors", "paper"))   # "Player 1 won!"
print(rps("scissors", "rock"))    # "Player 2 won!"
print(rps("paper", "paper"))      # "Draw!"

# Rud - Convert a Number to a String!
# Umi - Counting sheep