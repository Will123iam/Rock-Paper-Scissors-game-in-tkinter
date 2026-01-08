#Validates imputs

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