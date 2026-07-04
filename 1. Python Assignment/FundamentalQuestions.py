# Part 1: Input & Output Functions
# Question 1: Print Hello World and Your Name
print("Hello, World!")
print("Your Name")

# Question 2: Favorite Color
color = input("Enter your favorite color: ")
print("Your favorite color is", color)

# Question 3: Print Three Words with Hyphen
print("Python", "Programming", "Fun", sep="-")

# Question 4: Calculate Age
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print("Your age is:", age)

# Question 5: Print Sum
print("The sum of 5 and 5 is", 5 + 5)

# Question 6: Use end Parameter
print("Hello", end=" ")
print("World")

# Question 7: Join Two Strings
a = input("Enter first string: ")
b = input("Enter second string: ")
print(a + b)

# Question 8: Greeting in Uppercase
name = input("Enter your name: ")
print(("Welcome, " + name + "!").upper())

# Question 9: City and Country
city = input("Enter city: ")
country = input("Enter country: ")
print(city + ", " + country)

# Question 10: Fix String + Integer
age = 20
print("Age is " + str(age))


# Part 2: Variables & Data Types

# Question 11: Integer and Float
age = 20
height = 5.8
print(type(age))
print(type(height))

# Question 12: Complex Number
num = 3 + 4j
print(num)
print(type(num))

# Question 13: Boolean Variable
is_python_fun = True
print(is_python_fun)

# Question 14: Multiple Assignment
a, b, c = 10, 20, 30
print(a, b, c)

# Question 15: Same Value Assignment
x = y = z = 100
print(x, y, z)

# Question 16: Convert Input to Float
num = float(input("Enter a number: "))
print(num)

# Question 17: Convert String to Integer
num = int("100")
print(num)

# Question 18: Real Part of Complex Number
c = 5 + 8j
print(c.real)

# Question 19: Length of Paragraph
text = "Python is easy to learn and very powerful."
print(len(text))

# Question 20: Swap Two Variables
a = 10
b = 20

a, b = b, a

print(a)
print(b)


# Part 3: Arithmetic Operators

# Question 21: Area of Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("Area:", length * width)

# Question 22: Power
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a ** b)

# Question 23: Division and Floor Division
print(10 / 3)
print(10 // 3)

# Question 24: Modulus
print(25 % 4)

# Question 25: Average of Five Numbers
total = 0

for i in range(5):
    total += float(input("Enter number: "))

print("Average:", total / 5)

# Question 26: Minutes to Hours
minutes = int(input("Enter minutes: "))
print("Hours:", minutes // 60)
print("Remaining Minutes:", minutes % 60)

# Question 27: Area of Circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print(area)

# Question 28: Cube of Number
num = int(input("Enter number: "))
print(num ** 3)

# Question 29: PEMDAS
print(10 + 5 * 2)
print((10 + 5) * 2)

# Question 30: Simple Interest
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
si = (p * r * t) / 100
print(si)


# Part 4: Comparison & Logical Operators

# Question 31: Compare Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a > b)

# Question 32: Even Number
num = int(input("Enter number: "))
print(num % 2 == 0)

# Question 33: Between 10 and 50
num = int(input("Enter number: "))
print(num >= 10 and num <= 50)

# Question 34: Check String
text = input("Enter text: ")
print(text == "Python")

# Question 35: Admin or Superuser
user = input("Enter user: ")
print(user == "Admin" or user == "Superuser")

# Question 36: not Operator
flag = True
print(not flag)

# Question 37: Floating Point Comparison
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

# Question 38: Check NOT Under 18
age = int(input("Enter age: "))
print(not(age < 18))

# Question 39: Positive and Odd
num = int(input("Enter number: "))
print(num > 0 and num % 2 != 0)

# Question 40: Compare String Lengths
a = input("Enter first string: ")
b = input("Enter second string: ")
print(len(a) == len(b))


# Part 5: Assignment Operators

# Question 41: Add 5 using +=
x = 10
x += 5
print(x)

# Question 42: Subtract 3 using -=
price = 100
price -= 3
print(price)

# Question 43: Multiply by 2 using *=
balance = 50
balance *= 2
print(balance)

# Question 44: Divide by 4 using /=
total = 100
total /= 4
print(total)

# Question 45: Square using **=
num = 6
num **= 2
print(num)

# Question 46: Increment Counter
counter = 0
counter += 1
print(counter)

# Question 47: Find Remainder using %=
num = 15
num %= 2
print(num)

# Question 48: Floor Divide using //=
num = 17
num //= 3
print(num)

# Question 49: Convert 2 into 20
n = 2
n *= 5
n *= 2
n += 0
print(n)