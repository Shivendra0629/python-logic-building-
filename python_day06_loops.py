"""
PHASE 2 — LOOPING & PATTERNS (ITERATION & FLOW)

 Level 1: Basic Looping (Introductory)
1. Print numbers from 1 to 10.
2. Print all even numbers between 1 and 100.
3. Print all odd numbers between 1 and 100.
4. Print numbers from 10 down to 1.
5. Print the table of a given number (n × 1 to n × 10).
6. Print the sum of first n natural numbers.
7. Print the sum of all even numbers up to n.
8. Print the sum of all odd numbers up to n.
9. Print the factorial of a given number.
10. Print the product of digits of a given number.

"""

#Question 1:- Print numbers from 1 to 10.

for i in range (1,11):
    print(i)

#Question 2:-  Print all even numbers between 1 and 100.

for i in range(2,100):
    if i %2==0:
        print(i)
       

#Question 3:-  Print all odd numbers between 1 and 100.

for i in range(2,100):
    if i %2!=0:
        print(i)
    
#Question 4:- 4. Print numbers from 10 down to 1.

for i in range(10,0):
        print(i)