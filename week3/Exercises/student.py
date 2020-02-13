# Used for CSV
import math
import secrets
import csv
import platform
import matplotlib.pyplot as plt
import json
if platform.system() == 'Windows':
    newline = ''
else:
    newline = None
# Used for random


class Course():
    # 3. Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
    def __init__(self, name: str, classroom: str, teacher: str, ects: int, grade: int = None):
        self._name = name
        self._classroom = classroom
        self._teacher = teacher
        self._ects = ects
        self._grade = grade

    def getGrade(self):
        return self._grade

    def getEcts(self):
        return self._ects


class DataSheet():
    # 2. a data_sheet has multiple courses in particular order

    def __init__(self, *courses: Course):  # BEWARE
        for course in courses:
            addCourse(course)
        self.high = len(self.getCourses())

    def get_grades_as_list(self):
        # 5. In DataSheet create a method to get_grades_as_list()
        grades = []
        for course in getCourses():
            grades.append(course.getGrade())

        return grades

    def getEcts(self):
        ects = 0
        for course in self.getCourses():
            ects += course.getEcts()
        return ects

    def addCourse(self, course: Course):
        if (isinstance(course, Course)):
            self._courses.append(Course)
            self.high += 1
        else:
            raise ValueError("ERROR: {} is not a Course.".format(course))

    def getCourses(self):
        return self._courses

    # Extra: Make the Datasheet class iterable so that next(data_sheet) will return the next course in the list

    def __iter__(self):
        return self

    def __next__(self):  # Python 2: def next(self)
        self.current += 1
        if self.current < self.high:
            courses = self.getCourses()
            return courses[self.current]
        raise StopIteration


class Student():
    # 2. A student has a data_sheet

    def __init__(self, name: str, gender: str, data_sheet: DataSheet, image_url: str):
        # 4. In Student create __init__() so that a Student can be initiated with name, gender, data_sheet and image_url
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        # 6. In student create a method: get_avg_grade()
        grades = self.data_sheet.get_grades_as_list()
        gradesSum = 0
        for x in grades:
            gradesSum += x

        return gradesSum / len(grades)

    def showProgression(self):
        # 8. Make a method on Student class that can show progression
        # of the study in % (add up ECTS from all passed courses
        # divided by total of 150 total points (equivalent to 5 semesters))
        pointsCompleted = self.data_sheet.getEcts()
        percent = 150 / pointsCompleted * 100
        return percent

    def getListOfCourses(self):
        #    1. create a method on student that can return a list of courses
        return self.data_sheet.getCourses()


# Fixed lists for random generation with secrets.choice(array)
courseNames = ["Software", "Datamatiker",
               "FullStack JavaScript", "Security", "Python"]
genders = ["male", "female"]
male_names = ["Malte", "Runi", "August", "Andreas",
              "Nikolaj", "Lukas", "Jonas", "Asger"]
female_names = ["Camilla", "Stine", "Rikke",
                "Ida", "Lucia", "Emma", "Iben", "Lotte"]
grades = [-3, 00, 2, 4, 7, 10, 12]
img_urls = ["https://i.imgur.com/iARwJbr.jpg", "https://i.imgur.com/axzIjP6.jpg",
            "https://i.imgur.com/hPwV7x5.jpg", "https://i.imgur.com/f08ctzd.jpg", "https://i.imgur.com/X7dHjzh.jpg"]
classrooms = [103, 105, 101, 203, 205]
ects = [0, 30, 60, 90, 120, 150]

csvPath = "PythonProjects/week3/Exercises/students.csv"


def generateStudents(numberOfStudents):
    # tested, and it works

    # 7. Create a function that can generate n number of students
    # with random: name, gender, courses (from a fixed list of course names), grades, img_url

    # Path from Documents on Maltes Machine
    with open(csvPath, 'w', newline=newline) as output_file:

        output_writer = csv.writer(output_file)
        # Header Row
        output_writer.writerow(
            ["stud_name", "course_name", "teacher", "ects", "classroom", "grades", "img_url"])
        for i in range(0, numberOfStudents):
            gender = secrets.choice(genders)
            if gender == "male":
                name = secrets.choice(male_names)
            else:
                name = secrets.choice(female_names)
            # 1. Let the function write the result to a csv file with format
                # stud_name, course_name, teacher, ects, classroom, grade, img_url
            myEcts = secrets.choice(ects)
            myGrades = []
            for x in range(0, int(myEcts/30)):
                myGrades.append(secrets.choice(grades))

            output_writer.writerow([name, secrets.choice(courseNames), secrets.choice(male_names),
                                    myEcts, secrets.choice(classrooms), myGrades, secrets.choice(img_urls)])


