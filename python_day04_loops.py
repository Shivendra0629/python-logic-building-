
# Level 4: Logical Operators & Compound Statements



#QUESTION 1: Take a character and check if it is a letter, a digit, or neither.

ch=input("Enter a character:")

if ch>='A' and ch<='Z' and ch>='a' and ch<='z':
    print("letter")
elif ch>='0' and ch<='9':
    print("Digit")
else:
    print("Neither letter nor digit") 

#OR
ch = input("Enter a character: ")

if ch.isalpha():
    print("Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Neither letter nor digit")

#QUESTION 2: Take three numbers and print the median value (neither maximum nor minimum). 


a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))

if (a > b and a < c) or (a > c and a < b):
    print("Median:", a)
elif (b > a and b < c) or (b > c and b < a):
    print("Median:", b)
else:
    print("Median:", c)

#OR
a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))

nums = [a, b, c]
nums.sort()

print("Median:", nums[1])

#QUESTION 3: Take 24-hour time (hours and minutes) and print whether it is AM or PM.
time= int(input("Enter time in 24-hour:"))

if time>0 and time <12:
    print("AM")
elif time >=12 and time <=24:
    print("PM")
else:
    print("Invalid!")

#QUESTION 4:Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

income =int(input("Enter your income in Lakh:"))
age=int(input("Enter your age:"))
if  (age > 18 and income > 5):
    print("Eligible for tax")
else:
    print("Not eligible for tax paying.")

# QUESTION 5:Take a single digit (0–9) and print its word form (“Zero” to “Nine”).

digit =int(input("Enter a digit(0-9):"))

if digit==0:
    print("Zero")
elif digit==1:
    print("One")
elif digit==2:
    print("Two")
elif digit==3:
    print("Three")
elif digit==4:
    print("Four")
elif digit==5:
    print("Five")
elif digit==6:
    print("Six")
elif digit==7:
    print("Seven")
elif digit==8:
    print("Eight")
else:
    print("Nine")


#QUESTION 6: Take a weekday number (1–7) and determine if it is a weekday or weekend. 

dayno= int(input("enter a weekday number(1-7):"))

if dayno>=1 and  dayno<=5:
    print("WEEKDAY")
else:
    print("Weekend")

#QUESTION 7: Take a password string and check basic rules (length ≥ 8 and contains at least one digit)

password=(input("Enter you password:"))
flag=False
for i in password:
    if i.isdigit():
        flag=True
if len(password)>=8 and flag==True:
    print("Password is ok contains (length ≥ 8 and contains at least one digit).\nYour passowrd is:",password)


