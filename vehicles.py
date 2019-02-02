class Vehicles:
  
  def __init__(self):
    self.wheels = 0
    
  def getWheels(self):
    return self.wheels
    return self.price
    
  def setWheels(self, w, p):
    self.wheels = w
    self.price = p
    
class Bike(Vehicle):
  def __init__(self):
    Vehicles.__init__(self)
    self.wheels = 2
    self.price = 1000
  
class PedalBike(Bike):
  def __init__(self):
    Bike.__init__(self)
    self.status = 'human powered'
  
  def getStatus(self):
    return self.status
    
class MotorBike(Bike):
  def __init__(self):
    Bike.__init__(self)
    self.status = 'motor powered'
  
  def getStatus(self):
    return self.status
    
class Car(Vehicles):
  def __init__(self):
    Vehicles.__init__(self)
    self.wheels = 4
    self.price = 10000
    
  def getPrice(self):
    return self.price
    
class SportsCar(Car):
  def __init__(self):
    Car.__init__(self)
    self.price = 30000
    
class Van(Car):
  def __init__(self):
    Van.__init__(self)
    self.price = 34000
    
class Van(Car):
  def __init__(self):
    Van.__init__(self)
    self.price = 34000
    
class PickUps(Car):
  def __init(self):
    PickUps.__init__(self)
    self.price = 40000
    
class Convertible(Car):
  def __init__(self):
    Convertible.__init__(self)
    self.price = 35000
    
class StationWagon(Car):
  def __init__(self):
    Convertible.__init__(self)
    self.price = 36000
  
class Bus(Vehicles):
  def __init__(self):
    Bus.__init__(self)
    self.wheels = 6
    
class Trucks(Vehicles):
  def __init__self:
    Bus.__init__(self)
    self.wheels = 999
    
class HeavyTrucks(Trucks):
  def __init__(self):
    HeavyTrucks.__init__(self)
    self.wheels 99999
    
class MediumTrucks(Trucks):
  def __init__(self):
    MediumTrucks.__init__(self)
    