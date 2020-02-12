# Used for CSV
import secrets
import csv
import platform
if platform.system() == 'Windows':
    newline = ''
else:
    newline = None
# Used for random


class Student():
    # 2. A student has a data_sheet

    def __init__(self, name, gender, data_sheet, image_url):
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


class DataSheet():
    # 2. a data_sheet has multiple courses in particular order

    def __init__(self, *courses):
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

    def addCourse(self, course):
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


class Course():
    # 3. Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
    def __init__(self, name, classroom, teacher, ects, grade=None):
        self._name = name
        self._classroom = classroom
        self._teacher = teacher
        self._ects = ects
        self._grade = grade

    def getGrade(self):
        return self._grade

    def getEcts(self):
        return self._ects


# Fixed list of course names
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


def generateStudents(numberOfStudents):
    # 7. Create a function that can generate n number of students
    # with random: name, gender, courses (from a fixed list of course names), grades, img_url

    # 1. Let the function write the result to a csv file with format
    # stud_name, course_name, teacher, ects, classroom, grade, img_url

    # Path from Documents on Maltes Machine
    with open('PythonProjects/week3/Exercises/students.csv', 'w', newline=newline) as output_file:
        # How to get random element:
        # random_element = secrets.choice(list)
        output_writer = csv.writer(output_file)

        output_writer.writerow(['2015', '1', '0', '5100', '614,5'])
        output_writer.writerow(['2015', '1', '0', '5104', '2,3'])
        output_writer.writerow(['2015', '1', '0', '5106', '1'])
        output_writer.writerow(['2015', '1', '0', '5110', '1'])

    pass


def readStudentData(csvFilePath):
    # 7. Read student data into a list from a csv file:
    #    1. loop through the list and print each student with name, img_url and avg_grade.
    #    2. sort the list by avg_grade
    #    3. create a bar chart with student_name on x and avg_grade on y-axis
    pass


def visualizeStudentProgression():
    # 9. Show a line graph of distribution of study progression on x-axis and
    # number of students in each category on y-axis. (e.g. make 10 categories from 0-100%)
    pass


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


def closestToCompletion(listOfStudents):
    # 1. Create a function that can take a list of students
    # and return the 3 students closest to completing their study.
    # 2. If list is shorter than 3 raise your own custom exception (NotEnoughStudentsException)
    pass


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
