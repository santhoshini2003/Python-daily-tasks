'''
#1. Write a program to print the first N natural numbers.
#Input : 10 , Output : 1 2 3 4 5 6 7 8 9 10
n=int(input("Enter the number:"))
for i in range(1,n+1,1):
    print(i,end=" ")

#2. Write a program to print the first N even natural numbers.
#Input : 5 , Output 2 4 6 8 10
n=int(input("Enter the number:"))
for i in range(2,2*n+1,1):
    if i%2==0:
     print(i)

#3. Write a program to print the first N odd natural numbers.
#Input : 5 , Output : 1 3 5 7 9    
n=int(input("Enter the number:"))
for i in range(1,n*2,2):
    if i%2==1:
     print(i,end=" ")

#4. Write a program to print first N multiples of 3.
#Input : 7 , Output : 3 6 9 12 15 18 21
n=int(input("Enter the number:"))
for i in range(3,n*3+1,1):
     if i%3==0:
         print(i,end=" ")

#5. Write a program to print first N multiples of 5.
#Input : 5 , Output : 5 10 15 20 25
n=int(input("Enter the number:"))
for i in range(5,n*5+1,1):
     if i%5==0:
         print(i,end=" ")

#6. Write a program to print all the multiples of 2 till N.
#Input : 15 , Output : 2 4 6 8 10 12 14
n=int(input("Enter the number:"))
for i in range(2,n*1,2):
     if i%2==0:
         print(i,end=" ")

#7. Write a program to print all the numbers which are multiples of either 2 or 3 till N.
#Input : 15 , Output : 2 3 4 6 8 9 10 12 14 15
n=int(input("Enter the number:"))
for i in range(2,n+1,1):
     if i%2==0 or i%3==0:
         print(i,end=" ")

#8. Write a program to print all the numbers which are multiples of either 2, 5 or 7 till N.
#Input : 15 , Output : 2 4 5 6 7 8 10 12 14 15
n=int(input("Enter the number:"))
for i in range(2,n+2,1):
     if i%2==0 or i%5==0 or i%7==0:
         print(i,end=" ")

#10. Find the sum of all digits in a positive integer.
#Input : 123456789 , Output : 45
n=int(input("Enter the number:"))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
    print(s)

#11. Count the number of digits in a positive integer.
#Input : 123456789 , Output : 9
n=int(input("Enter the number:"))
c=0
while n>0:
    n=n//10
    c=c+1
    print(c)

#12. Write a program to find factors of a given number.
#Input : 20 , Output : 1 2 4 5 10 20
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)

#13. Write a program to count factors of a given number.
#Input : 20 , Output : 6
n=int(input("Enter the number:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
       print(c)

#14. Write a program to find whether the given number is a prime number or not.
#I nput : 11 , Output : Yes
n=int(input("Enter the number:"))
if n>1:
    for i in range(2,n):
        if n%1==0:
            print("yes")
            break

        else:
            print("not")
else:
    print("not")

#16. Write a program to find the greatest common factor of given 2 integers.
#Input : 10 20 , Output : 10
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
gcf=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcf=i
print("Enter the greatest common factor:",gcf)       

#17. Print the common factors of two positive integers n and m.
#Input : 8 12 , Output : 1 2 4    
n=int(input("Enter the number:"))
m=int(input("Enter the number:"))
for i in range(1,min(n,m)+1):
    if n%i==0 and m%i==0:
        print("the common factors:",i)

#20. Write a program that reads a set of integers, and then prints the sum of the even and odd integers.
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
even_sum=0
odd_sum=0
if a%2==0:
    even_sum+=1
else:
    odd_sum+=1

if a%2==0:
     even_sum+=1
else:
    odd_sum+=1
print("sum of the even:",even_sum)
print("sum of the odd:",odd_sum)

'''






        




























    
       









































         

























        
