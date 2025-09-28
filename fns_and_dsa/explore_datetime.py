from datetime import datetime,timedelta

current_date = datetime.now()
def display_current_datetime():
    print("Current date and time:", current_date)




def calculate_future_date():
    number_of_days= int(input("Enter the number of days to add to the current date:"))
    duration=timedelta(days=number_of_days) 
    future_time= current_date+duration
    print("Future date:", future_time) 




if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
