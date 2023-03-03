from django.shortcuts import render
from .models import *
from datetime import time, datetime, date, timedelta

# def is_time_between(begin_time, end_time, check_time=None):
#     # If check time is not given, default to current UTC time
#     check_time = check_time or datetime.utcnow().time()
#     if begin_time < end_time:
#         return check_time > begin_time and check_time < end_time
#     else: # crosses midnight
#         return check_time > begin_time or check_time < end_time


def available_time(request):
    salon = Salon.objects.get(id=1)
    salon_bookings = Bookings.objects.filter(salon=salon, created_at__contains = date.today())
    salon_services = Service.objects.filter(salon=salon)
    print("bbbbbbbbbb",salon_bookings)
    startTimeOfSalon = salon.start_time

    endtimeOfSalon = salon.end_time
    tempTime = startTimeOfSalon

    availableTimeList = []

    while tempTime < endtimeOfSalon:
        if tempTime in salon_bookings.values_list("booking_time", flat=True):
            serviceTimeTaken = Bookings.objects.get(booking_time=tempTime, salon=salon).service.service_time_taken
            result = datetime.combine(date.today(), tempTime) + timedelta(minutes=serviceTimeTaken)
            serviceEndAt = result.time()

            result = datetime.combine(date.today(), tempTime) + timedelta(minutes=30)
            nextSlot = result.time()

            if nextSlot == serviceEndAt:
                tempTime = nextSlot
                availableTimeList.append(tempTime)
            elif nextSlot < serviceEndAt:
                result = datetime.combine(date.today(), tempTime) + timedelta(minutes=30)
                tempTime = result.time()
            else:
                tempTime = nextSlot
                
        else:
            availableTimeList.append(tempTime)
        result = datetime.combine(date.today(), tempTime) + timedelta(minutes=30)
        tempTime = result.time()
    
    context = {
        "salon":salon,
        "services":salon_services,
        "bookings":salon_bookings,
        "available_time":availableTimeList
        }


    return render(request, "available_time.html" , context)