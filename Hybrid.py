# Hybrid Inheritance
class parent1:
    parentcar1 = "BMW"

class parent2:
    parentcar2 = "mercedes"

class child1(parent1,parent2):
    child1car = "alto"

objchild1=child1()
print(objchild1.child1car)
print(objchild1.parentcar1)

class child2(parent1,parent2):
    child2car = "swift"

objchild2 = child2()
print(objchild2.child2car)
print(objchild2.parentcar2)
