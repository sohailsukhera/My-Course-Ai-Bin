# Tuple Manipulation

# Question 1: Reverse tuple
t1=(10,20,30,40,50)
print("Reversed:",t1[::-1])

# Question 2: Access value
t2=(5,10,20,30,40)
print("Value:",t2[2])

# Question 3: Swap tuples
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple1,tuple2=tuple2,tuple1
print(tuple1)
print(tuple2)


# Tuple Operations Assignment

# Question 1: List of tuples (number, square)
start = 1
end = 10
tuple_list = []
i = start
while i <= end:
    tuple_list.append((i, i * i))
    i += 1
print("List of Tuples (Number, Square):")
print(tuple_list)

# Question 2: Filter tuples based on USN range
usn_list = [
    ("CS2023001", "Ali"),
    ("CS2023005", "Sara"),
    ("CS2023010", "Ahmed"),
    ("CS2023020", "Zain"),
    ("CS2023030", "Usman")
]
lower = 5
upper = 25
filtered_list = []
i = 0
while i < len(usn_list):
    usn = usn_list[i][0]
    name = usn_list[i][1]
    roll_no = int(usn[-3:])
    if roll_no >= lower and roll_no <= upper:
        filtered_list.append((usn, name))
    i += 1
print("Filtered USN Tuples (within range):")
print(filtered_list)