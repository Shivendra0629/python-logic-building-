 
# Level 3: Math and Number Logic


# QUESTION 1: Take a 3-digit number and check if all digits are distinct.

a = input("Enter a 3-digit number: ")

if len(set(a)) == 3:
    print("Distinct Digits")
else:
    print("Digits are not distinct")

#OR
a = int(input("Enter a 3-digit number: "))

d1 = a // 100        # hundreds digit
d2 = (a // 10) % 10  # tens digit
d3 = a % 10          # units digit

if d1 != d2 and d1 != d3 and d2 != d3:
    print("Distinct Digits")
else:
    print("Digits are not distinct")



# QUESTION 2: Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.

a=int(input("Enter a 3-Digit number:"))


d1 = a // 100        #Hundreds digits
d2 = (a // 10) % 10  #Tens     digits
d3 = a % 10          #Units    digits 


if d2>d1 and d2>d3:
    print("Middle is the Largest.")
elif d2<d1 and d2<d3:
    print("Middle is the smallest.")
else:
    print("Either.")

# QUESTION 3:Take a 4-digit number and check if the first and last digits are equal. 

a=int(input("enter the 4-digit number:"))

d1=a//1000
d2=(a//100)%10
d3=(a//10)%10
d4=a%10

if (d1==d4):
    print("First and Last digits are equal")
else:
    print("Not equal")


# QUESTION 4: Check whether a given integer is single-digit, double-digit, or multi-digit.
a=abs(int(input("Enter a number:")))
b=str(a) 
if len(b)==1: 
    print("single digit") 
elif len(b)==2: 
    print("Double digit") 
else: 
    print("Multi digit") 

#OR

a = abs(int(input("Enter a number: ")))

if a < 10:
    print("Single digit")
elif a < 100:
    print("Double digit")
else:
    print("Multi digit")

#QUESTION 5: Check if a number is a multiple of 7 or ends with 7.

a=int(input("Enter a number:"))

if(a%7==0):
    print(a,"is a multuiple of 7.")
if(a%10==7):
    print("The digit ends with 7.")

#QUESTION 6:Take coordinates (x, y) and determine which quadrant the point lies in.
x=int(input("Enter the value of x-coordinate:"))
y=int(input("Enter the value of y-coordinate:"))

if (x>0 and y>0):
    print("Lies in the 1st Quadrant")
elif (x<0 and y>0):
    print("Lies in the 2nd Quadrant")
elif(x<0 and y<0):
    print("Lies in the 3 rd Quadrant")
elif (x>0 and y<0):
    print("Lies in the 4 th Quadrant")
else:
    print("Lies in the x axis or y axis.")

#QUESTION 7:Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.

amt=int(input("Enter the amount:"))
if amt%100==0:
    print("AMount can be divided into 2000,500 and 100 currency notes.")

#QUESTION 8: Check if a number lies within the range [100, 999].
num=int(input("enter a number:"))
if (num>=100 and num <=999):
    print("The  number lies within the range [100, 999]")

#QUESTION 9:Take two angles of a triangle and compute the third angle.

a1=int(input("Enter angle 1:"))
a2=int(input("Enter angle 2:"))
if a1>0 and a2>0 and (a1+a2<180):
    c=180-(a1+a2)
    print("The 3rd angle is:",c)
else:
    print("Enter valid sides!")

#QUESTION 10: Check whether a number is a perfect square (without using the square root function).



num= int(input("Enter a number: "))
flag=False 
if num%2==0:
    for i in range(2,num,2):
            if i*i==num:
                print(num,"is a perfect square of",i)
                flag=True
                break
else:
    for j in range(1,num,2):
            if j*j==num:
                print(num,"is a perfect square of",j)
                flag=True
                break
if flag==False:
    print(num,"is not a perfect square number.")


# OR

num= int(input("Enter a number: "))
for i in range(1,num+1):
   if i*i==num:
    print(num,"is a perfect square of",i)
    break
