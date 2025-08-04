from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    CATEGORY_TYPES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPES)
    
    def __str__(self):
        return f"{self.name} ({self.type})"

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} - {self.user.username}"
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.amount} on {self.date}"
    
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    limit = models.DecimalField(max_digits=12, decimal_places=2)
    month = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.category.name} ({self.month})"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    deadline = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.user.username}" 