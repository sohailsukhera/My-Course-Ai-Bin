# List Manipulation

# Question 1: Reverse list
numbers=[10,20,30,40,50]
numbers.reverse()
print("Reversed List:",numbers)

# Question 2: Square of list items
numbers=[1,2,3,4,5]
squares=[]
for num in numbers:
    squares.append(num**2)
print("Squared List:",squares)

# Question 3: Remove empty strings
strings=["Ali","","Ahmed","","Sara","Zain"]
new_list=[]
for item in strings:
    if item!="":
        new_list.append(item)
print("Cleaned List:",new_list)

# Question 4: Insert item after specific item
colors=["Red","Blue","Green"]
i=colors.index("Blue")
colors.insert(i+1,"Yellow")
print("Updated List:",colors)

# Question 5: Replace item in list
fruits=["Apple","Banana","Mango"]
if "Banana" in fruits:
    i=fruits.index("Banana")
    fruits[i]="Orange"
print("Updated Fruits:",fruits)


# ASSIGNMENT 3 LIST PROGRAMS

# 1. Find Largest Number
numbers = [12, 45, 7, 89, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest:", largest)

# 2. Find Second Largest Number
numbers = [12, 45, 7, 89, 34]
largest = second = -99999
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second Largest:", second)

# 3. Find Largest Even and Odd Number
numbers = [11, 22, 33, 44, 55]
largest_even = 0
largest_odd = 0
for num in numbers:
    if num % 2 == 0:
        if num > largest_even:
            largest_even = num
    else:
        if num > largest_odd:
            largest_odd = num
print("Largest Even:", largest_even)
print("Largest Odd:", largest_odd)

# 4. Find Average of List
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average:", average)

# 5. Count Occurrences of Element
numbers = [1, 2, 3, 2, 4, 2]
search = 2
count = 0
for num in numbers:
    if num == search:
        count += 1
print(count)

# 6. Remove Duplicates from List
numbers = [1, 2, 2, 3, 4, 4]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

# 7. Find Odd Occurring Element
numbers = [1, 2, 3, 2, 3, 1, 3]
for num in numbers:
    if numbers.count(num) % 2 != 0:
        print(num)
        break

# 8. Find Union of Two Lists
list1 = [1, 2, 3]
list2 = [3, 4, 5]
union = list(set(list1 + list2))
print(union)

# 9. Swap First and Last Element
numbers = [10, 20, 30, 40]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

# 10. Find Longest Word
words = ["apple", "banana", "watermelon"]
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)

# 11. Generate Random Numbers
import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 20))
print(numbers)