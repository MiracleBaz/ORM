from django.contrib import admin
from .models import Loan_DB

class Loan_DBAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'borrower', 'amount', 'loan_date')  # Customize with your fields
    search_fields = ('borrower', 'loan_id')  # Fields you want to be searchable
    list_filter = ('loan_date',)  # Fields to filter by

admin.site.register(Loan_DB, Loan_DBAdmin)
