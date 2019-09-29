import math

class Mymath:
      def sqroot(self, x):
             return math.sqrt(x)
      def addition(self, x, y):
             return x+y
      def subtraction(self, x, y):
             return x-y
      def multiplication(self, x, y):
             return x*y
      def division(self, x, y):
             return x/y

if __name__=='__main__':
   m = Mymath()
   print(m.sqroot(3))
   print(m.addition(3, 4))
   print(m.subtraction(3, 4))
   print(m.multiplication(3, 4))
   print(m.division(3, 4))
