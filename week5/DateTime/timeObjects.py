from datetime import datetime, date, time, timedelta

t = time(12, 10, 30)

print(t.isoformat())

print(t.strftime('%H:%M:%S'))

print('The time is {:%H:%M}.'.format(t))
