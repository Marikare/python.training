n = int(input("Enter the amount of lines and columns:"))

for i in range (1, n + 1):
    for j in range (1, n + 1):
        print(i * j, end=" ")
    print ()

