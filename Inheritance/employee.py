from person import Person

class Employee(Person):
  
  def __init__(self, first, last, staffnum):
    Person.__init__(self, first, last)
    self.staffnumber = staffnum
    
  def GetEmployee (self):
    return self.Name() +", " + self.staffnumber
    
