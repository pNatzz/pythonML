"""[Class]
- Class => Myfriend
- Method => changeName
- Object => myfriend
"""

class Myfriend:

    name = "Ning" # define an attibute called name

    def changeName(self): # changeName is a method --> method to change name

        Myfriend.name = "JJ" # change the value of the attribute within a method

myfriend = Myfriend() # create object to class (Object = myfriend, Class = Myfriend)
print(myfriend.name)
myfriend.changeName() # call the method
print(myfriend.name)
