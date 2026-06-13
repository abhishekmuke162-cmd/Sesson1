class Animal:
 def sound(self):
    print("some generic sound")

class Dog(Animal):
  def sound(self):
     print("woof")   

class Cat(Animal):
    def sound(self):
     print("meow")   

def make_sound(animal):
    animal.sound()  

d=Dog()
c=Cat()

make_sound(d) # Output: Bark
make_sound(c) # Output: meow    
