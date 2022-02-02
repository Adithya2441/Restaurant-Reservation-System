from asyncio.windows_events import NULL
from email.policy import default
from re import T
from sqlite3 import Date
from statistics import mode
from tkinter import CASCADE
from django.conf import settings
from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    class Meta:
        db_table = 'Register'


class Restaurant(models.Model):
    Restaurant_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Phone_No = models.CharField(max_length=12)
    Table_Price = models.IntegerField()
    Type = models.CharField(max_length=25)
    Image = models.ImageField(default=None)

    class Meta:
        db_table = 'Restaurant'


class Table(models.Model):
    Table_ID = models.AutoField(primary_key=True)
    Table_Type = models.CharField(max_length=20)
    No_Of_Seats = models.IntegerField()

    class Meta:
        db_table = 'Table'


class Manager(models.Model):
    Manager_ID = models.AutoField(primary_key=True)
    Manager_Name = models.CharField(max_length=50)
    No_Of_Waiters = models.IntegerField()
    Restaurant_ID = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Manager'


class Menu_Veg(models.Model):
    Item_ID_Veg = models.AutoField(primary_key=True)
    Item_Name = models.CharField(max_length=50)
    Item_Price = models.IntegerField()
    Cuisine_Type = models.CharField(max_length=50)
    Image = models.ImageField(default=None)

    class Meta:
        db_table = 'Menu_Veg'

class Menu_NonVeg(models.Model):
    Item_ID_NonVeg = models.AutoField(primary_key=True)
    Item_Name = models.CharField(max_length=50)
    Item_Price = models.IntegerField()
    Cuisine_Type = models.CharField(max_length=50)
    Image = models.ImageField(default=None)
    
    class Meta:
        db_table = 'Menu_NonVeg'

class Valet(models.Model):
    Valet_ID = models.AutoField(primary_key=True)
    Valet_Name = models.CharField(max_length=25)
    No_Of_Vehicles = models.IntegerField(default=0)
    Manager_ID = models.ForeignKey(Manager,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Valet'

class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    Customer_Name = models.CharField(max_length=25)
    Vehicle_Number = models.CharField(max_length=15,null=True,blank=True)
    Email = models.EmailField(default=None)
    Phone_No = models.CharField(max_length=12)
    Valet_ID = models.ForeignKey(Valet,on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        db_table = 'Customer'

class Booking(models.Model):
    Booking_ID = models.AutoField(primary_key=True)
    Date = models.DateField()
    Time = models.TimeField()
    Restaurant_ID = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer,on_delete=models.CASCADE)
    Table_ID = models.ForeignKey(Table,on_delete=models.CASCADE)
    Manager_ID = models.ForeignKey(Manager,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Booking'
    
    def get_absolute_url(self):
        return "confirmed/{id}".format(id=self.Booking_ID)

class Meals_Order(models.Model):
    Meal_No = models.AutoField(primary_key=True)
    Item_Veg = models.ForeignKey(Menu_Veg,on_delete=models.CASCADE,default=None,null=True,blank=True)
    Item_NonVeg = models.ForeignKey(Menu_NonVeg,on_delete=models.CASCADE,default=None,null=True,blank=True)
    Quantity = models.IntegerField(default = 1)
    Booking_ID = models.ForeignKey(Booking,on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = 'Meals_Order'
