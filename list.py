first = input("Enter your first name: ")
last = input("Enter your last name: ")

fullname = first + " " + last
print(f"Full Name: {fullname}")

uppercase = fullname.upper()
print("Uppercase: ", uppercase)

lst = list(fullname)
print("Characters: ",lst)
for ch in lst:
    print(ch)

print("First character: ", lst[0])

print("Last Character: ", lst[-1])

print("First 4 Characters: ", lst[:4])

tup = (fullname, len(fullname))
print("Tuple: ",tup)

