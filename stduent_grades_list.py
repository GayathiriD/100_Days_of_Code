student_scores= {
    "Harry": 88,
    "Ron" : 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

student_grades = {}
for key in student_scores:
    if student_scores[key] <=100 and student_scores[key] >90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] <=90 and student_scores[key] >80:
        student_grades[key] = "Exceeds Expectation"
    elif student_scores[key] <=80 and student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)        