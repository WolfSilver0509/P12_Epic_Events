from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    contact_ventes = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    contact_ventes = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()



class Event(models.Model):
    EVENT_STATUS_CHOICES = (
        ('A venir', 'A venir'),
        ('En cours', 'En cours'),
        ('Terminer', 'Terminer'),
    )

    id = models.AutoField(primary_key=True)
    contract = models.ForeignKey('Contract', on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    event_status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()