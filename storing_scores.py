from window import *
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
    if date != False: matches = previous_scores+[[str(date),str(player),str(computer),str(overall_winner(player,computer))]] #Loads previous scores and appends new score
    else: matches = previous_scores
    #matches.append(previous_scores)
    print(matches)
    print("Items to remove: ",table1.removed_itmes)

    new_remove_str = []

    for match in table1.removed_itmes:
        temp=[]
        for item in match:
            temp.append(str(item))
        new_remove_str.append(temp)
    
    print("New Removales: ",new_remove_str)

    for match in matches:
        if match in new_remove_str:
            print(True)
        else:
            for data in match: scores_record.write(str(data)+',')
            scores_record.write('\n')

    scores_record.close()

    return "Saved!"

def store_settings():
    settings_record = open("settings_record.txt",'w')
    settings_to_store = [music_set.get(),effects_set.get(),music_style_set.get(),volume_set.get()]
    
    for item in settings_to_store: settings_record.write(str(item)+'\n')

    pygame.mixer.music.pause()

def store_score_close():
    store_score(False,0,0)
    store_settings()
    win.destroy()


#store_score('4','3') #Temp test call
#load_scores() #Temp test call
    