s = 0

while True:
    value = input("Enter the numbers you want to add or stop:")

    if value == "stop":
        break
    s = s + int(value)

print(s)
