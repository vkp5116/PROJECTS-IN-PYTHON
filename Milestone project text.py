# TIC TAC TOE ...

# creating the display function and making the tictac toe board

def display(board):
    
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("------")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("------")
    print(board[6]+"|"+board[7]+"|"+board[8])
    
    return board
    

# function for creating tic tac toe board wworks successfully

# Creating the input function for X or O 
def user():
    player_1 = input("What is player 1 going to choose : ")
    
    if player_1 == "X":
        player_2 = "O"
        print("Player_2 choses O")
    else:
        player_2 = "X"
        print("Player_2 choses X")
    return (player_1,player_2)
# first input function running successfully 

def game():
    
    test_board = [" "," "," "," "," "," "," "," "," "]
    i = 0
    while i < 9:
        move_1 = int(input("player_1 turn:"))
        y = test_board
        y[move_1] = "X"
        y = display(test_board)
        
        move_2 = int(input("player_2 turn:"))
        y = test_board
        y[move_2] = "O"
        y = display(test_board)
        
        # win condition 
        if y[0]==y[1]==y[2]=="X":
            print("Player_1 wins!")
            break
            
        elif y[0]==y[3]==y[6]=="X":
            print("Player_1 wins!")
            break
            
            
        elif y[2]==y[5]==y[8]=="X":
            print("Player_1 wins!")
            break
            
        elif y[1]==y[4]==y[7]=="X":
            print("Player_1 wins!")
            break
            
        elif y[3]==y[4]==y[5]=="X":
            print("Player_1 wins!")
            break
            
        elif y[6]==y[7]==y[8]=="X":
            print("Player_1 wins!")
            break
            
        elif y[0]==y[4]==y[8]=="X":
            print("Player_1 wins!")
            break
            
        elif y[2]==y[4]==y[6]=="X":
            print("Player_1 wins!")
            break
            
        if y[0]==y[1]==y[2]=="O":
            print("Player_2 wins!")
            break
            
        elif y[0]==y[3]==y[6]=="O":
            print("Player_2 wins!")
            break
            
            
        elif y[2]==y[5]==y[8]=="O":
            print("Player_2 wins!")
            break
            
        elif y[1]==y[4]==y[7]=="O":
            print("Player_2 wins!")
            break
            
        elif y[3]==y[4]==y[5]=="O":
            print("Player_2 wins!")
            break
            
        elif y[6]==y[7]==y[8]=="O":
            print("Player_2 wins!")
            break
            
        elif y[0]==y[4]==y[8]=="O":
            print("Player_2 wins!")
            break
            
        elif y[2]==y[4]==y[6]=="O":
            print("Player_2 wins!")
            break
            
        
        # win condition
        
        i = i + 2    
    

def final():
    # first, the board will be displayed
    test_board = [" "," "," "," "," "," "," "," "," "]
    display(test_board)
    
    #second, the players will be asked to chose X or O
    user()
    
    #third, the game is initiated 
    game()
    
    

