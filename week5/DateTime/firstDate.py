from datetime import date, datetime, timedelta
import datetime

# Make todays date
today = date.today()
print(today)

# To show that you can get year, month, day
today = date(today.year, today.month, today.day)
print(today)

next_lecture = date(today.year, today.month, today.day)
td = timedelta(days=7)
time_to_next_lecture = abs(today-today+td)
print(type(time_to_next_lecture))
print("Days to next lecture:", time_to_next_lecture.days)

next_lecture = date(today.year, 10, 2) + datetime.timedelta(5)
time_to_next_lecture = abs(next_lecture - today)
print(time_to_next_lecture.days)

print(today.strftime("%d/%m/%Y"))

print(today.strftime("%A %d. %B %Y"))
