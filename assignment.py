# Assignment 1
a=3
print(a) # integer
type(a)
b=3.52   # Float
print(b)
type (b)
Welcome ="Hello Everyone"  # String
print(Welcome)  
type(Welcome)
Bool1= 5   # Boolean
Bool2=10
if(Bool1<Bool2): 
    print('True')
# getting two input and printing
first_name=input("Enter your First Name:") 
last_name=input("Enter your Last name:")
full_name=first_name + last_name
print ("Your full name is:", full_name)
# Currency convertor
Currency=int(input("Enter the value in USD:"))
newvalue = Currency-0.04
print ("The value of Euro is" ,newvalue)
## Operators
# Sqaure of a number
num1 =5
num2 = num1 * num1
print(num2)
# Cube of a number
num1=5
num2=num1**3
print(num2)
##Square root of a number
square_root =49
result=square_root**0.5
print(result)
##Logical operator
#Positive and even
A=int(input("Enter the value to Check:"))
if (A>0 and A%2==0):
    print("The number is Positive and even")
else:
    print("The number is Not positive and even")
##Greater than 10 or lesser than -10
B= int(input("Enter the Value:"))
if ( B>10 ):
   print("The number you entered is greater than 10")
elif  B < -10:
   print("The number you entered is greater than 10")
else:
    print("The number is not greater than 10 or less than -10")
##Neither positive or divisible by 5
Q=int(input('Q:'))
if (Q>0 or Q%5==0):
    print('True')
else:
     Print('False')
##Functions
# Area of a rectangle (Formula is Area= Length * Width)
length=int(input("Length"))
width=int(input('Width'))
def area_of_rectangle():
    return length*width

r= area_of_rectangle()
print("the area of rectangle is :", r)
##Temperature convertor (Fareinheit as input and convert to celsius)(Formula : (Fareinheit-32)*5/9
farenheit= int(input("Enter the temperature in Farenheit:"))
def temp():
    return (farenheit-32)*5/9
t=temp()
print("The celsius equivalent is:",t)
## Simple interest( i=pnr/100)
p= int(input('p'))
n=int(input('n'))
r=int(input('r'))
def simple_int():
    return p*n*r/100
si=simple_int()
print("The simple interesr is: ", si)
## Fibonacci to be tried
## Multiplication table for 
n=int(input("Enter the num:"))
for i in range(1,11):
    print(i,"x",n,"=",i*n)
## Printing even numbers
for n in range(0,20):
    if n%2==0:
        print(n)
##Assignment 2
# create a variable and print you name
name="Archana"
print(name)
# Sum
num1=10
num2=20
num3=num1+num2
print(num3)
# Sring Concatenation
word1="Hello"
word2="World"
print(word1+word2)
#Check data type
num4=3.15
type(num4)
## Variable Swap
S1=10
S2=50
S1,S2=S2,S1
Print("s1",S1)
print("s2",S2)
