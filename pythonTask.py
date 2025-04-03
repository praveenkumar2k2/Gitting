# 1) String function
'''
txt = "have a Good Day"
print(txt.capitalize())
print(txt.casefold())
print(txt.center(2))
print(txt.count("hello"))
print(txt.title())
print(txt.upper())
print(txt.lower())
print(txt[::-1])
print(txt.replace("Day","life"))
print(txt.split())
print(txt.find("G"))
'''

# 2) List function
'''
fruits = ['mango','cherry','apple', 'banana']

print(fruits.append("orange"))
print(fruits.clear())
print(x = fruits.copy())
x = fruits.count("apple")
fruits.pop(0)
fruits.remove("banana")
fruits.reverse()
fruits.sort()

print(fruits)
'''

# Tuple 
'''''
tup = (1, 2, 3, 4, 5)

print(tup[0])
print(tup[1:4])
print(len(tup))

# Tuple unpacking
a, b, c, d, e = tup
print(a, b, c, d, e)
'''''

# 4. Grading System
'''
marks = int(input("Enter marks: "))

if marks>=90 and marks<=100:
    print("Grade A")
elif marks >=80 and marks <= 90:
    print("Grade B")
elif marks>=70 and  marks <= 80:
    print("Grade C")
else:
    print("Fail")
'''

#Reverse a string
'''
a=input("enter a string: ")
print(a[::-1])
'''

#check for palindrome
'''
s =input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome") 
    '''
# Fibonacci series
'''
n=int(input())
a=0
b=1
while n>0:
    print(a)
    c=a+b
    b=a
    a=c
    n=n-1
'''
#even or odd
'''
n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")
    
'''
# Get a Number and Check if Prime
'''
def is_prime(n):
    if n < 2:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
    return True  
# Take input from user
num = int(input("Enter a number: "))

# Check if prime
if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is NOT a Prime Number")
'''

#  Replace Even Numbers with '@'
'''
for i in range(1,101):
    if(i%2 ==0):
        print("@")
    else:
        print(i)
    '''
    
# Iterate Over Collection and Square Each Element
'''
a=[1,2,3,4,5,6,7]

for i in a:
    print(i**2)
'''

#Getting Values using Keys in Dictionary
'''
a={"a":210,"b":32,"c":33,"d":34}
for i in a.keys():
    print(a[i])
    '''
    
    # Get User Details and Display
'''
def get_user_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

def display_user_details(details):
    print(f"Name: {details[0]}, Age: {details[1]}")

user_details = get_user_details()
display_user_details(user_details)
'''

# calculator
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:  # Prevent division by zero
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operator!"

# Take input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Call function and display result
result = calculate(num1, num2, operator)
print("Result:", result)
