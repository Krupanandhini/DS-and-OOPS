# Python program to define  abstract class  
  
from abc import ABC    
class Polygon(ABC):     
   # abstract method   
   def sides(self):   
      pass  
  
class Triangle(Polygon):        
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):        
   def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):     
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):     
   def sides(self):   
      print("I have 4 sides")     
# Driver code   
t = Triangle()   
t.sides()   
  
s = square()   
s.sides()   
  
p = Pentagon()   
p.sides()   
  
k = Hexagon()   
K.sides()   

'''Output:
Triangle has 3 sides
Square has 4 sides
Pentagon has 5 sides
Hexagon has 6 sides
Explanation -
In the above code, we have defined the abstract base class named Polygon and we also defined the abstract method. This base class inherited by the various subclasses.
We implemented the abstract method in each subclass. We created the object of the subclasses and invoke the sides() method.The hidden implementations for the sides() method inside the each subclass comes into play. 
The abstract method sides() method, defined in the abstract class, is never invoked.'''