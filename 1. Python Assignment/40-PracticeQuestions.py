# Part A - Python Lists

# Question 1: Print First and Last Element
nums = [3, 1, 4, 1, 5]
print("First:", nums[0])
print("Last:", nums[-1])

# Question 2: Find Length of List
colors = ['red', 'blue', 'green']
print("Length:", len(colors))

# Question 3: Append an Element
colors = ['red', 'blue']
colors.append('yellow')
print(colors)

# Question 4: Insert an Element
fruits = ['apple', 'banana']
fruits.insert(1, 'orange')
print(fruits)

# Question 5: Remove an Element
fruits = ['apple', 'banana', 'grapes']
fruits.remove('banana')
print(fruits)

# Question 6: Pop Last Element
items = [10, 20, 30]
value = items.pop()
print("Popped:", value)
print(items)

# Question 7: Check Membership
nums = [1, 2, 3, 4]
print(3 in nums)

# Question 8: Slice a List
a = [0, 1, 2, 3, 4]
print(a[2:4])

# Question 9: Replace an Element
a = [5, 10, 15]
a[1] = 12
print(a)

# Question 10: Count Occurrences
nums = [1, 2, 2, 3, 2]
print(nums.count(2))


# Part B - Python Tuples

# Question 1: Print Second Element
t = (10, 20, 30)
print(t[1])

# Question 2: Find Length of Tuple
t = ('a', 'b', 'c')
print(len(t))

# Question 3: Unpack Tuple
x, y = (4, 5)
print(x)
print(y)

# Question 4: Check Membership
t = ('a', 'b', 'c')
print('b' in t)

# Question 5: Empty Tuple
t = ()
print(type(t))

# Question 6: Concatenate Tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)

# Question 7: Repeat Tuple
t = (7,)
print(t * 3)

# Question 8: Find Index
t = (1, 2, 3, 2)
print(t.index(2))

# Question 9: Count Occurrences
t = (1, 2, 3, 2)
print(t.count(2))

# Question 10: Single Element Tuple
t = (5,)
print(t)


# Part C - Python Sets

# Question 1: Create a Set
s = set([1, 2, 2, 3])
print(s)

# Question 2: Add Element
s = {1, 2, 3}
s.add(4)
print(s)

# Question 3: Remove Element
s = {1, 2, 3}
s.remove(2)
print(s)

# Question 4: Check Membership
s = {1, 3, 5}
print(5 in s)

# Question 5: Find Length
s = {10, 20, 30}
print(len(s))

# Question 6: Clear Set
s = {1, 2, 3}
s.clear()
print(s)

# Question 7: Add if Missing
s = {'a', 'b'}
if 'c' not in s:
    s.add('c')
print(s)

# Question 8: Remove Duplicates
lst = ['a', 'a', 'b']
s = set(lst)
print(s)

# Question 9: Union of Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

# Question 10: Intersection of Sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 & set2)


# Part D - Python Dictionaries

# Question 1: Print a Value
d = {'name': 'Ali', 'age': 25}
print(d['name'])

# Question 2: Add a Key
d = {'name': 'Ali', 'age': 25}
d['city'] = 'Lahore'
print(d)

# Question 3: Change a Value
d = {'name': 'Ali', 'age': 25}
d['age'] = 30
print(d)

# Question 4: Delete a Key
d = {'name': 'Ali', 'age': 25}
del d['age']
print(d)

# Question 5: Check if Key Exists
d = {'name': 'Ali', 'age': 25}
print('salary' in d)

# Question 6: Print All Keys
d = {'a': 1, 'b': 2}
print(d.keys())

# Question 7: Print All Values
d = {'a': 1, 'b': 2}
print(d.values())

# Question 8: Iterate Dictionary
d = {'x': 10, 'y': 20}
for k, v in d.items():
    print(k, v)

# Question 9: Use get()
d = {}
print(d.get('score', 0))

# Question 10: Create Dictionary from Lists
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))
print(d)