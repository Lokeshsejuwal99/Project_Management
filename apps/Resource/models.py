from django.db import models
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
    Description = models.TextField(null=True, blank=False)
    Category = models.CharField(max_length=100, null=True, blank=False)
    Size = models.CharField(max_length=30, choices=Inventory_size)
    Quantity = models.IntegerField()
    Unit_Price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=False
    )
    Total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=False
    )

    def save(self, *args, **kwargs):
        self.Total_price = self.Unit_Price * self.Quantity
        super().save(*args, **kwargs)

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
    Unit_price = models.DecimalField(
        decimal_places=2, max_digits=30, null=True, blank=False
    )
    Quantity = models.IntegerField(default=1)
    Condition = models.CharField(max_length=20, choices=Equipment_condition)
    Assigned_to = models.ManyToManyField(Employee_assigned)
    Total_price = models.DecimalField(
        decimal_places=2, max_digits=30, null=True, blank=False
    )

    def __str__(self):
        return self.Equipment_name


class Budget(models.Model):
    pay_method = (
        ("Bank", "Bank"),
        ("Check", "Check"),
        ("Cash", "Cash"),
        ("Credit Card", "Credit Card"),
    )
    Amount = models.DecimalField(
        decimal_places=2, max_digits=100, null=False, blank=True
    )
    Amount_in_words = models.CharField(max_length=400, null=False, blank=True)
    Payment_method = models.CharField(max_length=100, choices=pay_method)
    Date = models.DateTimeField(auto_now_add=True)
