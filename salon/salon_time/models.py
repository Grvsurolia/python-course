from django.db import models

class Salon(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=50)
    service_time_taken = models.IntegerField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Bookings(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    booking_time = models.TimeField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.service.name