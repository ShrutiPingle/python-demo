# a= int(input('enter a number to check if it is even '))
# c= a%2!=0
# print(f"number is odd : {c}")

# age= int(input('enter your age to check how many days you have been on earth '))
# print(f"{age} years = {age*365} days")

# min= int(input('enter minutes to check in hours '))
# print(f"{min} is {min//60} hours {min%60} minutes")

# num= int(input('enter number for its last digit '))
# print(f"{num} : last digit is {num%10}")

# role = input('enter role ')
# age2 = int(input('enter age '))
# print(f"Eligible : {'student'==role and age2 >=21}")

# swap
# a=10
# b=20
# print(f"a={a} and b={b}")
# b=a=b
# print(f"a={a} and b={b}")

 #dhinka chika
# day= int(input("enter a no. bet 1 to 7 for day"))

# match day:
#   case 1:
#     print("mon")
#   case 2:
#     print("tue")
#   case 3:
#     print("wed")
#   case 4:
#     print("thur")
#   case 5:
#     print("fri")
#   case 6:
#     print("sat")
#   case 7:
#     print("sun")
#   case _:
#     print("invalid number")

# num1= int(input("enter number "))
# if num1%2==0:
#   print(f"{num1} is even")
# else :
#   print(f"{num1} is odd")

# age1= int(input("enter age for ticket discount "))
# price=100
# if age1<12:
#   print(f"your age is {age1} ticket price is {price} after discount you will have to pay {price-(price/10)}")
# else :
#   print(f"your age is {age1} ticket price is {price}")

# marks= int(input("enter marks out of 100 : "))
# if marks>=90 and marks<=100:
#   print("O")
# elif marks >=80 and marks <90:
#   print("A")
# elif marks >=65 and marks <80:
#   print("B")
# elif marks >=35 and marks <65:
#   print("C")
# elif marks<35 and marks>=0:
#   print("FAIL")
# else:
#   print("invalid marks , enter only upto 100")

# num3= int(input("enter integer for positive or negative: "))
# if num3>0 :
#   print("integer is positive")
# elif num3==0:
#   print(" 0 is neither positive or negative")
# else :
#   print("integer is negative")

# n1=int(input("enter n1: "))
# n2=int(input("enter n2: "))
# n3=int(input("enter n3: "))
# if n1>n2 and n1>n3:
#   print(f"{n1} is greater")
# elif n2>n1 and n2>n3:
#   print(f"{n2} is greater")
# else :
#   print(f"{n3} is greater")

# year= int(input("enter year: "))
# if year%4==0 or year%400==0:
#   print(f"{year} is a leap year")
# else: 
#   print(f"{year} is NOT a leap year")

numA=int(input("enter no.1 "))
numB=int(input("enter no.2 "))
calc=input("enter action; add, sub, div, mul: ")
match calc:
  case 'add':
    print(f"{numA} + {numB} = {numA+numB}")
  case 'sub':
    print(f"{numA} - {numB} = {numA-numB}")
  case 'div':
    if numB!=0:
      print(f"{numA} / {numB} = {numA/numB}")
    else:
      print(f"0 cannot divide {numA}")
  case 'mul':
    print(f"{numA} x {numB} = {numA*numB}")
  case _:
    print("invalid action")