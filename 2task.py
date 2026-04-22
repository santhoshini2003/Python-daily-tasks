#1. Write a program to find the smallest number among two given integers.
'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if a<b:
    print("a is smallest number")
else:
    print("b is smallest number")
'''
#2. Write a program to find the largest number among two given integers.
'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if a>b:
    print("a is largest number")
else:
    print("b is largest number")
'''
#3. Write a program to find the absolute value of a given integer.
'''
num=int(input("Enter a number:"))
if num%2==0:
    absolute_value=num
else:
    absolute_value=-num
    print("Absolute value:", absolute_value )
'''    
#4. Check if a given number is even number or odd number
'''
num=int(input("Enter a number:"))
if num%2==0:
    print("even number")
else:
    print("odd number")
'''
#5. Determine whether the given number is a multiple of 5 or not.
'''
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("is a multiple of 5")
else:
    print("is not a multiple of 5")
'''

#6. Determine whether the given number is a multiple of 10 or not.
'''
num = int(input("Enter a number: "))

if num % 10 == 0:
    print("is a multiple of 10")
else:
    print("is not a multiple of 10")
'''    

#7. Check whether the given number is a two-digit number or not.
'''
num=int(input("Enter a number:"))
if 10<=num<=99 or -99<=num<=-10:
    print("number is a two-digit")
else:
    print("number is not a two-digit")
'''

#8. Check whether the given number is a three-digit number or not.
'''
num=int(input("Enter a number:"))
if 100<=num<=999 or -999<=num<=-100:
    print("number is a three-digit")
else:
    print("number is not a three-digit")
'''
#9. Check if a given number ends with zero or not.
'''
num=int(input("Enter a number:"))
if num%10==0:
    print("number ends with zero")
else:
    print("number not ends with zero")
'''
#10.Write a program to accept a number and check if its square is above 50 or below 50.
'''
num=int(input("Enter a number:"))
square=num**2
if num>50:
    print("true")
else:
    print("false")
'''










    













