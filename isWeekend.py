#!/usr/bin/env python

import datetime


day_number = datetime.datetime(2020,11,14).weekday()

if day_number < 5:
    print("Weekday")
else:
    print("Weekend")