from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExpenseIncome(models.Model):
    TRANSACTION_CHOICES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    TAX_TYPE_CHOICE =[
        ('flat','Flat'),
        ('percentage','Percentage'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_type = models.CharField(max_length=10,choices=TRANSACTION_CHOICES)
    tax = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    tax_type = models.CharField(max_length=10,choices=TAX_TYPE_CHOICE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def calc_total(self):
        if self.tax_type == 'flat':
            return self.amount+self.tax
        else:
            return self.amount+(self.amount * self.tax / 100)
    
    def __str__(self):
        return f"{self.title} - {self.transaction_type} - {self.amount}"