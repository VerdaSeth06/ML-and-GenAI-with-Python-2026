#Calculate the Sum of first 10 natural numbers
sum=0
for i in range(1,11):
 sum+=i
 print("Sum of first 10 natural numbers=",sum)

#Program for factorial of a number
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
  fact*=i
  print("Factorial=",fact)

#Program for fibonacci series
n=int(input("Enter a number:"))
a=0
b=1
print("Fibonacci series:")
for i in range(n):
  print(a,end="")
  c=a+b
  a=b
  b=c

#Program largest among three number
a=int(input("Enter first number:"))
b=int(input("Enter second number: "))
c=int(input("Enter third number:"))

if a>=b and a>=c:
 largest=a
elif b>=a and b>=c:
 largest=b
else:
  largest=c

print("Largest number=",largest)

#Program for student result
name=input("Enter Student name:")
roll=input("Enter roll numbers:")
total=0
subjects=5
for i in range(1,subjects+1):
 marks=float(input(f"Enter marks of Subject{i}:"))
total+=marks
percentage=total/subjects

if percentage>=90:
  grade="A"
elif percentage>=80:
  grade="B"
elif percentage>=70:
  grade="C"
elif percentage>=60:
  grade="D"
else:
  grade="Fail"
print("\n-----RESULT-----")
print("Name:",name)
print("ROLL NO:",roll)
print("Total marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)