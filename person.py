class Person:
  
  def __init__(self, first, last):
    self.firstName = first
    self.lastName = last
    
  def Name(self):
    return self.firstName + " " + self.lastName
    
  def first_name(self):
    return self.firstName
