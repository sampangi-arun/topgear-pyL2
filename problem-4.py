import math

class Mymath:
      def __init__(self, x, y=None):
          self.x = x
          self.y = y
      def sqroot(self):
          return math.sqrt(self.x)
      def addition(self):
          if self.y:
             return self.x+self.y
      def subtraction(self):
          if self.y:
             return self.x-self.y
      def multiplication(self):
          if self.y:
             return self.x*self.y
      def division(self):
          if self.y and self.y!=0:
             return self.x/self.y

if __name__=='__main__':
   m = Mymath(3, 4)
   print(m.sqroot())
   print(m.addition())
   print(m.subtraction())
   print(m.multiplication())
   print(m.division())