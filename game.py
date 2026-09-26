import random

player1_score = 0
player2_score = 0
player3_score = 0
player4_score = 0
players = random.randint(1,6)
attempts = 0

def player1_data():
    global player1_score 
    global players
    global attempts
    if players == 6:
        player1_score+=3
        attempts+=1
        return("You have a perfect roll")
        

    if players == 1:
            player1_score=0
            attempts+=1
            return("you gained no point")
            
        
    if players == 5 or players == 4 or players == 3 or players == 2:
            player1_score+=1
            attempts+=1
            return ("You gained a point")

def player2_data():
    global player2_score
    global players
    global attempts
    if players == 6:
        player2_score+=3
        attempts+=1
        return("You have a perfect roll")
        

    if players == 1:
            player2_score+=0
            attempts+=1
            return("you gained no point")
            
        
    if players == 5 or players == 4 or players == 3 or players == 2:
            player2_score+=1
            attempts+=1
            return ("You gained a point")

def player3_data():
    global player3_score
    global players
    global attempts
    if players == 6:
        player3_score+=3
        attempts+=1
        return("You have a perfect roll")
        

    if players == 1:
            player3_score+=0
            attempts+=1
            return("you gained no point")
            
        
    if players == 5 or players == 4 or players == 3 or players == 2:
            player3_score+=1
            attempts+=1
            return ("You gained a point")

def player4_data():
    global player4_score
    global players
    global attempts
    if players == 6:
        player4_score+=3
        attempts+=1
        return("You have a perfect roll")
        

    if players == 1:
            player4_score+=0
            attempts+=1
            return("you gained no point")
            
        
    if players == 5 or players == 4 or players == 3 or players == 2:
            player4_score+=1
            attempts+=1
            return ("You gained a point")
        
        
        
while True:
    print(f"Player 1 rolled {players}: {player1_data()}, your present score is {player1_score}")
    print(f"Player 2 rolled {players}: {player2_data()}, your present score is {player2_score}")
    print(f"Player 3 rolled {players}: {player3_data()}, your present score is {player3_score}")
    print(f"Player 4 rolled {players}: {player4_data()}, your present score is {player4_score}")

    if attempts%5 == 0:
          break
    




    
       

    