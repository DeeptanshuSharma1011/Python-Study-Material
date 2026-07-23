# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-90), C (70-79), D (60-69), F (below 60).

score = int(input("Enter the student's score: "))
grade = ""

if score < 60:
    grade = "F"
elif score < 70:
    grade = "D"
elif score < 80:
    grade = "C"
elif score <= 90:
    grade = "B"
else:
    grade = "A"

if score <= 101:
    print("Invalid score")
    exit()

print("Grade:", grade)
