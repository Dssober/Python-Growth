#import smtplib

#my_email = "dylans.sober@gmail.com"
#password = "edpv nnkr iyqq xmgf"

#with smtplib.SMTP("smtp.gmail.com") as connection:
   # connection.starttls()
   # connection.login(user=my_email, password=password)
   # connection.sendmail(
   #     from_addr=my_email,
    #    to_addrs="dylsober@gmail.com",
   #     msg="Subject:Hello\n\nThis is the body of my email."
#    )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1991, month=12, day=15)
# print(date_of_birth)

import datetime as dt
import smtplib
import random

my_email = "your email"
password = "your pass"
now = dt.datetime.now()
week_day = now.weekday()

if week_day == 5:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        random_quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dylsober@gmail.com",
             msg=f"Subject:Monday Motivation\n\nThis is your motivational quote: {random_quote}."
            )












