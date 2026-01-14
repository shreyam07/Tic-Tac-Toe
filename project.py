sum = lambda a,b,c : a+b+c # Lambda function for sum

def board(x,o): # Function to display current state of the board
    # Ternary operators to put 'X' or 'O' when user entered the value of the index else 0
    zero = 'X' if x[0] else ('O' if o[0] else 0)
    one = 'X' if x[1] else ('O' if o[1] else 1)
    two = 'X' if x[2] else ('O' if o[2] else 2)
    three = 'X' if x[3] else ('O' if o[3] else 3)
    four = 'X' if x[4] else ('O' if o[4] else 4)
    five = 'X' if x[5] else ('O' if o[5] else 5)
    six = 'X' if x[6] else ('O' if o[6] else 6)
    seven = 'X' if x[7] else ('O' if o[7] else 7)
    eight = 'X' if x[8] else ('O' if o[8] else 8)
    # Board formatting using f-string
    print(f"{zero} {one} {two} ")
    print(f"{three} {four} {five} ")
    print(f"{six} {seven} {eight} ") 

def check(x,o): # Declare player1 or player2 win by checking if one of them have occupied all the 3 spots
    # Winning combinations (fixed ways to win)
    rows =  [0,1,2], [3,4,5], [6,7,8]
    columns =  [0,3,6], [1,4,7], [2,5,8]
    diagonals = [0,4,8], [2,4,6]
    wins = list(rows+columns+diagonals)
    # Loop in in each winning combination to check win in each move
    for i in wins:
        if(sum(x[i[0]],x[i[1]],x[i[2]])==3):
            print(f'{player1} won the match!')
            return 1 # Indicates player 1 won
        if(sum(o[i[0]],o[i[1]],o[i[2]])==3):
            print(f'{player2} won the match!')
            return 0 # Indicates player 2 won
    return -1 # Indicates no one won

# Tic tac toe board is always a 9x9 matrix!!
# 0 : Empty | 1 : Occupied
x = [0,0,0,0,0,0,0,0,0] # Tracks moves of player1
o = [0,0,0,0,0,0,0,0,0] # Tracks moves of player2
turn = 1 # Tracks turns (1 : player1 | 0 : player2)

print('Welcome to Tic-Tac-Toe!!') # Greet both the players at start
player1 = input('Enter the name of player 1 : ')
player2 = input('Enter the name of player 2 : ')

# Function for looping in game 
while True:
    board(x,o) # Display board after each condition executes

    # Taking input of the index for each player where they want to put their mark (X,O)
    # Mark their spot as 1 in tracking lists (o,x)
    # Used try except to raise value or index error if user tries to enter a string or a number which is out of range
    if (turn==1): # for player1
        print(f'Current turn -> {player1}')
        try:
            index = int(input('Please enter the index where you want to put your mark : '))
        except IndexError: 
            print('Wrong number choosen! please choose a number between 0-8.')   
        x[index] = 1 
    else: # for player2
        print(f'Current turn -> {player2}')
        try:
            index = int(input('Please enter the index where you want to put your mark : '))
        except IndexError: 
            print('Wrong number choosen! please choose a number between 0-8.')
        o[index] = 1
    
    result = check(x,o) # Check if one of the players won after the move

    if (result != -1): # If check() returns 1 or 0 (not -1) , the match will over by simply breaking this loop
        print('MATCH OVER!')
        break

    turn = 1 - turn # Switching turns (if turn is 1 : 1-1=0 -> becomes player1's turn)
