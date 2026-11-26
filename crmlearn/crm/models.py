from django.db import models

# Create your models here.
class Doctor(models.Model):
    class EmploymentStatus(models.TextChoices):
        ACTIVE = "AC", "Active"
        FIRED = "FR", "Fired"
        ON_VACATION = "OV", "On vacation"
        SICK_LEAVE = "SL", "Sick leave"
        INTERN = "IN", "intern"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30)
    email = models.EmailField()
    employment_status = models.CharField(max_length=11, choices=EmploymentStatus.choices, default=EmploymentStatus.ACTIVE)


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

class Appointment(models.Model):
    class AppointmentStatus(models.TextChoices):
        ACTIVE = "AC", "Active"
        COMPLETED = "CP", "Completed"
        CANCELED = "CN", "Canceled"
        MOVED = "MV", "Moved"

    doctor = models.ForeignKey(Doctor, on_delete = models.PROTECT, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete = models.PROTECT, related_name="appointments")
    datetime = models.DateTimeField()
    status = models.CharField(max_length=11, choices=AppointmentStatus.choices, default=AppointmentStatus.ACTIVE)