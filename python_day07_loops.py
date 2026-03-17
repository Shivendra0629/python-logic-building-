"""
Level 3: Mathematical & Logical Patterns

"""

#Question 1. Print the squares of numbers from 1 to n.

n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i*i)

#Question 2. Print cubes of numbers from 1 to n.

n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i*i*i)

#Question 3. Print all numbers between a and b divisible by 7.

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))

for i in range(a,b+1):
    if i%7==0:
        print(i)


# Question 4. Find HCF of two numbers using loops

a = int(input("Enter the value of no.1 : "))
b = int(input("Enter the value of no.2 : "))

factors_a = []
factors_b = []


for i in range(1, a + 1):
    if a % i == 0:
        factors_a.append(i)

for j in range(1, b + 1):
    if b % j == 0:
        factors_b.append(j)

print("Factors of", a, ":", factors_a)
print("Factors of", b, ":", factors_b)


cf = []
for i in factors_a:
    if i in factors_b:
        cf.append(i)

print("Common Factors :", cf)
print("HCF =", max(cf))

#Question 5. Find LCM of two numbers using loops. 

a = int(input("Enter the value of no.1 : "))
b = int(input("Enter the value of no.2 : "))
lcm=0
if a>b:
    lcm=a
else:
    lcm=b
while True :
    if lcm%a==0 and lcm%b==0:
        print(lcm)
        break
    lcm+=1

#Question 6. Print all factors of a given number.


a=int(input("Enter the value of no:"))
print("Factors of the given number are:")
for i in range(1,a+1):
    if a%i==0:
      print(i,end=' ')

#Question 7. Find the sum of all factors of a number.


a=int(input("Enter the value of no:"))
print("Factors of the given number are:")
sumoffactors=0
for i in range(1,a+1):
    if a%i==0:
      sumoffactors+=i
      print(i,end=' ')
print("\nsum of factors is ",sumoffactors)

#Question 8. Check if a number is a strong number (sum of factorials of digits = number).

a=int(input("Enter the value of no:"))
sumoffactorial=0
for digit in str(a):                     #Iterate over each digit 
     fact=1                              #  Resets for every digit
     for i in range(1,int(digit)+1):     # factorial of each digit
         fact*=i
     sumoffactorial+=fact                #Sum gets updated after each digits factorial is calculated. 

if sumoffactorial==a:                    # Checking condition
    print("The number is a strong number")
    
#Question 9. Print first n terms of an arithmetic progression (a, d).

a=int(input("Enter the value of n no of terms:"))
f_term=int(input("Enter the value of first term:"))
d=int(input("Enter the value of common difference:"))
print("The AP  is :")
for i in range(1,a+1):
    print(f_term,end=' ')
    f_term+=d
   
#Question 10. Print first n terms of a geometric progression (a, r).

a=int(input("Enter the value of n no of terms:"))
f_term=int(input("Enter the value of first term:"))
r=int(input("Enter the value of common ratio:"))

print("The GP  is :")
nx_term=f_term
for i in range(1,a+1):
    print( nx_term,end=' ')
    nx_term*=r
   
   
   