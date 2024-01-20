from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
class Bus(models.Model):
    
    bus=models.TextField()
    seatplanleft=models.IntegerField()
    seatplanright=models.IntegerField()
    seatplanrows=models.IntegerField()
    operations_day=models.IntegerField()
    costmultiplier=models.FloatField()

    def __str__(self):
        return self.bus
class Routes(models.Model):
        fromstop=models.TextField()
        tostop=models.TextField()
        distance=models.IntegerField()
        cost=models.IntegerField()
        time=models.DateTimeField()
        bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
class Location(models.Model):
    locationname=models.TextField()
    coordinatesx=models.IntegerField()
    coordinatesy=models.IntegerField()
    city=models.TextField()
    state=models.TextField()
class Seats(models.Model):
    rownumber=models.IntegerField()
    colnumber=models.IntegerField()
    isoccupied=models.BooleanField()
class Users(models.Model):
    username=models.TextField()
    password=models.TextField()
    isadmin=models.BooleanField()
class Stops(models.Model):
    stopname=models.TextField()
    locationid=models.ForeignKey(Location,on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus,on_delete=models.CASCADE)
    arrivaltime=models.DateTimeField()
    departuretime=models.DateTimeField()
class Bookings(models.Model):
    userid=models.ForeignKey(Users,on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus,on_delete=models.CASCADE)
    seatrow=models.IntegerField()
    seatcol=models.IntegerField()
    date=models.DateTimeField()
    departuretime=models.DateTimeField()
    arrivaltime=models.DateTimeField()
    fromstop=models.ForeignKey(Stops,on_delete=models.CASCADE,related_name='fromstop')
    tostop=models.ForeignKey(Stops,on_delete=models.CASCADE,related_name='tostop')




     
    

    






# Create your models here.
