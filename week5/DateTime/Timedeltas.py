from datetime import timedelta, datetime

print('smallest possible timedelta:\t', timedelta.min)
print('largest possible timedelta:\t', timedelta.max)
t = timedelta(weeks=1, days=2, hours=3,
              minutes=4, seconds=5, microseconds=999)
# timedelta internally translates all to days,
# seconds and microseconds
print('internal representation:\t', repr(t))

print("a timedelta can be negative")
minus_5_hours = timedelta(hours=-5)
print(minus_5_hours)


print(" Operations with timedeltas")
year_as_delta = timedelta(days=365)
print('year_as_delta:', year_as_delta)
another_year_delta = timedelta(
    weeks=40, days=84, hours=23, minutes=50, seconds=600)
# adds up to 365 days
print(another_year_delta)

print("")
print("Year deltas")
last_year = datetime.now() - year_as_delta
next_year = datetime.now() - year_as_delta + (2 * another_year_delta)
print('last year', last_year)
print('next year', next_year)
print('difference', next_year-last_year)
two_year_delta = next_year - last_year
print('The two year difference is equivalent to {} days or to {} seconds'.format(
    two_year_delta.days, two_year_delta.total_seconds()))
