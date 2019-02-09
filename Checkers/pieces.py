class Pieces:
  def __init__(self, x = 0, y = 0, c = '' , s='pawn'):
    self._x = x
    self._y = y
    self._color = c
    self._status = 'pawn'
    
  def getX(self):
    return self._x
    
  def getY(self):
    return self._y
    
  def getColor(self):
    return self._color
    
  def getStatus(self):
    return self._status