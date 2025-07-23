#Ask the user to input a score
score = int(input("Enter the student score(0 - 100)"))

if score >= 90:
    grade = 'A'

elif score >= 80:
    grade = 'B'

elif score >= 70:
    grede = 'C'

elif score >= 60:
    grade = 'D'

#print the result

print(f"The student's grade is: ({grade})")