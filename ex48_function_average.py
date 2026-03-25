def average(arr):
    return sum(arr) / len(arr)

n = int(input("Enter the amount of itens you wanna add to the list:"))

arr = []

for _ in range(n):
    arr.append(int(input("Enter a number:")))

print(f"The average is: {average(arr)}")

