'''Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).'''
                                               
# parent class
class Bird:    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):
    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

'''Output
Bird is ready
Penguin is ready
Penguin
Swim faster
Run faster'''

'''In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class). The child class inherits the functions of parent class. We can see this from the swim() method.
Again, the child class modified the behavior of the parent class. We can see this from the whoisThis() method. Furthermore, we extend the functions of the parent class, by creating a new run() method.
Additionally, we use the super() function inside the __init__() method. This allows us to run the __init__() method of the parent class inside the child class.'''
							
								SINGLE INHERITANCE
#Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.
 # Python program to demonstrate single inheritance
# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class
class Child(Parent):
	def func2(self):
		print("This function is in child class.")

# Driver's code
object = Child()
object.func1()
object.func2()

'''Output:
This function is in parent class.
This function is in child class.'''

								MULTIPLE INHERITANCE
'''When a class can be derived from more than one base class this type of inheritance is called multiple inheritance.
 In multiple inheritance, all the features of the base classes are inherited into the derived class. '''
# Python program to demonstrate multiple inheritance
# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)

# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)

# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

'''Output:
Father : RAM
Mother : SITA'''

								 MULTILEVEL INHERITANCE
'''In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and grandfather.''' 
# Python program to demonstrate multilevel inheritance
# Base class
class Grandfather:
	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
	def __init__(self,sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)

# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

'''Output:
Lal mani
Grandfather name : Lal mani
Father name : Rampal
Son name : Prince'''

							HEIRARCHICAL INHERITANCE
'''When more than one derived classes are created from a single base this type of inheritance is called hierarchical inheritance.
 In this program, we have a parent (base) class and two child (derived) classes.'''
# Python program to demonstrate Hierarchical inheritance
# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")

# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

'''Output:
This function is in parent class.
This function is in child 1.
This function is in parent class.
This function is in child 2.'''

							HYBRID INHERITANCE
#Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
# Python program to demonstrate hybrid inheritance

class School:
	def func1(self):
		print("This function is in school.")

class Student1(School):
	def func2(self):
		print("This function is in student 1. ")

class Student2(School):
	def func3(self):
		print("This function is in student 2.")

class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")

# Driver's code
object = Student3()
object.func1()
object.func2()

'''Output:
This function is in school.
This function is in student 1.'''
 