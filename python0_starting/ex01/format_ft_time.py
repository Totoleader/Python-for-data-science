#!/usr/bin/python3

import datetime
from time import time

timesince = time()

decimal_timesince = "{:,.4f}".format(timesince)
scientific_timesince = '{:.2e}'.format(timesince)
current_date = datetime.date.today().strftime("%b %d %Y")

print("Seconds since January 1, 1970:", decimal_timesince, "or", scientific_timesince, "in scientific notation")
print(current_date)