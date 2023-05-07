
"""
Decorator Pattern

It is a way of apparently modifying an objects behavior, by enclosing it inside a decorating object with a similar interface.

"""

"""
Behavior modification

Lets imagine an object A. If the method foo is called on it, it behaves in a certain way. The Decorator Pattern modifies this behavior. 
So when object A is decorated, the same foo method now behaves differently.

"""
# While we can also change behaviour by making subclass then why we have to use decorator pattern.
# Useful link: https://betterprogramming.pub/decorator-pattern-and-python-decorators-b0b573f4c1ce

class Add:

  def __init__(self,a,b):
    self.a = a
    self.b = b

  def process (self):
    return self.a + self.b

class Multiply:

  def __init__(self,decorated,num):
    self.decorated = decorated
    self.num = num

  def process(self):
    return self.decorated.process()*self.num

class Division:

  def __init__(self,decorated,num):
    self.decorated = decorated
    self.num = num

  def process(self):
    return self.decorated.process()/self.num

addition_obj = Add(5,5)
mul_obj = Multiply(addition_obj,4)
div_obj = Division(mul_obj,8)
after_changing_behaviour = div_obj.process()
# addition = addition_obj.process()
# print("addition*****",addition)
print("after_changing_behaviour******",after_changing_behaviour)

































