import random

def validate_str(value,options):
    if value in options: return True
    else: return False

def convert_int(value):
    try: return int(value)
    except:
        print("Invaled input!")
        return False
    
def Score(player,computer,rounds):
    if rounds == 0:
        if player > computer: return "Player wins!"
        elif player == computer: return "It's a tie!"
        else: return "Computer wins!"
    print(player,"-",computer)


options = ['rock', 'paper', 'scissors']
rounds = False
p,c=0,0

while rounds == False:
    rounds = input("Enter number of rounds to play: ")
    rounds = convert_int(rounds)

while rounds > 0:
    computer = random.choice(options)
    player = input("Enter rock, paper, or scissors: ").lower()

    if validate_str(player,options) == True:
        print("Computer:", computer," Player:", player)

        if player == computer:
            print("It's a tie!")
        elif player == 'rock' and computer == 'scissors':
            print("You win! Rock crushes scissors.")
            p += 1
        elif player == 'paper' and computer == 'rock':
            print("You win! Paper covers rock.")
            p += 1
        elif player == 'scissors' and computer == 'paper':
            print("You win! Scissors cut paper.")
            p += 1
        else:
            print("You lost! Computer is better.")
            c += 1


        rounds -= 1
        Score(p,c,rounds)

    else:
        print("Invalid input! Please enter rock, paper, or scissors.")

print(Score(p,c,rounds))