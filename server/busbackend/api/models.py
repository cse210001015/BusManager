from django.db import models

class Bus(models.Model):
    """
    Model representing a bus.
    """
    busName = models.TextField()
    seatPlanLeft = models.IntegerField()
    seatPlanRight = models.IntegerField()
    seatPlanRows = models.IntegerField()
    operatingDays = models.IntegerField()
    costMultiplier = models.FloatField()

class Routes(models.Model):
    """
    Model representing routes between stops.
    """
    fromStop = models.TextField()
    toStop = models.TextField()
    distance = models.IntegerField()
    cost = models.IntegerField()
    time = models.IntegerField()

class Location(models.Model):
    """
    Model representing geographical locations.
    """
    locationName = models.TextField()
    coordinatesX = models.FloatField()
    coordinatesY = models.FloatField()
    city = models.TextField()
    state = models.TextField()

class Users(models.Model):
    """
    Model representing users.
    """
    username = models.TextField()
    password = models.TextField()
    isAdmin = models.BooleanField()

class Stops(models.Model):
    """
    Model representing stops along the routes.
    """
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    busId = models.ForeignKey(Bus, on_delete=models.CASCADE)
    arrivalTime = models.DateTimeField()
    departureTime = models.DateTimeField()

class Bookings(models.Model):
    """
    Model representing user bookings.
    """
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    busId = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seatRow = models.IntegerField()
    seatCol = models.IntegerField()
    date = models.DateTimeField()
    fromStop = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name='fromstop')
    toStop = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name='tostop')
