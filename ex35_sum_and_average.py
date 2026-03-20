n = int(input("Enter the amount off numbers you want to add:"))

s = 0

for i in range(n):
    values = float(input("Enter the number:"))
    s = s + values
    a = s / n

print(f"Sum is {s}")
print(f"Avg is {a}")
