n = int(input("Enter the amount of numbers you will add:"))

numbers = []

for i in range(n):
    value = int(input("Enter a number:"))
    numbers.append(value)

print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")

