# Level 5: Creative / Tricky Logical Scenarios


#QUESTION 1: Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin.
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
  
if x==0 and y==0:
    print("The coordinate lies at the origin.")
elif x==0:
    print("The point lies on the Y-axis.")
elif y==0:
   print("The point lies on the X-axis.")
else:
    print("The point does not lie on any axis.")

#QUESTION 2:Take three numbers and check if they can form a Pythagorean triplet.

a=int(input("Enter the value of 1st no:"))
b=int(input("Enter the value of 2nd no:"))
c=int(input("Enter the value of 3rd no:"))


if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a :
    print(" They  form a Pythagorean triplet.")
else:
    print("They can't form a Pythagorean triplet.")

#QUESTION 3: Take day and month and check if it forms a valid calendar date (ignoring leap years).

day=int(input("enter the value of day:"))
month=int(input("enter the value of month:"))

if (month ==2) and (day>=1 and day<=27):
    print("It forms a valid calendar date.")
elif month in (1,3,5,7,8,10,12) and day>=1 and day <=31 :
    print("It forms a valid calendar date.")
elif month in (4,6,9,11) and day>=1 and day <=30 :
    print("It forms a valid calendar date.")
else:
    print("It doesn't forms a valid calendar date.")

#QUESTION 4: Take time (hours and minutes) and print the smaller angle between the hour and minute hands.  CONCEPTUAL 

a= int(input("Enter hours:"))
b= int(input("Enter minutes:"))

hour_angle=30*a+0.5*b
minute_angle=6*b
ag=abs(hour_angle-minute_angle)

if ag>180:
    ag=360-ag
print("Smaller angle is:",ag)
"""
CODE EXPLANATION:- 
Step 1: Full circle of clock
A clock has 360° in a full circle.

Step 2: 12 hours on the clock
The hour hand completes 360° in 12 hours.
So movement per hour:
360∘÷12=30∘
360∘÷12=30∘
So hour hand moves 30° in 1 hour.

Step 3: 1 hour = 60 minutes
If the hour hand moves 30° in 60 minutes, then movement per minute is:
30∘÷60=0.5∘
So hour hand moves 0.5° every minute.
This finds minute hand angle.
Reason:
60 minutes = 360°
1 minute = 6°
Example
30 minutes
= 30 × 6 = 180°

"""


#QUESTION 5: Take three numbers and check if they are in arithmetic progression. 


a= int(input("Enter no 1:"))
b= int(input("Enter no 2:"))
c= int(input("Enter no 3:"))

if b-a==c-b:
    print("they are in arithmetic progression.")

#QUESTION 6: Take three numbers and check if they are in geometric progression.

a= int(input("Enter no 1:"))
b= int(input("Enter no 2:"))
c= int(input("Enter no 3:"))

if b/a==c/b:
    print("they are in geometric progression.")
else:
    print("They are not in geometric progression.")

#QUESTION 7: Take a 3-digit number and check if the sum of the first and last digit equals the middle digit.

a= int(input("Enter a three digit no:"))

a1=a//100
a2=(a//10)%10
a3=a%10

if a1+a3==a2:
    print(" The sum of the first and last digit equals the middle digit.")
else:
    print(" NO the sum of the first and last digit equals the middle digit.")

#QUESTION 8: Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits.

a=int(input("Enter an integer(1-9999)"))
d1=a//1000
d2=(a//100)%10
d3=(a//10)%10
d4=a%10

if len(str(a))==1:
    print("Sum of digits greater than product")
elif len(str(a))==2:
    if d3+d4>d3*d4:
        print("Sum of digits greater than product")
elif len(str(a))==3:
    if d2+d3+d4>d2*d3*d4:
        print("Sum of digits greater than product")
elif len(str(a))==4:
    if d1+d2+d3+d4 > d1*d2*d3*d4:
        print("Sum of digits greater than product")
else:
    print("NULL")

    # or

    a = int(input("Enter an integer (1-9999): "))

d1 = a // 1000
d2 = (a // 100) % 10
d3 = (a // 10) % 10
d4 = a % 10

sum_digits = d1 + d2 + d3 + d4
product_digits = d1 * d2 * d3 * d4

if sum_digits > product_digits:
    print("Sum of digits is greater than product of digits")
else:
    print("Sum of digits is NOT greater than product")

#QUESTION 9: Take two dates (day and month) and determine which one comes first in the calendar.

d1 =int(input("Enter date 1:"))
m1 = int(input("Enter month of date 1: "))
d2 =int(input("Enter date 2:") )
m2 = int(input("Enter month of date 2: "))
if m1>m2:
    print("D2 comes first.")
elif m1<m2:
    print("D1 comes first")
else:
    if d1>d2:
        print("D2 comes first.")
    elif d1==d2:
        print("both are same dates.")
    else:
        print("D1 comes first.")



#QUESTION 10: Take a year and print the corresponding century (e.g., “19th century”, “20th century”)


year = int(input("Enter year: "))

century = (year - 1) // 100 + 1   #Formula for century calculation.

print("Century is:", century)




