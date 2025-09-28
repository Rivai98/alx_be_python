from datetime import datetime,timedelta

current_date = datetime.now()
def display_current_datetime():
    print("Current date and time:", current_date)
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted date and time:", formatted_date)




def calculate_future_date():
    number_of_days= int(input("Enter the number of days to add to the current date:"))
    duration=timedelta(days=number_of_days) 
    future_date= current_date+duration
    print("Future date:", future_date) 
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted future date:", formatted_future_date) 




if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
