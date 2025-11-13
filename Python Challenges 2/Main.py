#Write a Python Program to create a Tic Tac Toe game.
#You can use different modules and functions to create this game.
#Make sure that you print the board after every move
#''' We will make the board using dictionary
#in which keys will be the location(i.e : top-left,mid-right,etc.)
#and initialliy it's values will be empty space and then after every move
#we will change the value according to player's choice of move. '''

TheBoard = {'7': ' ' , '8': ' ', '9': ' ' ,'4': ' ' , '5': ' ' , '6': ' ' ,'1': ' ' , '2': ' ' , '3': ' '}
turn="X"
count=0 
''' We will have to print the updated board after every move in the game and
thus we will make a function in which we'll define the printBoard function
so that we can easily print the board everytime by calling this function. '''
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
for i in range(10):
    printBoard(TheBoard)
    print("It's your turn," + turn + ".Move to which place?") 
    move = input()
    if TheBoard[move]==' ':
        TheBoard[move]=turn
        count=count+1
    else:
        print("The Place Is Already Filled.Pls Choose Another Place")
        continue
    if count>=5:
        if TheBoard['9']==TheBoard['8']==TheBoard['7']!=' ':
            printBoard(TheBoard)
            print("The Board At Top Won")
            break
        elif TheBoard['6']==TheBoard['5']==TheBoard['4']!=' ':
            printBoard(TheBoard)
            print("The Board At Middle Won ")
            break
        elif TheBoard['3']==TheBoard['2']==TheBoard['1']!=' ':
            printBoard(TheBoard)
            print("The Board At The Bottom Won")
            break
        elif TheBoard['7']==TheBoard['4']==TheBoard['1']!=' ':
            printBoard(TheBoard)
            print("The Column At first Won")
            break
        elif TheBoard['5']==TheBoard['8']==TheBoard['2']!=' ':
            printBoard(TheBoard)
            print("The Column At Middle Won")
            break
        elif TheBoard['9']==TheBoard['6']==TheBoard['3']!=' ':
            printBoard(TheBoard)
            print("The third Column Won")
            break
        elif TheBoard['9']==TheBoard['5']==TheBoard['1']!=' ':
            printBoard(TheBoard)
            print("diagonal won")
            break
        elif TheBoard['7']==TheBoard['5']==TheBoard['3']!=' ':
            printBoard(TheBoard)
            print("diagonal won")
            break
   # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:
        print("\nGame Over.\n")                
        print("It's a Tie!!")

    # Now we have to change the player after every move.
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'