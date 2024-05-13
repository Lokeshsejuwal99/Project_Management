from django.db import models
# from .publisher import publish_inventory_created_event

# Create your models here.


class Employee_assigned(models.Model):
    Employee_id = models.IntegerField()
    Employee_name = models.CharField(max_length=30)
    Employee_email = models.EmailField(max_length=254)
    Employee_phone = models.IntegerField()
    Employee_address = models.CharField(max_length=30)

    def __str__(self):
        return self.Employee_name
    

class Inventory(models.Model):
    Inventory_size = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    )

    Name = models.CharField(max_length=30)
    Quantity = models.IntegerField()
    size = models.CharField(max_length=30, choices=Inventory_size)
    Client_name = models.CharField(max_length=20)
    Address = models.CharField(max_length=30)
    Phone = models.IntegerField()
    Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.Name
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         # Publish event when a new inventory item is created
    #         publish_inventory_created_event(self)
    #     super().save(*args, **kwargs)


class Equipments(models.Model):
    Equipment_condition = (
        ("New", "New"),
        ("Used", "Used"),
        ("Damaged", "Damaged"),
        ("Broken", "Broken"),
    )

    Equipement_id = models.IntegerField()
    Equipment_name = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=1)
    Condition = models.CharField(max_length=20, choices=Equipment_condition)
    Assigned_to = models.ManyToManyField(Employee_assigned)
    
    def __str__(self):
        return self.Equipment_name