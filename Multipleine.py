# Multiple inheritance
class parent1:
    parent1car = "BMW"

class parent2:
    parentcar2 = "mercedes"

class child(parent1, parent2):
    childcar = "alto"

objchild=child()  
print(objchild.parent1car)
print(objchild.parentcar2)   
