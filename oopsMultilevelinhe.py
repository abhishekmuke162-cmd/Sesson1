# Multi-level inheritance
class GrandParent:
    GrandParentbike = "rajdoot"

class Parent(GrandParent):
    Parentcar = "BMW"

class Child(Parent):
        Childcar = "alto"
objc = Child()
print( objc.GrandParentbike)
print( objc.Parentcar)
print( objc.Childcar)
