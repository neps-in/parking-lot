from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def __init__(self):
      self.vtype = ''
      # Nothing
      print('v class')


class Car(Vehicle):

    def __init__(self, color, reg):
        self.color = color
        self.reg = reg
        self.vtype = 'car'


    def __str__(self):
        return " reg " + self.reg + " color: " + self.color 


class TwoWheeler(Vehicle):

  def __init__(self, color, reg):
    self.color = color
    self.reg = reg
    self.vtype = 'TV'

  def __str__(self):
    return " reg " + self.reg + " color: " + self.color 


# if __name__ == "__main__":

# 	c = Car('Green', '123')
# 	print( c.__str__() )