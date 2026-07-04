# Part A - Python Lists

# Question 1: Squares of Even Numbers
result = []
for i in range(21):
    if i % 2 == 0:
        result.append(i * i)
print(result)

# Question 2: Sort Without Changing Original List
nums = [3, 1, 4, 1, 5, 9]
new_list = sorted(nums)
print(nums)
print(new_list)

# Question 3: Remove Duplicates
nums = [1,2,2,3,1,4]
new = []
for i in nums:
    if i not in new:
        new.append(i)
print(new)

# Question 4: Flatten Nested List
nested = [[1,2],[3,4],[5]]
flat = []
for sub in nested:
    for item in sub:
        flat.append(item)
print(flat)

# Question 5: Sort Names Ignore Case
names = ['alice','Bob','charlie','DAVID']
names.sort(key=str.lower)
print(names)

# Question 6: Replace Slice
a = [10,20,30,40,50,60]
a[2:5] = [100,200]
print(a)

# Question 7: Find All Indices
nums = [7,2,7,5,7]
for i in range(len(nums)):
    if nums[i] == 7:
        print(i)

# Question 8: Elements Appearing Once
nums = [1,2,2,3,4,4,5]
for i in nums:
    if nums.count(i) == 1:
        print(i)

# Question 9: Rotate Right
lst = [1,2,3,4]
lst = [lst[-1]] + lst[:-1]
print(lst)

# Question 10: Even and Odd Lists
nums = [1,2,3,4,5,6]
even = []
odd = []
for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

# Part B - Python Tuples

# Question 1: Convert List to Tuple and Unpack
lst = [1, 2, 3, 4]
t = tuple(lst)
a, b, c, d = t
print(a)
print(b)
print(c)
print(d)

# Question 2: Print Second Elements
t = (('a', 1), ('b', 2), ('c', 3))
second = []
for i in t:
    second.append(i[1])
print(second)

# Question 3: Return Sum, Minimum and Maximum
def calculate(nums):
    total = sum(nums)
    minimum = min(nums)
    maximum = max(nums)
    return total, minimum, maximum
s, mn, mx = calculate([5, 8, 2, 9])
print("Sum:", s)
print("Min:", mn)
print("Max:", mx)

# Question 4: Combine Tuples and Convert to List
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(list(t3))

# Question 5: Highest Frequency Element
t = (1, 2, 2, 3, 2, 4)
highest = t[0]
for i in t:
    if t.count(i) > t.count(highest):
        highest = i
print(highest)

# Question 6: Check Same Elements
t1 = (3, 2, 1)
t2 = (1, 2, 3)
print(sorted(t1) == sorted(t2))

# Question 7: Last Three Elements
t = (1, 2, 3, 4, 5, 6)
print(t[-3:])

# Question 8: Repeat Tuple Three Times
t = (1, 2)
print(t * 3)

# Question 9: Flatten Nested Tuple
nested = ((1, 2), (3, 4))
flat = ()
for group in nested:
    flat = flat + group
print(flat)

# Question 10: Manhattan Distance
p1 = (2, 3)
p2 = (5, 8)
distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print(distance)


# Part C - Python Sets

# Question 1: Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
print(set1 - set2)

# Question 2: Common Elements
a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 4, 5}
print(a & b & c)

# Question 3: Unique Words
sentence = "Python is Fun and Python is Easy"
words = sentence.lower().split()
print(set(words))

# Question 4: Remove Duplicates and Sort
nums = [4, 2, 5, 2, 4, 1]
result = sorted(set(nums))
print(result)

# Question 5: Strict Subset
a = {1, 2}
b = {1, 2, 3}
print(a < b)

# Question 6: Squares Divisible by 3
result = set()
for i in range(1, 16):
    if i % 3 == 0:
        result.add(i * i)
print(result)

# Question 7: Count Duplicates
nums = [1, 2, 2, 3, 4, 4, 4]
duplicates = len(nums) - len(set(nums))
print(duplicates)

# Question 8: Remove Vowels
text = "Programming"
vowels = {'a', 'e', 'i', 'o', 'u'}
result = ""
for ch in text:
    if ch.lower() not in vowels:
        result += ch
print(result)

# Question 9: Symmetric Difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)

# Question 10: Compare Unique Characters
s1 = "listen"
s2 = "silent"
print(set(s1) == set(s2))


# Part D - Python Dictionaries

# Question 1: Count Word Frequency
sentence = "apple banana apple mango banana apple"
words = sentence.split()
d = {}
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)

# Question 2: Invert Dictionary
d = {'a': 1, 'b': 2, 'c': 3}
new = {}
for key in d:
    new[d[key]] = key
print(new)

# Question 3: Merge Dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'b': 10, 'c': 3}
d1.update(d2)
print(d1)

# Question 4: Group Words by First Letter
words = ["apple", "ant", "banana", "ball", "cat"]
groups = {}
for word in words:
    first = word[0]
    if first not in groups:
        groups[first] = []

    groups[first].append(word)
print(groups)

# Question 5: Keep Values Greater Than 50
d = {'a': 20, 'b': 70, 'c': 90, 'd': 40}
new = {}
for key in d:
    if d[key] > 50:
        new[key] = d[key]
print(new)

# Question 6: Access Nested Dictionary
data = {
    'user': {
        'profile': {
            'name': 'Ali'
        }
    }
}
print(data['user']['profile']['name'])

# Question 7: Dictionary of Cubes
cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3
print(cubes)

# Question 8: Find Highest Value
d = {'Ali': 90, 'Sara': 95, 'Ahmed': 88}
highest = ""
marks = 0
for key in d:
    if d[key] > marks:
        marks = d[key]
        highest = key
print(highest)

# Question 9: Create Dictionary from Lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)

# Question 10: Remove None Values
d = {'a': 10, 'b': None, 'c': 20, 'd': None}
new = {}
for key in d:
    if d[key] != None:
        new[key] = d[key]
print(new)