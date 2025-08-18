# Lecture 1: Intro to Python.
# Worksheet 1

# Formatting stuff
skip = True
SEP = "-" * 10
BIG_SEP = "-" * 20

# Problem 1
name = "Sanchit Ram Arvind"
age = 29
height = 67  # inches
print(f"{BIG_SEP} PROBLEM 1 {BIG_SEP}")
print(f"{SEP} (i) {SEP}")
print("Hi! My name is", name, "\nI am", age, "years old, and am", height, "inches tall")
print(f"{SEP} (ii) {SEP}")
print(f"Hi! My name is {name}\nI am {age} years old, and am {height:.1f} inches tall")

# Problem 2
print()
print(f"{BIG_SEP} PROBLEM 2 {BIG_SEP}")
year = input("Tell me the year: ").strip()
day = input("Tell me the day: ")
time = input("Tell me the time: ")
print("\tYear is", year, "\n\tDay is", day, "\n\tTime is", time)
print("Year is 2025:", year == "2025")

# Problem 3
print()
print(f"{BIG_SEP} PROBLEM 3 {BIG_SEP}")
x = 61
y = 50
z = 11
print(f"{x} - {y} == {z}", x - y == z)
print(f"{x / 10} - {y / 10} == {z / 10}", x / 10 - y / 10 == z / 10)
print("Probably because...", x / 10 - y / 10, "is not equal to", z / 10)

# Problem 4
print()
# print(f"{BIG_SEP} PROBLEM 4 {BIG_SEP}")
b = 1
c = int(input("Enter an integer: "))
print(f"{c} * 1 == {c}:", b * c == c)
b /= 10
print(f"{c} * 1/10 == {c / 10}:", b * c == c / 10)

# Problem 5
print()
print(f"{BIG_SEP} PROBLEM 5 {BIG_SEP}")
str1 = "String 1"
str2 = "String 2"
lst1 = ["list1", "1"]
lst2 = [lst1, "list2"]

print(f"Adding two strings {str1} + {str2}:", str1 + str2)
# print(f"Subtracting two strings {str1} - {str2}", str1 - str2) # Can't subtract strings
# print(f"Multiply two strings {str1} * {str2}", str1 * str2) # Can't multiply strings
# print(f"Multiply two lists {lst1} * {lst2}", lst1 * lst2)  # Can't multiply lists
print(f"Multiply string by an integer {str1} * 10:", str1 * 10)
print(f"Multiplying list by an integer {lst1} * 10:", lst1 * 10)
# print(f"Divide two strings: {str1} / {str2}", str1 / str2)  # Can't divide strings
# print(f"Divide two lists: {lst1} / {lst2}", lst1 / lst2)  # Can't divide lists
