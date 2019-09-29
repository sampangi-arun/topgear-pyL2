'''Simple Inheritance prgoram'''

import math

class sqroot(object):
      def sqrt(self, x):
          return math.sqrt(x)

class addition(object):
      def add(self, x, y):
          return x+y

class subtraction(object):
      def sub(self, x, y):
          return x-y

class multiplication(object):
      def mul(self, x, y):
          return x*y

class division(object):
      def div(self, x, y):
          return x/y

class mathnew(sqroot, addition, subtraction, multiplication, division):
      def __init__(self, x, y):
          self.x = x
          self.y = y
      def sqroot(self):
          return super().sqrt(self.x)
      def addition(self):
          return super().add(self.x, self.y)
      def subtraction(self):
          return super().sub(self.x, self.y)
      def multiplication(self):
          return super().mul(self.x, self.y)
      def division(self):
          return super().div(self.x, self.y)

if __name__=='__main__':
   m = mathnew(3, 4)
   print(m.addition())
   print(m.sqroot())
   print(m.subtraction())
   print(m.multiplication())
   print(m.division())