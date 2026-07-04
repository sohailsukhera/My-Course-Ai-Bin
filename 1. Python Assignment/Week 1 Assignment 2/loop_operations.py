# List Manipulation 

# Question 1: First 10 numbers
i=1
while i<=10:
    print(i)
    i+=1

# Question 2: Even numbers
n=int(input("Enter number:"))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i+=1

# Question 3: Odd numbers
n=int(input("Enter number:"))
i=1
while i<=n:
    if i%2!=0:
        print(i)
    i+=1

# Question 4: Prime numbers
n=int(input("Enter number:"))
num=2
while num<=n:
    prime=True
    i=2
    while i<num:
        if num%i==0:
            prime=False
            break
        i+=1
    if prime:
        print(num)
    num+=1

# Question 5: Multiplication table
num=int(input("Enter number:"))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1

# Loop Operations Assignment

import random
lst = [12, 45, 2, 89, 33, 67]

# Question 1: Largest number in list
largest = lst[0]
i = 1
while i<len(lst):
    if lst[i]>largest:
        largest=lst[i]
    i += 1
print("Largest number:", largest)

# Question 2: Second largest number
unique_lst=list(set(lst))
unique_lst.sort()
second_largest=unique_lst[-2]
print("Second largest number:", second_largest)

# Question 3: Largest Even and Largest Odd
i=0
largest_even=None
largest_odd=None
while i < len(lst):
    if lst[i] % 2 == 0:
        if largest_even is None or lst[i] > largest_even:
            largest_even = lst[i]
    else:
        if largest_odd is None or lst[i] > largest_odd:
            largest_odd = lst[i]
    i += 1
print("Largest Even:", largest_even)
print("Largest Odd:", largest_odd)

# Question 4: Average of list
i = 0
total = 0
while i < len(lst):
    total += lst[i]
    i += 1
average = total / len(lst)
print("Average:", average)

# Question 5: Count occurrences of an element
num = 45
i = 0
count = 0
while i < len(lst):
    if lst[i] == num:
        count += 1
    i += 1
print("Occurrences of", num, ":", count)

# Question 6: Remove duplicates
dup_list = [1, 2, 2, 3, 4, 4, 5]
no_duplicates = []
i = 0
while i < len(dup_list):
    if dup_list[i] not in no_duplicates:
        no_duplicates.append(dup_list[i])
    i += 1
print("Without duplicates:", no_duplicates)

# Question 7: Odd occurring number (XOR method)
arr = [1, 2, 3, 2, 3, 1, 3, 3, 3]
result = 0
i = 0
while i < len(arr):
    result = result ^ arr[i]
    i += 1
print("Odd occurring number:", result)

# Question 8: Union of two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
union = list(set(list1 + list2))
print("Union of lists:", union)

# Question 9: Swap first and last element
swap_list = [10, 20, 30, 40, 50]
temp = swap_list[0]
swap_list[0] = swap_list[-1]
swap_list[-1] = temp
print("\nAfter swap:", swap_list)

# Question 10: Longest word
words = ["algorithm", "data", "python", "intelligence", "AI"]
longest_word = words[0]
i = 1
while i < len(words):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]
    i += 1
print("Longest word:", longest_word)

# Question 11: Random numbers list (1 to 20)
n = 10
random_list = []
i = 0
while i < n:
    random_list.append(random.randint(1, 20))
    i += 1
print("Random list:", random_list)