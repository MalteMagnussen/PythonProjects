# # Exercise for the 3rd course week

# ## Ex 1 Classes
# 1. Create 3 classes: Student, DataSheet and Course
# 2. A student has a data_sheet and a data_sheet has multiple courses in particular order
# 3. Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
# 4. In Student create __init__() so that a Student can be initiated with name, gender, data_sheet and image_url
# 5. In DataSheet create a method to get_grades_as_list()
# 6. In student create a method: get_avg_grade()
# 7. Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url
#    1. Let the function write the result to a csv file with format stud_name, course_name, teacher, ects, classroom, grade, img_url
# 7. Read student data into a list from a csv file:
#    1. loop through the list and print each student with name, img_url and avg_grade.
#    2. sort the list by avg_grade
#    3. create a bar chart with student_name on x and avg_grade on y-axis
# 8. Make a method on Student class that can show progression of the study in % (add up ECTS from all passed courses divided by total of 150 total points (equivalent to 5 semesters))
# 9. Show a line graph of distribution of study progression on x-axis and number of students in each category on y-axis. (e.g. make 10 categories from 0-100%)

# Extra: Make the Datasheet class iterable so that next(data_sheet) will return the next course in the list

# ## Ex 2 Exceptions
# 1. Create a function that can take a list of students and return the 3 students closest to completing their study.
# 2. If list is shorter than 3 raise your own custom exception (NotEnoughStudentsException)
# 3. Create another function that can create a csv file with 3 students closest to completion
#    1. If an exception is raised write an appropriate message to the file

# ## Ex 3 Plotting
# 1. Create a function that can take a list of students and show a pie chart of how students are distributed in ECTS percentage categories (10%, 20%, ...)
# 2. create a function that can take a list of students and show how many students have taken each course (bar chart)
#    1. create a method on student that can return a list of courses
# 3. make the figure show males and females in different colors for each course (display 2 datasets in same figure)
