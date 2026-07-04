# Dictionary Manipulation

# Question 1: Check value in dictionary
student={"name":"Ali","age":20,"city":"Lahore"}
value="Ali"
if value in student.values():
    print("Value exists")
else:
    print("Not found")

# Question 2: Key of minimum value
marks={"Math":80,"English":65,"Science":90}
min_value=min(marks.values())
for key in marks:
    if marks[key]==min_value:
        print("Min value key:",key)

# Question 3: Delete keys from dictionary
data={"a":1,"b":2,"c":3,"d":4}
remove_keys=["b","d"]
for key in remove_keys:
    if key in data:
        data.pop(key)
print("Updated dict:",data)

# Dictionary Operations Assignment

# Question 1: Check if a key exists
my_dict = {
    "name": "Ali",
    "age": 18,
    "city": "Lahore"
}
key_to_check = "age"
if key_to_check in my_dict:
    print("Key exists")
else:
    print("Key does not exist")

# Question 2: Add a key-value pair
my_dict["country"] = "Pakistan"
print("Updated Dictionary:", my_dict)

# Question 3: Sum of all values
num_dict = {
    "a": 10,
    "b": 20,
    "c": 30
}
total = 0
for key in num_dict:
    total += num_dict[key]
print("Sum of all items:", total)

# Question 4: Product of all values
product = 1
for key in num_dict:
    product *= num_dict[key]
print("Product of all items:", product)

# Question 5: Dictionary of squares
n = 5
square_dict = {}
i = 1
while i <= n:
    square_dict[i] = i * i
    i += 1
print("Square Dictionary:", square_dict)

# Question 6: Concatenate two dictionaries
dict1 = {
    "a": 1,
    "b": 2
}
dict2 = {
    "c": 3,
    "d": 4
}
merged_dict = {}
for key in dict1:
    merged_dict[key] = dict1[key]
for key in dict2:
    merged_dict[key] = dict2[key]
print("Concatenated Dictionary:", merged_dict)