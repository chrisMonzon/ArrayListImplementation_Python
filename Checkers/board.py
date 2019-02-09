from pieces import *

class Board:

  
  def __init__(self, board =[]):
    self._board = [[Pieces(0,0,'blk'),'',Pieces(0,2,'blk'),'',Pieces(0,4,'blk'),'',Pieces(0,6,'blk'),''],
                  ['',Pieces(1,1,'blk'),'',Pieces(1,3,'blk'),'',Pieces(1,5,'blk'),'',Pieces(1,7,'blk')],
                  [Pieces(2,0,'blk'),'',Pieces(2,2,'blk'),'',Pieces(2,4,'blk'),'',Pieces(2,6,'blk'),''],
                  ['','','','','','','',''],
                  ['','','','','','','',''],
                  ['',Pieces(5,1,'wht'),'',Pieces(5,3,'wht'),'',Pieces(5,5,'wht'),'',Pieces(5,7,'wht')],
                  [Pieces(6,0,'wht'),'',Pieces(6,2,'wht'),'',Pieces(6,4,'wht'),'',Pieces(6,6,'wht'),''],
                  ['',Pieces(7,1,'wht'),'',Pieces(7,3,'wht'),'',Pieces(7,5,'wht'),'',Pieces(7,7,'wht')]]

  def printBoard(self):
    print "\n                0   1   2   3   4   5   6   7\n"
    for i in range(8):
      val = "          "+str(i) + '   | '
      print "              ---------------------------------"
      for j in range (8):
        if type(self._board[i][j]) is Pieces and self._board[i][j]._color == 'blk' and self._board[i][j]._status == 'king':
          val = val + "oo" + "| "
        elif type(self._board[i][j]) is Pieces and self._board[i][j]._color == 'blk':
          val = val + "o " + "| "
        elif type(self._board[i][j]) is Pieces and self._board[i][j]._color == 'wht' and self._board[i][j]._status == 'king':  
          val = val + "xx" + "| "
        elif type(self._board[i][j]) is Pieces and self._board[i][j]._color == 'wht':
          val = val+ "x " + "| "
        else:
          val = val + "  " + "| " 
      print val
    print "              ---------------------------------"
  
  def invalidMove(self, xi = 0, yi = 0, xf = 0, yf = 0,):
    if self._board[xi][yi] == '':
      print "Please pick a piece to move."
      return True
    else:
      if self._board[xi][yi]._status == 'king':
        if abs(xi - xf) == 1 and abs(yi - yf) == 1: #This is a valid move
          return False
        else:
          return True
      elif self._board[xi][yi]._color == 'blk' and self._board[xi][yi]._status == 'pawn' and xf > xi:
        if abs(xi - xf) == 1 and abs(yi - yf) == 1: #This is a valid move
          return False
        else:
          return True
      elif self._board[xi][yi]._color == 'wht' and self._board[xi][yi]._status == 'pawn' and xf < xi:
        if abs(xi - xf) == 1 and abs(yi - yf) == 1: #This is a valid move
          return False
        else:
          return True
      elif xf > 7 or xf < 0:
        print "Input out of bounds."
        return True
      elif yf > 7  or yf < 0:
        print "Input out of bounds."
        return True
      else:
        print "Invalid move."
        return True

  def crownCheck(self):
    for i in range(len(self._board[0])):
      if type(self._board[0][i]) is Pieces:
        if self._board[0][i]._color == 'wht':
          self._board[0][i]._status = 'king'
      if type(self._board[7][i]) is Pieces:
        if self._board[7][i]._color == 'blk':
          self._board[7][i]._status = 'king'
  
  def captureCheck(self,xi,yi,xf,yf):
    cont = input("capture piece?")
    flag = True
    while cont == 'yes':
      if xf < xi: #if capturing a piece higher
        if self._board[xi - 2][yi + 2] == '': # right space
          if (xf - 1) < 0 or (yf + 1) > 7:
            print "Out of bound..."
            return
          flag = False
          self._board[xf - 1][yf + 1] = self._board[xi][yi]
          self._board[xi][yi] = ''
          self._board[xf][yf] = ''
        elif self._board[xi - 2][yi - 2] == '':
          if (xf - 1) < 0 or (yf - 1) < 0:
            print('Out of bound...')
            return
          flag = False
          self._board[xf - 1][yf - 1] = self._board[xi][yi]
          self._board[xi][yi] = ''
          self._board[xf][yf] = ''
          xf = xf - 1
          yf = yf - 1
        else:
          break
        if flag == True:
          row = int(input("Continue capturing...\nEnter row: "))
          column = int(input("\nEnter column: "))
          self.captureCheck(xf, yf, row, column)
      elif xf > xi:
        if self._board[xi + 2][yi + 2] == '': # if right space is open
          if (xf + 1) > 8 or (yf + 1) > 8:
            print('Out of bound...')
            return
          flag = False
          self._board[xf +1][yf+1] = self._board[xi][yi] 
          self._board[xi][yi] = ''
          self._board[xf][yf] = ''
        elif self._board[xi + 2][yi - 2] == '': #if left space is open
          if (xf + 1) > 8 or (yf - 1) < 0:
            print('Out of bound...')
            return
          flag = False
          self._board[xf + 1][yf - 1] = self._board[xi][yi]
          self._board[xi][yi] = ''
          self._board[xf][yf] = ''
          xf = xf - 1
          yf = yf - 1
        else:
          break
        if flag == True:
          print flag
          row = int(input("Continue capturing...\nEnter row: "))
          column = int(input("\nEnter column: "))
          self.captureCheck(xf, yf, row, column)
      else:
        break
      self.printBoard()
  
  
   
  def move(self, xi = 0, yi = 0, xf = 0, yf = 0, c = ''):
    if self.invalidMove(xi, yi, xf, yf) == False:
      if self._board[xf][yf] == '':
        self._board[xf][yf] = self._board[xi][yi]
        self._board[xi][yi] = ''
      elif self._board[xf][yf] != '':
        if (self._board[xi][yi]._color == "wht" and self._board[xf][yf]._color == 'blk') or (self._board[xi][yi]._color == 'blk' and self._board[xf][yf]._color == 'wht'):
          self.captureCheck(xi,yi,xf,yf)
          
        else:
          print "Invalid move."
      else:
        return True
    else:
      return False 