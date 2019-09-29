'''Sample program to illustrate MRO'''

class First:
    def method1(self):
        print("Hello From First1")

class Second(First):
    def method1(self):
        print("Hello From Second")
    
class Third(First):
    def method1(Self):
        print("Hello From Third")

class Fourth(Second, Third):
    def method1(self):
        print("Hello From Fourth")
    

# Method Resolution order would be Fourth -> Second -> Third -> # First

f = Fourth()
f.method1() # prints "Hello From Fourth"
