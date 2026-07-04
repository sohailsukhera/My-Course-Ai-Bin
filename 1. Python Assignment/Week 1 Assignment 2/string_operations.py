# String Manipulation

# Question 1: First, middle, last character
text=input("Enter a string:")
first=text[0]
middle=text[len(text)//2]
last=text[-1]
print("New string:",first+middle+last)

# Question 2: Count occurrences of characters
text=input("Enter a string:")
count={}
for ch in text:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print("Character count:",count)

# Question 3: Reverse a string
text=input("Enter a string:")
print("Reversed string:",text[::-1])

# Question 4: Split string on hyphens
text=input("Enter hyphen-separated string:")
print("Split string:",text.split('-'))

# Question 5: Remove special symbols
text=input("Enter a string:")
cleaned=""
for ch in text:
    if ch.isalnum() or ch.isspace():
        cleaned+=ch
print("Clean string:",cleaned)


# ASSIGNMENT 3 - STRING MANIPULATION PROGRAMS

# 1. Pangram Check 
text = input("Enter string for pangram check: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True
for ch in alphabet:
    if ch not in text:
        is_pangram = False
if is_pangram:
    print("It is a pangram")
else:
    print("It is not a pangram")

# 2. Replace Spaces with Hyphen
text = input("Enter string: ")
print(text.replace(" ", "-"))

# 3. Letters in Two Strings but not Both
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = ""
for ch in str1:
    if ch not in str2 and ch not in result:
        result += ch
for ch in str2:
    if ch not in str1 and ch not in result:
        result += ch
print(result)

# 4. Larger String without Using len()
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
count1 = 0
count2 = 0
for i in str1:
    count1 += 1
for i in str2:
    count2 += 1
if count1 > count2:
    print("Larger string:", str1)
else:
    print("Larger string:", str2)

# 5. Count Uppercase and Lowercase Letters
text = input("Enter string: ")
upper = 0
lower = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)

# 6. Check Anagram
str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

# 7. Check Substring
main = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in main:
    print("Substring found")
else:
    print("Substring not found")

# 8. Find Length without len()
text = input("Enter string: ")
count = 0
for ch in text:
    count += 1
print("Length:", count)

# 9. New String from First 2 and Last 2 Characters
text = input("Enter string: ")
if len(text) >= 2:
    print(text[:2] + text[-2:])
else:
    print("String too short")