from datetime import date, datetime, timedelta, time
import numpy as np


def get_meeting_dates(period_as_timedelta, time_of_day,
                      number_of_meetings, start_date=datetime.now()):
    if number_of_meetings > period_as_timedelta.days:
        raise ValueError("Too many meetings!")
    # Distribute evenly:
    # start, stop, step
    day_deltas = np.linspace(0, period_as_timedelta.days-1,
                             number_of_meetings, dtype=int)
    base_time_of_day = datetime.combine(start_date, time_of_day)
    list_of_meetings = [base_time_of_day +
                        timedelta(int(day_delta)) for day_delta in day_deltas]
    return list_of_meetings


print(get_meeting_dates(timedelta(700), time(17, 0), 3))

# create another list of number of attendents,
# that was actually there at each meeting.

# So to complete that task, I'd make a list of names.
# Then I'd import import secrets choice
# Then I'd take a random number of names from the list,
# and slap them on the meetings.
# Maybe make it a dictionary?
# The key is the date, the value is the atendees

# create a bar plot of attendance through the series of meetings
# I know how to make a barplot now.
# Might return to this if i find the time this week
