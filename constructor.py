#Constructor is the special function that is automatically executed when an object of a class is created. In Python, there is a special function called “init” which act as a Constructor.

class Sample:
    num=0
    def __init__(self, var):
        Sample.num+=1
        self.var=var
        print("The object value is = ", var)
        print("The count of object created = ", Sample.num)
S1=Sample(15)
S2=Sample(35)
S3=Sample(45)

'''In the above program, class variable num is shared by all three objects of the class Sample. It is initialized to zero and each time an object is created, the num is incremented by 1.
Since, the variable shared by all objects, change made to num by one object is reflected in other objects as well. Thus the above program produces the output given below.'''

'''Output
The object value is         =       15
The count of object created     =       1
The object value is         =       35
The count of object created     =       2
The object value is         =       45
The count of object created     =       3'''

	1.non-parameterized
class Student:  
    # Constructor - non parameterized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
student = Student()  
student.show("John")
'''output
This is non parametrized constructor
Hello John'''

	2.parameterized
class Student:  
    # Constructor - parameterized  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = Student("John")  
student.show()    
'''Output:
This is parametrized constructor
Hello John'''

	3.default
class Student:  
    roll_num = 101  
    name = "Joseph"  
  
    def display(self):  
        print(self.roll_num,self.name)  
  
st = Student()  
st.display()  
#Output:101 Joseph

	4.more than one constructor
class Student:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second contructor")  
st = Student()  
#Output:The Second Constructor