import datetime

#take todays date and minus 30 days from it
#https://docs.python.org/3.4/library/datetime.html

today = datetime.date.today()
mas =datetime.timedelta(days=30)


date2 = today - mas

#sample date imput and format correction
year = 2018
month = 3
day = 20


com = datetime.date(year, month, day)

if com > date2:
    print(com)
else:
    print("Nothng found")
