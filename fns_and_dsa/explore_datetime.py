import datetime
current_date = datetime.datetime.now()
print("Current date and time:", current_date)

number_of_days= int(input("Enter the number of days to add to the current date:"))
duration=datetime.timedelta(days=number_of_days,) 
future_time= current_date+duration
print("Future date:", future_time) 