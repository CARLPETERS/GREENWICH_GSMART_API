# True False
print(5==5)
print(5>5)

print("-----------------")

#None
print(None==0)
print((None == False))
print(None==[])
print(None == None)

def a_void_function():
    a = 1
    b = 2
    c = a+b

    return c # if wwe remove this return statement, the answer is noe
x = a_void_function()
print(x)

# and, or, not
print(True and False)
print(True or False)
print(True or True)
print(False or False)
print(not False)

#as
import math as myMath
print(myMath.cos(myMath.pi))

#assert
assert 5>4
assert 5==5

#break
for i in range(1,11):
    if i == 5:
        break
    print(i)

print("-----------------")

#continue
for i in range(1,8):
    if i == 5:
        continue
    print(i)

#class
class ExampleClass:
    def function1(parameters):
        print("Function1() Executing....")
    def function2(parameters):
        print("Function2() Executing....")
ob1=ExampleClass()
ob1.function1()
ob1.function2()

#def
def function_name(parameters):
    pass
function_name(10)

#del
a = 10
print(a)
del a
#print(a) # gives an error as the allocared data is already deleted

#if.. elif..else
num = 3
if num ==1:
    print('One')
elif num ==2:
    print('Two')
elif num == 3:
    print('Three')
else:
    print('Something Else')

# try...raise...catch...finally
try:
    x = 9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
    print("Execution Successful")

# from... import..
import math
from math import cos
print(cos(10))

#in
a= [1,2,3,4]
print(4 in a)

#is
print(True is True)

#lambda  (for anonymous function -- anonymous)
a = lambda x:x*2
for i in range(1,6):
    print(a(i))
    print(i, a(i))

def outerfunction():
    a=5
    def innerfunction():
        nonlocal a
        a = 10
        print("Inner Fucntion: ",a)
    innerfunction()
    print("Outer Function: ",a)
outerfunction()

#pass
def function(args):
    pass
function(10)

#while
i =5
while(i>0):
    print(i)
    i-=1

# with
with open('exmple.txt', 'w') as my_file:
    my_file.write("Hello World!")

# yield
def generator():
    for i in range(6):
        yield i*i

g=generator()
for i in g:
    print(i)

