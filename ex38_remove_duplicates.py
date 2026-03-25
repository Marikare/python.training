n = int(input("How many itens you wanna add to your list?:"))

list = []

for _ in range(n):
    value = input("Enter something to your list:")
    if value not in list:
        list.append(value)

print(list)



