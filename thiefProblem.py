person_A = int(input("Enter person A's amount: "))
person_B = int(input("Enter person B's amount: "))
person_C = int(input("Enter person C's amount: "))
N = int(input("Enter the stolen amount: "))

if person_A > N:
    print("Thief is Person A.")
elif person_B > N:
    print("Thief is Person B")
elif person_C > N:
    print("Thief is Person C")
else:
    print("Not found")