# Write a program to count the number of vowels in a given string. (aeiouAEIOU).


text = input("Enter a string: ")

vowels = "aeiouAEIOU"

count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:" , count)