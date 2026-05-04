#1. Find the largest number among three integers.
'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>=b and a>=c:
    print("the largest number",a)
elif b>=a and b>=c:
    print("the largest number",b)
elif c>=a and c>=b:
    print("the largest number",c)
else:
    print("invalided")
'''
#2. Find the smallest number among three integers.
'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a<=b and a<=c:
    print("the smallest number",a)
elif b<=a and b<=c:
    print("the smallest number",b)
elif c<=a and c<=b:
    print("the smallest number",c)
else:
    print("invalided")
'''
#3. Check if a given number is greater than 0, if yes then print 'Positive'.
#If the given number is lesser than 0, then print 'Negative'. If the given number is exactly equal to 0, then print 'Zero'.
'''
a=int(input("Enter a number:"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
elif a>=0:
    print("Zero")
else:
    print("invalided")
'''
#4. Write a program that functions as a basic calculator.
#The program will prompt the user to input two numbers and a mathematical operation (+, -, x, /).
#It will then perform the selected operation and display the result on the screen.
'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
s=str(input("Enter a operators(+,-,*,/):"))
if s=='+':
    print(a+b)
elif s=='-':
    print(a-b)
elif s=='*':
    print(a*b)
elif s=='/':
    print(a/b)
else:
    print("invalided")
'''
#5. Check whether the given number is a multiple of 5, 3, and 7.
'''
a=int(input("Enter a number:"))
if a%5==0:
    print("multiple of 5")
elif a%3==0:
    print("multiple of 3")
elif a%7==0:
    print("multiple of 7")
else:
    print("invalided")
'''
#6. A library charges fine for books returned late. To calculate the fine, define a class Library with the following .
#To input the number of days books were returned late. To calculate and print the fine based on the following condition:
#a. First five days 40 paisa per day
#b. Six to ten days 65 paisa per day
#c. above 10 days 80 paisa per day
'''
a=int(input("number of days:"))
if a>=1 and a<=5:
    print("First five days 40 paisa per day")
elif a>=6 and a<=10:
    print("Six to ten days 65 paisa per day")
elif a>10:
    print("above 10 days 80 paisa per day")
else:
    print("invalided")
'''
#7.To input weight of the parcel and type of booking (`O' for ordinary and 'E' for express).
#To compute and display the charges based on the weight of the parcel as per the tariff given






















































    








































