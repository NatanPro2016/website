from django.db import models
from django.utils import timezone

# Create your models here.

from django.db import models

# Create your models here.
class SectorMessage(models.Model):
    class Titles(models.TextChoices):
        WEEKEND  = 'WE', 'weekend'
        REGULAR = 'RE', 'regular'
        EXTENSION = 'EX', 'extension'

    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50 ,choices=Titles.choices)

    
class Sector(models.Model):
    class Titles(models.TextChoices):
        WEEKEND  = 'WE', 'weekend'
        REGULAR = 'RE', 'regular'
        EXTENSION = 'EX', 'extension'

    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50 ,choices=Titles.choices)


    def __str__(self):
        return self.title



class Studet(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PE', 'pending'
        STARTED = 'ST', 'started'

    class Titles(models.TextChoices):
        WEEKEND  = 'WE', 'weekend'  
        REGULAR = 'RE', 'regular'
        EXTENSION = 'EX', 'extension'


    first_name = models.CharField(max_length=40, blank=True)
    middle_name = models.CharField(max_length=40,  blank=True)
    last_name = models.CharField(max_length=40,  blank=True)
    sex = models.CharField(max_length=10  ,blank=True)
    email = models.EmailField( blank=True)
    phone_number = models.CharField(max_length=40,  blank=True)
    status = models.CharField(max_length=40, choices=Status.choices, default='pending',  blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE,  blank=True)
    type = models.CharField(max_length=50 ,choices=Titles.choices)
    date = models.DateTimeField(default=timezone.now)



class Teacher(models.Model):
    first_name = models.CharField(max_length=40,  blank=True)
    middle_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    sex = models.CharField(max_length=10, blank=True)
    phone_no = models.CharField(max_length=40, blank=True)
    


    def __str__(self):
        return self.first_name


class Room(models.Model):
    room_no = models.CharField(max_length=20)
    campaus = models.CharField(max_length=20)

    def __str__(self):
        return self.room_no



class Schedule(models.Model):
    class Days(models.TextChoices):
        MONDAY  = 'MO', 'Monday'
        TUESDAY = 'TU', 'Tuesday'
        WEDNESDAY = 'WE', 'Wednesday'
        THURSDAY= 'TH', 'Thursday'
        FRIDAY = 'FR', 'Friday'
        SATURDAY = 'SA', 'Saturday'
        SUNDAY = 'SU', 'Sunday'
    class Times(models.TextChoices):
        MORNING  = 'MO', 'Morning'
        AFTERNOON = 'AF', 'Afternoon'
        NIGHT = 'NI', 'Night'

    day = models.CharField(max_length=50, choices=Days.choices)
    time = models.CharField(max_length=10, choices=Times.choices)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector , on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class News(models.Model):
    header = models.CharField(max_length=20)
    message = models.CharField(max_length=255)
    


class Feedback(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.CharField(max_length=255)



   
    
    
