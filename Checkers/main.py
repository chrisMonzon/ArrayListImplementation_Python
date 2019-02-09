from board import *
from pieces import *

whtTurn = True
board = Board()

#board.move(5,5,4,4)
#board.move(2,2,3,3)

print "It's white turn."

while True:
  board.printBoard()
  if whtTurn == True:
    print "It's white turn."
    xi1 = int(input("Enter the row your piece is in: "))
    yi1 = int(input("Enter the column your piece is in: "))
    if board._board[xi1][yi1]._color == 'wht':
      xf1 = int(input("Enter the row you want to move your piece to: "))
      yf1 = int(input("Enter the column you want to move your piece to: "))
      board.move(xi1,yi1,xf1,yf1)
      whtTurn = False
    else:
      print("You can't move that piece!")
  elif whtTurn == False:
    print "It's black turn."
    xi1 = int(input("Enter the row your piece is in: "))
    yi1 = int(input("Enter the column your piece is in: "))
    if board._board[xi1][yi1]._color == 'blk':
      xf1 = int(input("Enter the row you want to move your piece to: "))
      yf1 = int(input("Enter the column you want to move your piece to: "))
      board.move(xi1,yi1,xf1,yf1)
      whtTurn = True
    else:
      print("You can't move that piece!")
  
  board.crownCheck()
  
