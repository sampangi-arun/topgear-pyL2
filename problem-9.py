'''Python program to calculate area and circumference of a Circle'''

import math

class Circle(object):
      def __init__(self, radius=None):
          self.radius = radius
      def area(self):
          return math.pi*self.radius*self.radius
      def circumference(self):
          return 2*math.pi*self.radius


if __name__=='__main__':
   c= Circle(5)
   print(c.area())
   print(c.circumference())
          
