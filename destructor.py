#Destructor is also a special method gets executed automatically when an object exit from the scope. It is just opposite to constructor. In Python, __del__( ) method is used as destructor.

class Sample:
    num=0
    def __init__(self, var):
        Sample.num+=1
        self.var=var
        print("The object value is = ", var)
        print("The value of class variable is= ", Sample.num)
    def __del__(self):
        Sample.num-=1
        print("Object with value %d is exit from the scope"%self.var)

S1=Sample(15)
S2=Sample(35)
S3=Sample(45)

'''Output
The object value is =  15
The value of class variable is=  1
The object value is =  35
The value of class variable is=  2
The object value is =  45
The value of class variable is=  3
Object with value 35 is exit from the scope
Object with value 45 is exit from the scope
Object with value 15 is exit from the scope'''