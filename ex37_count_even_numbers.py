n = int(input("Enter the amount of numbers  you will enter:"))

count = 0 

for _ in range(n):
    number = int(input("Enter the numbers:"))
    if number % 2 == 0:
         count += 1

print(f"Amount of even numbers is: {count}")
