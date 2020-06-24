## Alex Chalco 
# Tty_game.py (Creation date well say 4/21) 
# This is my first project in which I make a tic tac toe game that prints a board in which the players choose where they would like to place their game marker 
# Please let me know if there is anything wrong with the code pls and thankies 

def game_board(board):
    #clear_output()
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-----')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-----')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])

#This funtion will allow the user to choose whether Player 1 wants to be either X or O and depending on the first players input it will assign the variable player 1 and player 2 accordingly
def player_choice(choice):  
    if choice == 'X':
        player1 = 'X'
        player2 = 'O'
    elif choice == 'O':
        player1 = 'O'
        player2 = 'X'
    return player1,player2 
#The game board will be a 2D array to be able to check for rows later on for the win conditions 
board=[['','',''],['','',''],['','','']]
#game_board(board)
start = input('Player 1 Please choose if you want to be X or O(keep in mind that the input must be either capital X or capital O)')
player_choice(start)
counter = 0 

while counter < 4:  

    # This while loop will start the game and the while loop will remain for the remainder of the total number of possible turns that the game can be allowed to go for 
    play1 = input('Player 1 please input the location of where you would want your mark to be')
    play_1= int(play1)
    board[play_1]=(player1)
    #This allows Player 1 to choose where in the board they would like to place their respective marker on since the input is a string the variable play_1 would take the str input and convert it to a int and change the list accordingly

    play2= input('Player 2 please input the location of where you would want your maker to be')
    play_2 = int(play2)
    board[play_2]=(player2)
    #This allows the same the same thing to happen for player 2 

    game_board(board)
    # This will print out the board to what the current round is 

    # The following will be what determines the following rounds to come to be
    # Checks for win conditions/ conditions to continue 

    if board[0] == board[1] == board[2]:
        print('Congrats! Player {} you have won the game'.format(board[1]))
        break
    elif board[3] == board[4] == board[5]:
        print('Congrats! Player {} you have won the game'.format(board[4]))
        break 
    elif board[6] == board[7] == board[8]:
        print('Congrats! Player {} you have won the game'.format(board[7]))
        break
    elif board[2] == board[5] == board[8]:
        print('Congrats! Player {} you have won the game'.format(board[3]))
        break 
    elif board[1] == board[4] == board[7]:
        print('Congrats! Player {} you have won the game'.format(board[2]))
        break
    elif board[0] == board[3] == board[6]:
        print('Congrats! Player {} you have won the game'.format(board[1]))
        break
    elif board[0] == board[4] == board[8]:
        print('Congrats! Player {} you have won the game'.format(board[1]))
        break 
    elif board[2] == board[4] == board[6]:
        print('Congrats! Player {} you have won the game'.format(board[3]))
        break 
    elif counter == 4: 
        Print('Oh my! This match has ended in a Tie!')
    else:
        continue 
    #This big big series of if/ elif/ else statements serves the purpose to check if all possible win conditions have been met and in the case that by the 4th round no one is winning thne the loop will end and declare the game a draw 
counter += 1 

print('Thanks for playing!')