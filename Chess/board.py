from pieces import *

class Board:
  kingCount = 0
  bD = {'pawn':'b ','Rook':'bR','Knight':'bH','Bishop':'bB','Queen':'bQ','King':'bK'}
  wD = {'pawn':'w ','Rook':'wR','Knight':'wH','Bishop':'wB','Queen':'wQ','King':'wK'}
  
  def __init__(self, board =[]):
    self._board = [[Pieces(0,0,'blk', 'Rook'),Pieces(0,1,'blk', 'Knight'),
                  Pieces(0,2,'blk','Bishop'),Pieces(0,3,'blk','Queen'),
                  Pieces(0,4,'blk', 'King'),Pieces(0,5,'blk','Bishop'),
                  Pieces(0,6,'blk', 'Knight'),Pieces(0,7,'blk', 'Rook')],
                  
                  [Pieces(1,0,'blk','pawn'), Pieces(1,1,'blk','pawn'), Pieces(1,2,'blk','pawn'), 
                  Pieces(1,3,'blk', 'pawn'), Pieces(1,4,'blk', 'pawn'), Pieces(1,5,'blk', 'pawn'), 
                  Pieces(1,6,'blk','pawn'), Pieces(1,7,'blk','pawn')],
                  
                  [Pieces(2,0,'null'),Pieces(2,1,'null'),Pieces(2,2,'null'),Pieces(2,3,'null'),
                  Pieces(2,4,'null'),Pieces(2,5,'null'),Pieces(2,6,'null'),Pieces(2,7,'null'),],
                  [Pieces(3,0,'null'),Pieces(3,1,'null'),Pieces(3,2,'null'),Pieces(3,3,'null'),
                  Pieces(3,4,'null'),Pieces(3,5,'null'),Pieces(3,6,'null'),Pieces(3,7,'null'),],
                  [Pieces(4,0,'null'),Pieces(4,1,'null'),Pieces(4,2,'null'),Pieces(4,3,'null'),
                  Pieces(4,4,'null'),Pieces(4,5,'null'),Pieces(4,6,'null'),Pieces(4,7,'null'),],
                  [Pieces(5,0,'null'),Pieces(5,1,'null'),Pieces(5,2,'null'),Pieces(5,3,'null'),
                  Pieces(5,4,'null'),Pieces(5,5,'null'),Pieces(5,6,'null'),Pieces(5,7,'null'),],
                  
                  [Pieces(6,0,'wht', 'pawn'), Pieces(6,1,'wht', 'pawn'), Pieces(6,2,'wht', 'pawn'), 
                  Pieces(6,3,'wht', 'pawn'), Pieces(6,4,'wht', 'pawn'), Pieces(6,5,'wht', 'pawn'), 
                  Pieces(6,6,'wht', 'pawn'), Pieces(6,7,'wht', 'pawn')],
                  
                  [Pieces(0,0,'wht', 'Rook'),Pieces(0,1,'wht', 'Knight'),
                  Pieces(0,2,'wht','Bishop'),Pieces(0,3,'wht','Queen'),
                  Pieces(0,4,'wht', 'King'),Pieces(0,5,'wht','Bishop'),
                  Pieces(0,6,'wht', 'Knight'),Pieces(0,7,'wht', 'Rook')]]
    self.gameEnd = False
                  
  def printBoard(self):
    global kingCount, gameEnd
    global wD, bD
    kingCount = 0
    for i in self._board[0]:
      if i._status == "pawn" and i._color == "wht":
        newStat = input("You just crowned a piece! Enter pawn's new status: ")
        print(newStat)
        print self.wD.get(newStat)
        i._status = newStat
        #i = Pieces(0,yf,'wht',newStat)
    for j in self._board[7]:
      if j._status == "pawn" and j._color == "wht":
        newStat = input("You just crowned a piece! Enter a pawn's new status: ")
        j._status = newStat
        #j = Pieces(xf,yf,'wht',newStat)
    for k in range(0,8):
      for l in range(0,8):
        if self._board[k][l]._status == 'King':
          kingCount += 1
    if kingCount == 1:
      for m in range(0,8):
        for n in range(0,8):
          if self._board[m][n]._status == 'King':
            if self._board[m][n]._color == 'wht':
              print "White wins!"
            elif self._board[m][n]._color == 'blk':
              print "black wins!"
              #print kingCount
            self.gameEnd = True
              
      
    print "\n                0   1   2   3   4   5   6   7\n"
    for i in range(8):
      val = "          "+str(i) + '   | '
      print "              ---------------------------------"
      #print "              _________________________________"
      #""""
      for j in range (8):
        if  type(self._board[i][j]) is Pieces and self._board[i][j]._color == 'blk':
          val = val + self.bD.get(self._board[i][j]._status) + "| "
        elif  type(self._board[i][j]) is Pieces and self._board[i][j]._color == 'wht':
          val = val + self.wD.get(self._board[i][j]._status) + "| "
        else:
          val = val + "  " + "| "
      
      print val
    print "              ---------------------------------"
    kingCount = 0
    

      
  def pMove(self, xi = 0, yi = 0, xf = 0, yf = 0, c = ''):
    global bD, wD
    #MOVING
    if self._board[xf][yf]._status == 'null':
      if self._board[xi][yi]._color == 'wht':
        if yf == yi and xf == xi - 2 and  xi == 6:
          self._board[xf][yf] = self._board[xi][yi]
          self._board[xi][yi] = Pieces(xi, yi, 'null')
        elif yf == yi and xf == xi - 1:
          self._board[xf][yf] = self._board[xi][yi]
          self._board[xi][yi] = Pieces(xi, yi, 'null')
        else:
          print "Invalid move"
      elif self._board[xi][yi]._color == 'blk':
        if yf == yi and xf == xi + 2 and  xi == 1:
          self._board[xf][yf] = self._board[xi][yi]
          self._board[xi][yi] = Pieces(xi, yi, 'null')
        elif yf == yi and xf == xi + 1:
          self._board[xf][yf] = self._board[xi][yi]
          self._board[xi][yi] = Pieces(xi, yi, 'null')
        else:
          print "Invalid move"
    #CAPTURING
    elif xf == xi - 1 and (yf == yi - 1) or (yf == yi + 1) and  self._board[xf][yf]._color == "blk":
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Pieces(xi, yi, 'null')
    elif xf == xi + 1 and (yf == yi- 1) or (yf == yi + 1) and  self._board[xf][yf]._color == "wht":
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Pieces(xi, yi, 'null')
    
    else:
      print "Invalid move, my dude."
        
  def rMove(self, xi = 0, yi = 0, xf = 0, yf = 0, c = ''):
    if (xi == xf) or (yi == yf) and (xi + yi) != (xf + yf):
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Pieces(xi,yi,'','null')
    else:
      print "Invalid move."
      
  def kMove(self, xi = 0, yi = 0, xf = 0, yf = 0, c = ''):
    dx = abs(xi - xf)
    dy = abs(yi - yf)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Pieces(xi,yi,'','null')
    else:
      print "Invalid move."
      
  def bMove(self, xi = 0, yi = 0, xf = 0, yf = 0, c = ''):
    if abs(xi - xf) == abs(yi - yf) and (xi + yi) != (xf + yf):
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Pieces(xi,yi,'','null')
    else:
      print "Invalid move."
  
  def qMove(self, xi = 0, yi = 0, xf = 0, yf = 0, c = ''):
    if xi == xf or yi == yf:
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Piece(xi,yi,'','null')
    elif abs(xi - yi) == abs(xf - yf):
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Pieces(xi,yi,'','null')
    else:
      print "Invalid move."
      
  def kgMove(self, xi = 0, yi = 0, xf = 0, yf = 0, c = ''):
    
    if abs (xi - xf) <= 1 and abs(yi - yf) <= 1:
      
      if self._board[xi][yi]._color == 'wht': 
        if self._board[xf][yf]._color != 'wht':# and self._board[xf][yf]._status == 'null':
          self._board[xf][yf] = self._board[xi][yi]
          self._board[xi][yi] = Pieces(xi,yi,'','null')
        else:
          print "Invalid move."
      elif self._board[xi][yi]._color == 'blk':
        
        if self._board[xf][yf]._color != 'blk':# and self._board[xf][yf]._status == 'null':
          self._board[xf][yf] = self._board[xi][yi]
          self._board[xi][yi] = Pieces(xi,yi,'','null')
        else:
          print "invalid move."
    else:
      print "InValId MOvE"
  
  def collisionCheck (self, xi = 0, yi = 0, xf = 0, yf = 0, s = '', c = ''):
    
    if self._board[xi][yi]._status == 'Rook':
      if xi == xf:
        if self._board[xi][yi]._color == 'wht':
          for i in range (yi,yf + 1):
            if self._board[xi][i]._color == 'wht':
              return True
        elif self._board[xi][yi]._color == 'blk':
          for i in range (yi,yf + 1):
            if self._board[xi][i]._color == 'blk':
              return True
      elif yi == yf:
        if self._board[xi][yi]._color == 'wht':
          #print "whiiiiiiiiite"
          if xi > xf:
            for i in range (xi,xf - 1, -1):
              if self._board[xi][i]._color == 'wht' or self._board[xi][i]._color == 'blk':
                #print "YA YEET"
                return True
          else:
            for i in range (xi,xf + 1):
              if self._board[xi][i]._color == 'wht' or self._board[xi][i]._color == 'blk':
                #print "YA YEET"
                return True
        elif self._board[xi][yi]._color == 'blk':
          #rint "blaaaaack"
          if xi > xf:
            for i in range (xi,xf + 1):
              if self._board[xi][i]._color == 'blk':
                #print "FETUS DELETUS"
                return True
          else:
            for i in range (xi,xf - 1, -1):
              if self._board[xi][i]._color == 'blk':
                #print "FETUS DELETUS"
                return True
              
              




    elif self._board[xi][yi]._status == 'Bishop':
      if self._board[xi][yi] == 'wht':
        if yf < yi:
          for i in range(xi, xf + 1):
            for j in range(yf, yi - 1,  -1):
              if self._board[i][j]._color == 'wht':
                return True
        elif yf > yi:
          for i in range(xi, xf + 1):
            for j in range(yi, yf + 1):
              if self._board[i][j]._color == 'wht':
                return True
      elif self._board[xi][yi]._color == 'blk':
        if yf < yi:
          print "diagonal left"
          for i in range(xi, xf +1):
            for j in range(yf, yi + 1):
              if self._board[i][j]._color == 'blk':
                return True
        elif yf > yi:
          print "diagonal right"
          for i in range(xi, xf + 1):
            for j in range(yi, yf + 1):
              if self._board[i][j]._color == 'blk':
                return True
        elif self._board[xf][yf]._color == "blk":
          return True
                
    elif self._board[xi][yi]._status == 'Queen':
      if xi == xf or yi == yf:
        if xi == xf:
          if self._board[xi][yi]._color == 'wht':
            for i in range (yi,yf + 1):
              if self._board[xi][i]._color == 'wht':
                return True
          elif self._board[xi][yi]._color == 'blk':
            for i in range (yi,yf + 1):
              if self._board[xi][i]._color == 'blk':
                return True
        elif yi == yf:
          if self._board[xi][yi]._color == 'wht':
            for i in range (xi,xf + 1):
              if self._board[xi][i]._color == 'wht':
                return True
          elif self._board[xi][yi]._color == 'blk':
            for i in range (xi,xf + 1):
              if self._board[xi][i]._color == 'blk':
                return True
      elif abs(xi - yi) == abs(xf - yf):
        if self._board[xi][yi] == 'wht':
          if yf < yi:
            for i in range(xi, xf + 1):
              for j in range(yf, yi - 1,  -1):
                if self._board[i][j]._color == 'wht':
                  return True
          elif yf > yi:
            for i in range(xi, xf + 1):
              for j in range(yi, yf + 1):
                if self._board[i][j]._color == 'wht':
                  return True
        elif self._board[xi][yi] == 'blk':
          if yf < yi:
            for i in range(xi, xf - 1, -1):
              for j in range(yf, yi + 1):
                if self._board[i][j]._color == 'blk':
                  return True
          elif yf > yi:
            for i in range(xi, xf - 1, - 1):
              for j in range(yi, yf - 1, -1):
                if self._board[i][j]._color == 'blk':
                  return True
        else:
          return True
      else:
        return False
        
  def statCheck(self, xi = 0, yi = 0, xf = 0, yf = 0, s = '', c = ''):
    print(xi, yi, xf, yf)
  
    if s == 'pawn':
      self.pMove(xi, yi, xf, yf, self._board[xi][yi]._color)
      
    elif s == "Rook":
      self.rMove(xi, yi, xf, yf, self._board[xi][yi]._color)
    elif s == "Knight":
      self.kMove(xi, yi, xf, yf, self._board[xi][yi]._color)
    elif s == "Bishop":
      self.bMove(xi, yi, xf, yf, self._board[xi][yi]._color)
    elif s == "Queen":
      self.qMove(xi, yi, xf, yf, self._board[xi][yi]._color)
    else:
      print self._board[xi][yi]._color
      self.kgMove(xi, yi, xf, yf, self._board[xi][yi]._color)
    
  """
  def capCheck (self, xi = 0, yi = 0, xf = 0, yf = 0, s = '', c = ''):
    if s == 'pawn':
      elif xf == xi - 1 and (yf == yi - 1) or (yf == yi + 1) and  self._board[xf][yf]._color == "blk":
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Pieces(xi, yi, 'null')
    elif xf == xi + 1 and (yf == yi- 1) or (yf == yi + 1) and  self._board[xf][yf]._color == "wht":
      self._board[xf][yf] = self._board[xi][yi]
      self._board[xi][yi] = Pieces(xi, yi, 'null')
          
    elif s == "Rook":
      self.rMove(xi, yi, xf, yf, self._board[xi][yi]._color)
    elif s == "Knight":
      self.kMove(xi, yi, xf, yf, self._board[xi][yi]._color)
    elif s == "Bishop":
      self.bMOve(xi, yi, xf, yf, self._board[xi][yi]._color)
    elif s == "Queen":
      self.qMove(xi, yi, xf, yf, self._board[xi][yi]._color)
    else:
      self.kgMove(xi, yi, xf, yf, self._board[xi][yi]._color)
  """