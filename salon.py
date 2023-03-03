from datetime import datetime, timedelta
from time import sleep

salon_details = {
    "name":"Codedesk Salon",
    "start_time":"8:00 AM",
    "close_time":"8:00 PM",
}

services = {   # takes time in minutes
    "hair_cut":60,
    "facial":90,
    "massage":120,
}

bookings = {    #  today's bookings
    "gaurav": ["hair_cut", "12:00 PM"],
    "anurag": ["facial", "09:00 AM"],
    "kamlesh": ["facial", "06:00 PM"],
    "dheeraj": ["massage", "04:00 PM"],
}

start_date_time_obj = datetime.strptime(salon_details["start_time"], '%H:%M %p')
close_date_time_obj = datetime.strptime(salon_details["close_time"], '%H:%M %p')

# print(start_date_time_obj)
# print(close_date_time_obj)

available_time = []

current_date_time = start_date_time_obj
# while True:
for k,v in bookings.items():
    print("current_date_time = ",current_date_time, type(current_date_time))
    if current_date_time == close_date_time_obj:
        break
    booking_time = datetime.strptime(v[1], '%H:%M %p').time()
    if current_date_time != booking_time:
        available_time.append(current_date_time)
    
    current_date_time = current_date_time + timedelta(minutes=30)
