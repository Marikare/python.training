n = input("Enter a word to check if it is a palindrome:")

n = n.lower().replace(" ", "")

reverse = n[::-1]

if n == reverse:
    print("Its a palindrome")
else:
    print("Its NOT a palindrome")
