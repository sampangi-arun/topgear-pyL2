
'''String compare program based on the length of the data'''

class StrCompare(object):
      def __init__(self, s1):
          self.s1 = s1
      def __gt__(self, s2):
          return len(self.s1)>len(s2)

if __name__=='__main__':
     s = StrCompare('hello')
     print(s > 'world')