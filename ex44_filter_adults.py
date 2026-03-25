n = int(input("Enter the amount you users you will add:"))

users = []

for _ in range(n):
    name = input("Enter the user name:")
    age = int(input("Enter the user age:"))

    user = {
        "name": name,
        "age": age
        }

    users.append(user)

for user in users:
                if user["age"] >= 18:
                    print(user["name"])

