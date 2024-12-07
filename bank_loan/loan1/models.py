from django.db import models

class Loan_DB(models.Model):
    loan_id = models.CharField(max_length=50)
    borrower = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_date = models.DateField()

    def __str__(self):
        return self.loan_id
