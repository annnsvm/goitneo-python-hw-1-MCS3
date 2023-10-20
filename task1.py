from datetime import datetime
from collections import defaultdict
import calendar


def get_birthdays_per_week(users):
    bdays = defaultdict(list)
    current_day = datetime.today().date()

    for user in users:
        birthday_this_year = user["birthday"].date().replace(
            year=current_day.year)

        if birthday_this_year < current_day:
            birthday_this_year = birthday_this_year.replace(
                year=current_day.year+1)

        delta_days = (birthday_this_year - current_day).days

        if delta_days >= 7:
            continue

        weekday = birthday_this_year.weekday()
        if weekday in [5, 6]:
            weekday = 0
        bdays[weekday].append(user['name'])

    for weekday, user in bdays.items():
        print('{},{}'.format(calendar.day_name[weekday], ','.join(users)))




users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
         {"name": "Bill ", "birthday": datetime(1999, 12, 14)}]

birthdays = get_birthdays_per_week(users)

print(birthdays)
