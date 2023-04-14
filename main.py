import datetime as dt
import smtplib
import random

MY_EMAIL = "your_id@gmail.com"
MY_PASSWORD = "your_password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}")