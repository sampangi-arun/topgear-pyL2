'''Matrix addition program using operator overloading'''

class Matrix(object):
    def __init__(self, row1=None, row2=None):
        self._matrix = (row1, row2)
    
    def __add__(self, m2):
        return Matrix((self._matrix[0][0] + m2._matrix[0][0], self._matrix[0][1]+m2._matrix[0][1]), (self._matrix[1][0] + m2._matrix[1][0], self._matrix[1][1]+m2._matrix[1][1]))
    
    def __str__(self):
        return str(self._matrix)

    
m = Matrix((1,2), (3, 4))
m2 = Matrix((1,2), (3,4))

print(m+m2)
        