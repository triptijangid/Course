
correct_password = "Python123"
for i in range(1,4):
    password = input("Enter the Password :")
    if password == correct_password:
        print("Access Granted")
        break
    elif password == "Skip":
        continue
    else :
        print("Wrong Password. Try again")
        
print("System Locked")