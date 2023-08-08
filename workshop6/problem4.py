# problem4, 29/04/21, Cordelia Jiang
# write a program that allows the user to enter the marks of 5 students in 4
# courses, Output the highest average marks for students and courses.
studentInput1 = input("Student 1 (courses 1-4): ")
studentInput2 = input("Student 2 (courses 1-4): ")
studentInput3 = input("Student 3 (courses 1-4): ")
studentInput4 = input("Student 4 (courses 1-4): ")
studentInput5 = input("Student 5 (courses 1-4): ")

studentList1 = [int(x) for x in studentInput1.split()]
studentList2 = [int(x) for x in studentInput2.split()]
studentList3 = [int(x) for x in studentInput3.split()]
studentList4 = [int(x) for x in studentInput4.split()]
studentList5 = [int(x) for x in studentInput5.split()]

allStudentsList = [studentList1, studentList2, studentList3, studentList4, studentList5]


# calc for highest average marks of students
avgStudentsList = []
for i in range(len(allStudentsList)):
    avgStudentsList.append(sum(allStudentsList[i]) / len(allStudentsList[i]))

# key parameter of max function is changed to float, as avgStudentsList contains floats
highestAvgStudent = max(avgStudentsList, key=float)


# calc for highest average marks of courses
avgCoursesList = []     # helper to store all 5 average courses marks
courseID = 0            # keep track of which course we are iterating
courseList = []         # temporary list to store all students' marks for the current course in the loop
while courseID < len(allStudentsList) - 1:
    for studentID in range(len(allStudentsList)):
        #print(studentID, courseID)
        courseList.append(allStudentsList[studentID][courseID])
    avgCoursesList.append(sum(courseList)/len(allStudentsList))
    courseList.clear()  # clear temporary list courseList
    courseID += 1

highestAvgCourse = max(avgCoursesList)


print("The highest average mark of students: ", highestAvgStudent)
print("The highest average mark of courses: ", highestAvgCourse)
