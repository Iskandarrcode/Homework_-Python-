import os
import datetime

os.system("cls")

date = input("Sanani kriting: ").strip()

year = date[6:]
month = date[3:5]
day = date[:2]

date = datetime.datetime(int(year), int(month), int(day)).date()
weekday = date.strftime("%A")

while weekday != "Friday":
    date = date + datetime.timedelta(days=1)
    weekday = date.strftime("%A")

while date.day != 13:
    date = date + datetime.timedelta(days=7)

print(f"{date.day:02d}.{date.month:02d}.{date.year:04d}")