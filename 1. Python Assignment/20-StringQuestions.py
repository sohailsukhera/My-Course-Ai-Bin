# Question 1: Length of a String
s = input("Enter a string: ")
print("Length:", len(s))

# Question 2: Uppercase & Lowercase
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# Question 3: Count a Character
s = input("Enter a string: ")
ch = input("Enter character: ")
print("Count:", s.count(ch))

# Question 4: First & Last Character
s = input("Enter a string: ")
if s:
    print("First:", s[0])
    print("Last:", s[-1])
else:
    print("String is empty")

# Question 5: Check Substring Presence
s = input("Enter a string: ")
sub = input("Enter substring: ")
print("Present:", sub in s)

# Question 6: Slice a String
s = input("Enter a string: ")
start = int(input("Start index: "))
end = int(input("End index: "))
print("Substring:", s[start:end])

# Question 7: Reverse a String
s = input("Enter a string: ")
print("Reversed:", s[::-1])

# Question 8: Replace Substring
s = input("Enter a string: ")
old = input("Word to replace: ")
new = input("New word: ")
print("Updated:", s.replace(old, new))

# Question 9: Split and Join
s = input("Enter a sentence: ")
words = s.split()
print("Result:", "-".join(words))

# Question 10: Strip Whitespace
s = input("Enter text: ")
print("Result:", s.strip())

# Question 11: Count Vowels & Consonants
s = input("Enter a string: ")
vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

# Question 12: Palindrome Check
s = input("Enter a string: ")
clean = ""
for ch in s:
    if ch.isalnum():
        clean += ch.lower()
if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Question 13: Title Case (Manual)
s = input("Enter a sentence: ")
words = s.split()
result = []
for word in words:
    result.append(word[0].upper() + word[1:].lower())
print("Title Case:", " ".join(result))

# Question 14: Find All Indices of a Substring
s = input("Enter string: ")
sub = input("Enter substring: ")
indices = []
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        indices.append(i)
print("Indices:", indices)

# Question 15: Character Frequency Dictionary
s = input("Enter a string: ")
freq = {}
for ch in s.lower():
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Question 16: Anagram Checker
s1 = input("First string: ")
s2 = input("Second string: ")
a = ""
b = ""
for ch in s1:
    if ch.isalpha():
        a += ch.lower()
for ch in s2:
    if ch.isalpha():
        b += ch.lower()
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")

# Question 17: Compress Repeated Characters
s = input("Enter a string: ")
if s:
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    print("Compressed:", result)

# Question 18: Longest Word in a Sentence
s = input("Enter a sentence: ")
words = s.split()
longest = ""
for word in words:
    clean = ""
    for ch in word:
        if ch.isalpha():
            clean += ch
    if len(clean) > len(longest):
        longest = clean
print("Longest Word:", longest)

# Question 19: Remove Duplicate Characters
s = input("Enter a string: ")
seen = set()
result = ""
for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch
print("Result:", result)

# Question 20: Mask Email Username
email = input("Enter email: ")
username, domain = email.split("@")
if len(username) <= 2:
    masked = username
else:
    masked = username[0] + "*" * (len(username)-2) + username[-1]
print("Masked Email:", masked + "@" + domain)