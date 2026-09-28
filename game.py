import random

player1_score = 0
player2_score = 0
player3_score = 0
player4_score = 0

attempts = 0

def player1_data():
    global player1_score 
    global player1_roll
    global attempts
    if player1_roll == 6:
        player1_score+=3
        attempts+=1
        return("You have a perfect roll")
        

    if player1_roll == 1:
            player1_score+=0
            attempts+=1
            return("you gained no point")
            
        
    if player1_roll == 5 or player1_roll == 4 or player1_roll == 3 or player1_roll == 2:
            player1_score+=1
            attempts+=1
            return ("You gained a point")

def player2_data():
    global player2_score
    global player2_roll
    global attempts
    if player2_roll == 6:
        player2_score+=3
        attempts+=1
        return("You have a perfect roll")
        

    if player2_roll == 1:
            player2_score+=0
            attempts+=1
            return("you gained no point")
            
        
    if player2_roll == 5 or player2_roll == 4 or player2_roll == 3 or player2_roll == 2:
            player2_score+=1
            attempts+=1
            return ("You gained a point")

def player3_data():
    global player3_score
    global player3_roll
    global attempts
    if player3_roll == 6:
        player3_score+=3
        attempts+=1
        return("You have a perfect roll")
        

    if player3_roll == 1:
            player3_score+=0
            attempts+=1
            return("you gained no point")
            
        
    if player3_roll == 5 or player3_roll == 4 or player3_roll == 3 or player3_roll == 2:
            player3_score+=1
            attempts+=1
            return ("You gained a point")

def player4_data():
    global player4_score
    global player4_roll
    global attempts
    if player4_roll == 6:
        player4_score+=3
        attempts+=1
        return("You have a perfect roll")
        

    if player4_roll == 1:
            player4_score+=0
            attempts+=1
            return("you gained no point")
            
        
    if player4_roll == 5 or player4_roll == 4 or player4_roll == 3 or player4_roll == 2:
            player4_score+=1
            attempts+=1
            return ("You gained a point")
        
        
        
while True:
    player1_roll = random.randint(1,6)
    player2_roll = random.randint(1,6)
    player3_roll = random.randint(1,6)
    player4_roll = random.randint(1,6)
    print(f"Player 1 rolled: {player1_roll} {player1_data()}, your present score is {player1_score}")
    print(f"Player 2 rolled: {player2_roll} {player2_data()}, your present score is {player2_score}")
    print(f"Player 3 rolled: {player3_roll} {player3_data()}, your present score is {player3_score}")
    print(f"Player 4 rolled: {player4_roll} {player4_data()}, your present score is {player4_score}")

    if attempts%5 == 0:
          break
    




    
       

    