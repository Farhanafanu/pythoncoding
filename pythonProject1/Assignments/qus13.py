writtentestweight = 70
labexamsweight = 20
assignmentsweight = 10
writtentestscore = float(input("Enter the score for the written test: "))
labexamsscore = float(input("Enter the score for the lab exams: "))
assignmentsscore = float(input("Enter the score for the assignments: "))
overall_grade = (writtentestscore * writtentestweight / 100) + (labexamsscore * labexamsweight / 100) + (assignmentsscore * assignmentsweight / 100)
print(" overall grade:", overall_grade)
