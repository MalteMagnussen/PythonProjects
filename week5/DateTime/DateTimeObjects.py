from datetime import datetime, date, time


d = date.today()
t = time(12, 30)
combined = datetime.combine(d, t)
# todays date combined with time: 12:30
print(combined)

now = datetime.now()

print(now)
print(type(now))
now = now.replace(microsecond=0)
print(now)

utc = datetime.utcnow()
print("UTC", utc)

##

# isocalendar using (year, week, day)
ic = datetime.now().isocalendar()
print('the year is {}, the week is {} and it is the {}th day'.format(
    ic[0], ic[1], ic[2]))
week_number = ic[1]
print("ic", ic)
print("week number", week_number)

##

# Using datetime (or time or date) .strftime() to convert datetime
# to string.
# See https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
now = datetime.now()
date_string = now.strftime("%A, %d. %B %Y %I:%M%p")
print(date_string)
# or using string format with new style: https://pyformat.info/
print('Time now is: {:%A %Y-%m-%d %H:%M:%S:%f}'.format(datetime.now()))

##

# format textstring using str.format()
print("str.format()", 'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(now, "day", "month", "time")
      )

print("almost done")
d = datetime.strptime('10 Jun 2010', '%d %b %Y')
print(d)
print(d.strftime('%d-%m-%Y week: %U'))