def readStudentData(csvFilePath, showGraph):
    # 7. Read student data into a list from a csv file:
    #    2. sort the list by avg_grade

    # TODO:
    # DOESNT SORT PROPERLY

    students = []

    with open(csvFilePath) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # print header + its index
        for index, column_header in enumerate(header_row):
            print(index, column_header)

        # 0 stud_name
        # 1 course_name
        # 2 teacher
        # 3 ects
        # 4 classroom
        # 5 grade
        # 6 img_url

        # Get rest of rows after header and do something
        for row in reader:
            grades = json.loads(row[5])
            totalGrades = 0
            for x in grades:
                totalGrades += int(x)

            if (totalGrades != 0):
                avgGrade = totalGrades / len(grades)
            else:
                avgGrade = 0
            #    1. loop through the list and print each student with name, img_url and avg_grade.
            print("\n\nName: "+row[0]+"\nImage URL: " +
                  row[6]+"\nAverage Grade: "+str(avgGrade))

            student = {
                "student_name": row[0],
                "avg_grade": avgGrade,
                "ects": int(row[3])
            }
            students.append(student)

        # print(students)

    students_sorted = sorted(students, key=lambda i: i['avg_grade'])
    if (showGraph == True):
        print("students non sorted: ")
        print(students)
        print("\n\n")
        print("students sorted: ")
        print(students_sorted)
        #    3. create a bar chart with student_name on x and avg_grade on y-axis
        plt.figure()
        # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )

        myDict = {x["student_name"]: x["avg_grade"] for x in students_sorted}

        plt.bar(myDict.keys(), myDict.values(), width=0.7, align='center')
        # plt.ticklabel_format(useOffset=False)
        # plt.axis([0, max(ages) + 10, 0, max_y_val+500]) #axis(x-min, x-max, y-min, y-max)
        title = "Average Grade per Student"
        plt.title(title, fontsize=12)
        plt.xlabel("Student Names", fontsize=10)
        plt.ylabel("Average Grades", fontsize=10)
        plt.show()

    return students


# TESTING
# generateStudents(11)
#readStudentData(csvPath, True)


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


def visualizeStudentProgression():

    # 9. Show a line graph of distribution of study progression on x-axis and
    # number of students in each category on y-axis. (e.g. make 10 categories from 0-100%)
    categories = [i*10 for i in range(0, 11)]
    students = readStudentData(csvPath, False)
    print(students)
    myDict = {i: 0 for i in categories}
    for student in students:
        # Get % of way through studies.
        # 150 ects for a done study == 100%
        ects = student.get("ects")
        percent = roundup(ects/1.5)
        myDict[percent] += 1

    print(myDict)

    # # print(categories)
    plt.figure()
    plt.title("Study Progression", fontsize=12)
    plt.xlabel("% Progress", fontsize=10)
    plt.ylabel("Number of students", fontsize=10)
    plt.plot(list(myDict.keys()), list(myDict.values()))
    plt.show()


# visualizeStudentProgression()


class NotEnoughStudentsException(ValueError):
    # your own custom exception (NotEnoughStudentsException)

    # HOW TO USE:
    # value = 1
    # some_data = [2, 7, 8, 10, 'aha']
    # if value in some_data:
    #     print('Alright!')
    # else:
    #     raise NoOneValueError('Oh no, {} is not in {}!'.format(value, some_data))

    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


def closestToCompletion(students):
    if len(students) < 3:
        # 2. If list is shorter than 3 raise your own custom exception (NotEnoughStudentsException)
        raise NotEnoughStudentsException(
            "Not enough students. Must be at least 3.")
    # 1. Create a function that can take a list of students
    # and return the 3 students closest to completing their study.
    students_sorted = sorted(students, key=lambda i: i['avg_grade'])
    print(students_sorted[-3:])
    return students_sorted[-3:]


#closestToCompletion(readStudentData(csvPath, False))


def topStudentsToCSV(listOfStudents):
    # 3. Create another function that can create a csv file with 3 students closest to completion
    #    1. If an exception is raised write an appropriate message to the file
    pass


def ectsDistrubution():
    # 1. Create a function that can take a list of students
    # and show a pie chart of how students are distributed
    # in ECTS percentage categories (10%, 20%, ...)
    pass


def courseBarChart():
    # 2. create a function that can take a list of students
    # and show how many students have taken each course (bar chart)
    # 3. make the figure show males and females in different colors for each course (display 2 datasets in same figure)
    pass
