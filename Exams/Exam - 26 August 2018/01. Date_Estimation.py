from datetime import date, timedelta, datetime

today = date(2018, 8, 26)

year, month, day = input().split('-')
check_date = date(int(year), int(month), int(day))

if check_date < today:
    print('Passed')
elif check_date == today:
    print('Today date')
else:
    delta = check_date - today
    print(f"{delta.days+1} days left")
