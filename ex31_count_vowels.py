n = input("Enter the word you want to count the vowels:")

count = 0

for letter in n:
    if letter.lower() in "aeiou":
        count = count + 1
print(f"Vowels: {count}")
