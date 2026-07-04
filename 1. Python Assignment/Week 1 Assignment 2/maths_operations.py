#Math Operations
import math

# Question 1: Area of Triangle (Heron's Formula)
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of Triangle:", area)

# Question 2: Quotient and Remainder
num1 = 17
num2 = 5
print("Quotient:", num1 // num2)
print("Remainder:", num1 % num2)

# Question 3: Identity Matrix
n = 4
i = 1
print("Identity Matrix:")
while i <= n:
    j = 1
    while j <= n:
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
        j += 1
    print()
    i += 1

# Question 4: LCM of Two Numbers
x = 12
y = 18
lcm = (x * y) // math.gcd(x, y)
print("LCM:", lcm)

# Question 5: Sum of Natural Numbers
N = 10
i = 1
sum_n = 0
while i <= N:
    sum_n += i
    i += 1
print("Sum of Natural Numbers:", sum_n)

# Question 6: Amicable Numbers Check
num1 = 220
num2 = 284
i = 1
sum1 = 0
sum2 = 0
while i < num1:
    if num1 % i == 0:
        sum1 += i
    i += 1
i = 1
while i < num2:
    if num2 % i == 0:
        sum2 += i
    i += 1
if sum1 == num2 and sum2 == num1:
    print("Amicable Numbers: Yes")
else:
    print("Amicable Numbers: No")

# Question 7: Perfect Squares (digit sum < 10)
start = 1
end = 100
i = 1
print("Perfect Squares (digit sum < 10):")
while i * i <= end:
    square = i * i
    if square >= start:
        digit_sum = 0
        temp = square
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        if digit_sum < 10:
            print(square)
    i += 1

# Question 8: Armstrong Number Check
num = 153
temp = num
digits = len(str(num))
armstrong_sum = 0
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** digits
    temp //= 10
if armstrong_sum == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")