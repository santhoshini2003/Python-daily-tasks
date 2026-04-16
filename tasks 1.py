#Write a Program to Swap Two Variables  [using third variable , without using third variable]
'''
a=10
b=20
#swap two variables using third variable
temp=a
a=b
b=temp
print(a)
print(b)
#without using third variable
a=a+b
b=a-b
a=a-b
print("a:",a)
print("b:",b)
'''


#Write a Program to Convert Kilometers to Miles [ 1km = 0.63 miles ]
'''
km=float(input("Enter a distance of km:"))
miles=km*0.63
print("Enter a distance of miles:", miles)
'''


#Write a Program to Convert Celsius To Fahrenheit [ formula = (Celsius x 1.8) + 32]
'''
c=float(input("Enter a celsius:"))
f=c*1.8
d=f+32
print("Enter a fahrenheit:", d)
'''


#Write a program to find last digit of the number
'''
num=int(input("Enter a number:"))
last_digit=num%10
print("Enter a last digit number:", last_digit)
'''


#Write a program to find last two digit of the number
'''
num=int(input("Enter a number:"))
last_two_digit=num%100
print("Enter a last two digit of number:", last_two_digit)
'''

'''
Write a program to take a five-digit number as input, square the middle digit and print number and the square.
Input Data:
Input an integer: 54623
Expected Output
Square of 6 is: 36

num=input("Input an integer:")
md=int(num[2])
square=md**2
print("Square of", md, "is:", square)
'''