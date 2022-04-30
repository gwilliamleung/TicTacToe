from ast import Break

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ','mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M':' ','low-R':''}

def printBoard(board):
    print(board['top-L']+'|'+ board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+ board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+ board['low-M']+'|'+board['low-R'])
    
def winCon(board):
    if board['top-L'] == board['top-M'] == board['top-R'] == turn:
        printBoard(board)
        print( turn + " has won!")
        exit()
    if board['mid-L'] == board['mid-M'] == board['mid-R'] == turn:
        printBoard(board)
        print( turn + " has won!")
        exit()
    if board['low-L'] == board['low-M'] == board['low-R'] == turn:
        printBoard(board)
        print( turn + " has won!")
        exit()
    if board['top-L'] == board['mid-L'] == board['low-L'] == turn:
        printBoard(board)
        print( turn + " has won!")
        exit()
    if board['top-M'] == board['mid-M'] == board['low-M'] == turn:
        printBoard(board)
        print( turn + " has won!")
        exit()
    if board['top-R'] == board['mid-R'] == board['low-R'] == turn:
        printBoard(board)
        print( turn + " has won!")
        exit()
    if board['top-L'] == board['mid-M'] == board['low-R'] == turn:
        printBoard(board)
        print( turn + " has won!")
        exit()
    if board['top-R'] == board['mid-M'] == board['low-L'] == turn:
        printBoard(board)
        print( turn + " has won!")
        exit()

turn = 'X'
for i in range(9):
    printBoard(board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    board[move]= turn
    winCon(board)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(board)