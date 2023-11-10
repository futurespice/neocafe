from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Schedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Workdays(models.Model):
    WEEKDAYS = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    workday = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.schedule.title} - {self.workday} - {self.start_time} - {self.end_time}'

    class Meta:
        verbose_name_plural = 'Workdays'


class Branch(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = PhoneNumberField()
    link_to_map = models.URLField()

    def __str__(self):
        return f'{self.address} - {self.phone_number}'
