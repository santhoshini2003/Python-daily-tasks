#11.Write a program to accept two numbers, subtract the two numbers and check if the difference (answer) is 0 or not
'''
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
if a-b==0:
    print("The difference is 0")
else:
    print("The difference is not 0")
'''
#12.Write a program to read the Computer Science marks of a student and print if the student has passed or failed.
#The student has passed if marks is 50 or above otherwise failed).
'''
student = int(input("Enter a computer science mark:"))
if student>=50:
    print("passed")
else:
    print("failed")
'''
#13.Write a program to accept a number and check if the number is divisible by 10.
'''
a = int(input("Enter a number:"))
if a%10==0:
    print("number is divisible by 10")
else:
    print("number is not divisible by 10")
'''
#14.Write a program to take a two-digit number and print the biggest digit.
'''
num = int(input("Enter a two digit number:"))
digit1=num//10
digit2=num%10
if digit1>digit2:
    print("the biggest digit is digit1", digit1)
else:
    print("the biggest digit is digit2", digit2)
'''
#15.Write a program to accept the choice from the user.
#If the choice is 1 print “The exam will be easy”, otherwise print “The exam will be difficult”.
'''
choice=int(input("Enter the choice:"))
if choice==1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")
'''
#16.Write a program to accept a value from the user.
#If the value entered is 1 then print “You can go out and play” otherwise “You cannot go out and play”
'''
value=int(input("Enter the value:"))
if value==1:
    print("You can go out and play")
else:
    print("You cannot go out and play")
'''
#17.Write a program to accept the length and breadth of a shape and print if they are the same.
#If they are the same, print it’s a square otherwise its rectangle.
'''
length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
if length==breadth:
    print("it's a square")
else:
    print("its rectangle")
'''
#18.Check if a given number is the ASCII value of an uppercase alphabet or not.
'''
num=int(input("Enter a number:"))
if 65<=num<=90:
    print("uppercase alphabet")
else:
    print("is not a uppercase alphabet")
'''    
#19.Check if a given number is the ASCII value of a lowercase alphabet.
'''
n=(input("Enter a number:"))
if 97<=n<=122:
    print("lowercase alphabet")
else:
    print("is not a lowercase alphabet")
'''
#20.Check if a given number is the ASCII value of a numeric character or not.
'''
n=int(input("Enter a number:"))
if 48<=n<=57:
    print("numeric character")
else:
    print("is not a numeric character")
'''
#21.Check whether the given number is a multiple of both 5 and 3.
'''
n=int(input("Enter a number:"))
if n%5==0 and n%3==0:
    print("is multiple of both 5 and 3")
else:
    print("is not multiple of both 5 and 3")
'''
#22.Check if a given number is a three-digit number and also a multiple of 10.
'''
n=int(input("Enter a three digit:"))
if 100<=n<=999 and n%10==0:
    print("is a three-digit number and also multiple of 10")
else:
    print("is not  a three-digit number and also not multiple of 10")
'''
#23.Check if a given number is a three-digit number and also a multiple of 2, 5, and 10.
'''
n=int(input("Enter a three digit:"))
if 100<=n<=999 and n%2==0 and n%5==0 and n%10:
    print("is a three-digit number and also multiple of 2, 5 and 10")
else:
    print("is not a three-digit number and also not multiple of 2, 5 and 10")
'''
#24.Check the given two integer inputs. If both numbers are even, find their product. Otherwise, find their sum.
'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if a%2==0 and b%2==0:
    print("if both number are even", a*b)
else:
    print("if both number are not even", a+b)
'''
#25.A number is said to be Buzz Number if it ends with 7 or is divisible by 7.
#Example: 1007 is a Buzz Number. Define a class Buzz number to read a number and check if it is a Buzz number or not.
'''
a=int(input("Enter a number:"))
digit=a%10
if digit==7 or a%7==0:
    print("its a Buzz number")
else:
    print("its not a Buzz number")
'''






































































