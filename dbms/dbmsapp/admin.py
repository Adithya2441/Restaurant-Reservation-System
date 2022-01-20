from atexit import register
from django.contrib import admin
from .models import Booking, Customer, Manager, Meal, Meal_Order, Meals, Meals_Order, Menu_NonVeg, Menu_Veg, Register, Restaurant, Table, Valet

admin.site.register(Register)
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Manager)
admin.site.register(Menu_Veg)
admin.site.register(Menu_NonVeg)
admin.site.register(Customer)
admin.site.register(Valet)
admin.site.register(Booking)
admin.site.register(Meals_Order)


