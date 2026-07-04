# STORY ASSIGNMENTS

# 1. Find Words Containing Vowels
# Define the source story text so `story.split()` has input
story = (
    "Humanity had long surrendered control to the clockwork functions of the cities, "
    "where intelligence was measured in cycles and numbers like 2147 echoed in the towers."
)
words = story.split()
vowel_words = []
for word in words:
    for ch in word.lower():
        if ch in "aeiou":
            vowel_words.append(word)
            break
print(vowel_words)


# 2. Create List of Nouns
nouns = ["Humanity","control","functions",
        "intelligence","Cities","clockwork"]
print(nouns)


# 3. Add Nested Number List in Noun List
numbers = [2147]
noun_list = nouns + [numbers]
print(noun_list)


# 4. Convert Noun List into Tuple
noun_tuple = tuple(nouns)
print(noun_tuple)


# 5. Add Nested Tuple in Noun Tuple
noun_tuple2 = noun_tuple + ((2147,),)
print(noun_tuple2)


# 6. Convert Nouns into Set
noun_set = set(nouns)
print(noun_set)
number_set = {2147}
print(noun_set, number_set)


# 7. Create Dictionary of Nouns
noun_dict = {
    1: "Humanity",
    2: "control",
    3: "functions",
    4: "intelligence",
    5: "Cities",
    6: "clockwork",
    "numbers": {
        1: 2147
    }
}
print(noun_dict)