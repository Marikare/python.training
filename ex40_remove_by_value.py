n = int(input("Enter the amount of itens you will add to the list:"))

arr = []

for _ in range(n):
    arr.append(input("Enter itens to your list:").strip())

target = input("Enter item to remove:").strip()

if target in arr:
    arr.remove(target)

print(arr)

