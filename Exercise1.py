#Area of rectangle
length=int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length*width
print("The area of the rectangle is ", area)

#Simple Interest
p=int(input("Enter the principal amount: "))
t=int(input("Enter the time: "))
r=int(input("Enter the rate: "))
interest=(p*t*r)/100
print("The interest rate is ",interest)

#Celsius to Fahrenheit
temp=int(input("Enter the temperature in Celsius: "))
Fahrenheit=(temp*9/5)+32
print("The temperature in Fahrenheit is ",Fahrenheit)

#Average of 3 numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
average=(a+b+c)/3
print("The average is",average)

#Square and cube of a number
n=int(input("Enter the number: "))
sq=n*n
print("The square is",sq)
cube=n*n*n
print("The cube is",cube)

#Swap two numbers without using third variable
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
a, b = b, a
print("After swapping:")
print("First number =", a)
print("Second number =", b)

#StudentReport
sub1=int(input("Enter the marks obtained in Subject 1: "))
sub2=int(input("Enter the marks obtained in Subject 2: "))
sub3=int(input("Enter the marks obtained in Subject 3: "))
sub4=int(input("Enter the marks obtained in Subject 4: "))
sub5=int(input("Enter the marks obtained in Subject 5: "))
total=sub1+sub2+sub3+sub4+sub5
print("The total is",total)
per=(total/5)*100
print("The percentage is",per)
print(f"The student scored {total} marks , resulting in a percentage of {per} % ")


