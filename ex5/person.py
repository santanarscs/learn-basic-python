#person.py
class Person:

  def setName(self, name):
    self.name = name

  def setAge(self, age):
    self.age = age

  def setHeight(self, height):
    self.height = height

  def setWeight(self, weight):
    self.weight = weight

  def getName(self):
    return self.name

  def getAge(self):
    return self.age

  def getHeight(self):
    return self.height

  def getWeight(self):
    return self.weight
    
  def getImc(self):
    return self.weight / (self.height * self.height)