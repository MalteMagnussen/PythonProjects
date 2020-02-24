from datetime import datetime, date, time
import dateutil.parser

print(datetime.now().isoformat())


dt = datetime.strptime('21/11/2006 16:30', '%d/%m/%Y %H:%M')
print(dt)

print(dt.strftime('%y-%m-%d %H:%M'))

myDate = dateutil.parser.parse('21-11-06 16:30')

print(type(myDate))
print(myDate)
