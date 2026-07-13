import random

user_score = 0
computer_score = 0
draw_score = 0

while True:
    print("\nWELCOME to Rock Paper Scissor Game\n")
    print("1.ROCK\n2.PAPER\n3.SCISSOR")

    user = (input("Choose one of them(rock,paper,scissor) :- ")).lower() .strip()
      

    choices =['rock','paper','scissor']
    computer= random.choice(choices)
    

    if computer == user :
        print("Game is Draw")
        draw_score += 1
        
    elif computer == "rock" and user == "scissor":
        print("Computer Wins")
        computer_score += 1
        
    elif computer == "scissor" and user == "paper":
        print("Computer Wins")
        computer_score += 1
        
    elif computer == "paper" and user == "rock":
        print("Computer Wins")
        computer_score += 1

    else:
        print("User Wins")
        user_score +=1
        
    while True:    
        user_p = input("\ndo you want to play again (yes/no):- ").lower() .strip()
        
        if user_p  =="yes":
            break
        
        elif user_p  == "no":
            print("thanks for playing! \n\nFINAL SCORE\n")
            print("COMPUTER SCORE =",computer_score)
            print("USER SCORE =",user_score)
            print("DRAW SCORE =",draw_score)
            
            
            if computer_score > user_score:
                print("COMPUTER WINS")
            
            elif computer_score < user_score:
                print("USER WINS")
            
            else:
                print("BOTH HAVE SAME SCORE")
                
            exit()
        
        else:
            print("Please enter only 'yes' or 'no'.")
            
        
        
