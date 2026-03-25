name = input("Enter your name:")
email = input("Enter your email:")
age = int(input("Enter your age:"))

person1 = { 
           "Name": name,
           "Email": email,
           "Age": age
           }

print(f"Name: {person1["Name"]}")
print(f"Email: {person1["Email"]}")
print(f"Age: {person1["Age"]}")
