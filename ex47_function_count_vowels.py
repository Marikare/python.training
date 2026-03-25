def countVowels(text):
    count = 0

    for char in text: 
        if  char.lower() in "aeiou":
            count += 1      
    return count 

text = input("Enter a text:")

print(f"Vowels: {countVowels(text)}")
