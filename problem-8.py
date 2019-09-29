'''Python program to calculate area and circumference of a Circle'''

import math

class Circle(object):
      def area(self, radius):
          return math.pi*radius*radius
      def circumference(self, radius):
          return 2*math.pi*radius


if __name__=='__main__':
   c= Circle()
   print(c.area(5))
   print(c.circumference(5))
          