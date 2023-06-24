students_grade=[]
students_grade.append((1,"srinidhi"))
students_grade.append((4,"preethi"))
print("yes")
print(students_grade)
students_grade.append((3,"mithra"))
students_grade.append((2,"madhu"))
students_grade.sort(reverse=True)
print("priority wise sorted")
print(students_grade)
print("")
print("original queue")
while students_grade:
    print(students_grade.pop())
