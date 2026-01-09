#Storing and loading the latest scores

def overall_winner(player,computer):
    if player > computer: return "Player"
    elif player == computer: return "Tie"
    else: return "Computer"

def load_scores():
    scores_record = open("scores_record.txt",'r')
    temp=""
    user=[]
    scores=[] #Prevents dublicats when loading

    #Re-using old code from a different project here
    for line in scores_record: #Iterates over every line in file
        for ch in line: #Iterates over every charter in line in file
            if ch != ",": #Checks for ',' in that line
                temp+=ch #Addes that character to temp if not ','
            elif ch == ",":
                if temp[0:1] == "\n": #detects / removes \n from temp if its there
                    temp=temp[1:len(temp)]
                
                user.append(temp)
                temp=""

        if user != []:
            scores.append(user) #Appeneds the user profile aquired from the line
            user=[] #Resets user list ready for next line

    print(scores)

    scores_record.close()

    return scores

def store_score(date,player,computer):
    previous_scores = load_scores()
    scores_record = open("scores_record.txt",'w')
    matches = previous_scores+[[str(date),str(player),str(computer),str(overall_winner(player,computer))]] #Loads previous scores and appends new score
    #matches.append(previous_scores)
    print(matches)

    for match in matches:
        for data in match: scores_record.write(str(data)+',')
        scores_record.write('\n')

    scores_record.close()

    return "Saved!"


#store_score('4','3') #Temp test call
#load_scores() #Temp test call
    