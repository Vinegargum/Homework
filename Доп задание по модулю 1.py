dict_school={}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=list(students)
students2=students.sort()
m0=sum(grades[0])/len(grades[0])
m1=sum(grades[1])/len(grades[1])
m2=sum(grades[2])/len(grades[2])
m3=sum(grades[3])/len(grades[3])
m4=sum(grades[4])/len(grades[4])
dict_school.update({students[0]:m0, students[1]:m1, students[2]:m2,students[3]:m3, students[4]:m4})
print(dict_school)
