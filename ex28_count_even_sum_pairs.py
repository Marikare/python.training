n = int(input("Enter a number to check how many even numbers it has:"))

count = 0

for i in range (1, n + 1):
    for j in range (1, n + 1):
        if (i + j)  % 2 == 0:
            count = count + 1
print(count)
