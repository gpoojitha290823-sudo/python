#functions
#syntax:
# def function_name():
#    statements

#Creating function
def greet():
    print("Hello Poojitha!")  #Hello Poojitha!
greet()



def add():
    a = 10
    b = 20
    print(a+b)    #30
add()



#Functions with arguements
def add(a,b):
    print(a-b)           # a and b are parameters
                         # 20 and 5 are arguements
add(20,5)




def student(name):
    print("Hello",name)
student("Poojitha")
student("Python")




def greet(name="Student"):
    print("Hello",name)
greet()
greet("Poojitha")    


