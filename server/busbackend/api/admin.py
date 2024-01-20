from django.contrib import admin
from .models import *

admin.site.register(Bookings)
admin.site.register(Bus)
admin.site.register(Routes)
admin.site.register(Location)
admin.site.register(Users)
admin.site.register(Stops)