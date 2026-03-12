# Phase 1 – Conditional Thinking (If–Else, Boolean Logic)

#QUESTION 1: Check if a given year is a leap year.     

a=int(input("Enter the year:"))
if( a%4==0 and a%100!=0):
    print("Lear year")
elif (a%400==0): 
    print("leap year")
else:
    print("not a leap year")

#QUESTION 2:Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

    b=int(input("Enter the temp :"))
    if (b<28 and b>=10):
        print("Warm")
    elif (b<10):
        print("Cold")
    else:
        print("Hot")

# QUESTION 3: Take a character and check whether it’s uppercase, lowercase, a digit, or a special character

str=input("Enter a character :")
if (str>='A' and str<='Z'):
    print("Uppercase")
elif (str>='a' and str<='z'):
    print("Lowercase")
elif (str>='0'and str<='9'):
    print("digit")
else:
    print("Special character")

# OR

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")