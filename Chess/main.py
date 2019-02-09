from board import *
from pieces import *

whtTurn = True
board = Board()

#board.move(5,5,4,4)
#board.move(2,2,3,3)

print "It's white turn."

while board.gameEnd == False:
  board.printBoard()
  if whtTurn == True and board.gameEnd == False:
    print "It's white turn."
    #print board._board[5][0]._status
    xi1 = int(input("Enter the row your piece is in: "))
    yi1 = int(input("Enter the column your piece is in: "))
    if board._board[xi1][yi1]._color == 'wht':
      xf1 = int(input("Enter the row you want to move your piece to: "))
      yf1 = int(input("Enter the column you want to move your piece to: "))
      if board.collisionCheck(xi1, yi1, xf1, yf1,board._board[xi1][yi1]._status,'wht' ) == True:
        print "\nthats an INVALID MOVE  go back to kindergarten"
        xi1 = int(input("Enter the row you want to move your piece to: "))
        yi1 = int(input("Enter the column you want to move your piece to: "))
        xf1 = int(input("Enter the row you want to move your piece to: "))
        yf1 = int(input("Enter the column you want to move your piece to: "))
      else:
        board.statCheck(xi1, yi1, xf1, yf1, board._board[xi1][yi1]._status,'wht')
        whtTurn = False
    else:
      print("You can't move that piece!")
  elif whtTurn == False and board.gameEnd == False:
    print "It's black turn."
    xi1 = int(input("Enter the row your piece is in: "))
    yi1 = int(input("Enter the column your piece is in: "))
    if board._board[xi1][yi1]._color == "blk":
      xf1 = int(input("Enter the row you want to move your piece to: "))
      yf1 = int(input("Enter the column you want to move your piece to: "))
      if board.collisionCheck(xi1, yi1, xf1, yf1,board._board[xi1][yi1]._status,'blk' ) == True:
        print "\nthats an INVALID MOVE  go back to kindergarten"
        xi1 = int(input("Enter the row you want to move your piece to: "))
        yi1 = int(input("Enter the column you want to move your piece to: "))
        xf1 = int(input("Enter the row you want to move your piece to: "))
        yf1 = int(input("Enter the column you want to move your piece to: "))
      else:
        board.statCheck(xi1, yi1, xf1, yf1, board._board[xi1][yi1]._status,'blk')
        whtTurn = True
    else:
      print("You can't move that piece!")
print "thanks 4 playing"

  
