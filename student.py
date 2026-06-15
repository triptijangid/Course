student_name = input("Enter your Name: ")
marks = int(input("Enter the Marks: "))
attendance = int(input("Enter the percentage:"))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

scholarship = False

if grade != "Fail":
    if attendance > 80:
        scholarship = True

print("Hello" , student_name)
print("Grade" ,grade)
print("Scholarship Eligible" , scholarship)