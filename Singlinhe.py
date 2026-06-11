# Single inheritance
class Parent:
    Parentcar = "BMW"

class Child(Parent):
        Childcar = "alto"
objc = Child()
print( Parent.Parentcar)
print( objc.Childcar)
