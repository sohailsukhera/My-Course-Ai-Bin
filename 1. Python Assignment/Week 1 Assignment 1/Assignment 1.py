# Question 1: Convert Celsius to Fahrenheit
celsius=float(input("Enter temperature in Celsius:"))
fahrenheit=(celsius*9/5)+32
print("Fahrenheit:",fahrenheit)

# Question 2: Calculate Area of Rectangle
length=float(input("Enter length:"))
width=float(input("Enter width:"))
print("Area:",length*width)

# Question 3: Calculate Compound Interest
p=float(input("Principal:"))
r=float(input("Rate:"))
t=float(input("Time:"))
ci=p*(1+r/100)**t-p
print("Compound Interest:",ci)

# Question 4: Calculate Perimeter of Rectangle
length=float(input("Length:"))
width=float(input("Width:"))
print("Perimeter:",2*(length+width))

# Question 5: Calculate Average of Three Numbers
a=float(input("Num 1:"))
b=float(input("Num 2:"))
c=float(input("Num 3:"))
print("Average:",(a+b+c)/3)

# Question 6: Calculate Square and Cube of a Number
num=float(input("Enter number:"))
print("Square:",num**2)
print("Cube:",num**3)

# Question 7: Calculate Distribution of Candies
candies=int(input("Candies:"))
students=int(input("Students:"))
print("Each gets:",candies//students)
print("Left:",candies%students)

# Question 8: Calculate Profit or Loss
cp=float(input("Cost Price:"))
sp=float(input("Selling Price:"))
if sp>cp:
    print("Profit:",sp-cp)
elif cp>sp:
    print("Loss:",cp-sp)
else:
    print("No Profit No Loss")

# Question 9: Calculate Marks and Percentage
total=0
for i in range(5):
    total+=float(input("Enter marks:"))
print("Total:",total)
print("Average:",total/5)
print("Percentage:",(total/500)*100)

# Question 10: Calculate Salary
basic=float(input("Basic Salary:"))
hra=0.20*basic
da=0.15*basic
print("Total Salary:",basic+hra+da)

# Question 11: Calculate Age in Months and Days
years=int(input("Enter age in years:"))
print("Months:",years*12)
print("Days:",years*365)

# Question 12: Convert USD to PKR
usd=float(input("USD:"))
print("PKR:",usd*280)

# Question 13: Calculate Sum of First N Natural Numbers
n=int(input("Enter N:"))
print("Sum:",n*(n+1)/2)

# Question 14: Calculate Percentage of Correct Answers
total_q=int(input("Total Questions:"))
correct=int(input("Correct Answers:"))
print("Percentage:",(correct/total_q)*100)

# Question 15: Calculate Speed
distance=float(input("Distance:"))
time=float(input("Time:"))
print("Speed:",distance/time)

# Question 16: BMI Calculator
weight=float(input("Weight(kg):"))
height=float(input("Height(m):"))
bmi=weight/(height**2)
print("BMI:",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal")
else:
    print("Overweight")

# Question 17: Convert Minutes to Hours
minutes=int(input("Minutes:"))
print("Hours:",minutes//60)
print("Minutes:",minutes%60)