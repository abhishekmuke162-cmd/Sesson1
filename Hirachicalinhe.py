# Hierarchical inheritance
class Parent:
    parentcar1 = "BMW"
    parentcar2 = "mercedes"


class child1(Parent):
        child1car = "alto"

objchild1 = child1()
print(objchild1.child1car)
print(objchild1.parentcar1)

class child2(Parent):
    child2car = "swift"

objchild2 = child2()
print(objchild2.child2car)
print(objchild1.parentcar2)
