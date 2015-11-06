import datetime
print("Today is"), (datetime.datetime.now().date()), \
("and it is"), datetime.datetime.now().strftime("%H:%M:%S")
