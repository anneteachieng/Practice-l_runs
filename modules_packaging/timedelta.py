#printing date of  future or past days

import datetime

current_date = datetime.date.today()
calculate_future_date = datetime.timedelta(int(input("Enter the number of days to add to current date.")))
future_date = current_date + calculate_future_date

print(future_date)
