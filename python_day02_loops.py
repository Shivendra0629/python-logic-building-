# Level 2: Nested If & Multiple Conditions

#QUESTION 1: (a)Take three sides and check if they form a valid triangle. 
#            (b) If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.

a=int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(input("enter side 3:"))
if (a>0 and b>0 and c>0) and (a+b>c and b+c>a and a+c>b):
    print("triangle")
    if(a==b and b==c):
        print("equilateral triangle")
    elif(a==b and a!=c ):
        print("Isosceles triangle")
    else:
        print("scalene traingle")
else:
    print("Not a triangle")

# QUESTION 2: Check if one of two given numbers is a multiple of the other.   



def check(a,b):
    if (b!=0 and a%b==0):
        print(a," is a multiple of ",b)
    elif (a!=0 and b%a==0):
        print(b," is a multiple of ",a)
    else:
        print("Both are not a multiple of each other")


check(a=int(input("enter no 1:")),b=int(input("enter no 2:")))

# QUESTION 3: Take a month number (1–12) and print the number of days in that month (add leap year conditions).  

def Calendar(a):
    
    if (a==1):
        print("31 DAYS")
    elif (a==2) :
        year=int(input("Enter a year:"))
        if( year%4==0 and year%100!=0):
            print("28 days")
        elif (year%400==0):
            print("28 days")
        else:
            print("27 Days")
    elif (a==3) :
        print("30 days")
    elif (a==4) :
        print("31 days")
    elif (a==5) :
        print("30 days")
    elif (a==6) :
        print("31 days")
    elif (a==7) :
        print("30 days")
    elif (a==8) :
        print("31 days")
    elif (a==9) :
        print("30 days")
    elif (a==10) :
        print("31 days")
    elif (a==11) :
        print("31 days")
    elif (a==12) :
        print("30 days")
    else:
        print("Enter a valid month(1-12)!")

Calendar(a=int(input("Enter a month (1-12):")))


#OR
def Calendar(a):
    if a in [1,3,5,7,8,10,12]:
        print("31 days")
    elif a in [4,6,9,11]:
        print("30 days")
    elif a == 2:
        print("28 days")
    else:
        print("Enter a valid month (1-12)")

Calendar(int(input("Enter a month (1-12): ")))