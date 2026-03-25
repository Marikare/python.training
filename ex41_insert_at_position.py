n = int(input("Enter the amount of itens your list will have:"))

arr = []

for _ in range(n):
    arr.append(input("Enter itens to your list:"))

value = input("What do you wanna add?:")
pos = int(input("Enter the location you want to add:"))

arr.insert(pos, value)

print(arr)
