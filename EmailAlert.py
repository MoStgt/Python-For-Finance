import os
import smtplib
import imghdr
from email.message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

EMAIL_ADDRESS = 'xxxx@googlemail.com'
EMAIL_PASSWORD = 'xxxx'

msg = EmailMessage()

yf.pdr_override()
start = dt.datetime(2018, 12, 1)
now = dt.datetime.now()

stock = "QQQ"
TargetPrice = 180

msg["Subject"] = "Alert on " + stock
msg["From"] = EMAIL_ADDRESS
msg["To"] = 'Email address'

alerted = False

while 1:
    df = pdr.get_data_yahoo(stock, start, now)
    currentClose = df["Adj Close"][-1]

    condition = currentClose > TargetPrice

    if (condition and alerted==False):
        alerted = True
        message = stock + " Has activated the alert price of " + str(TargetPrice) + \
            "\nCurrent Price: " + str(currentClose)
        msg.set_content(message)

        files = [r""]

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

            print("completed")
    else:
        print("no new alerts")

    time.sleep(60)