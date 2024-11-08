import pandas as pd
from django.core.management.base import BaseCommand
from clients.models import Client, Transaction
from django.db import transaction

class Command(BaseCommand):
    help = 'Load data from CSV and XLSX into the database'

    def handle(self, *args, **kwargs):
        # Use raw string literals (r"") to avoid issues with backslashes in paths
        clients_df = pd.read_csv(r"C:\Users\User\Desktop\Rick\MyDjangoProjects\data_engineering_project\clients.csv")
        transactions_df = pd.read_excel(r"C:\Users\User\Desktop\Rick\MyDjangoProjects\data_engineering_project\transactions.xlsx")

        # Clients data
        for _, row in clients_df.iterrows():
            client, created = Client.objects.get_or_create(
                client_id=row['client_id'],
                defaults={
                    'name': row['name'],
                    'email': row['email'],
                    'date_of_birth': row['date_of_birth'],
                    'country': row['country'],
                    'account_balance': row['account_balance']
                }
            )
        
        # Transactions data
        with transaction.atomic():
            for _, row in transactions_df.iterrows():
                client = Client.objects.get(client_id=row['client_id'])
                Transaction.objects.create(
                    transaction_id=row['transaction_id'],
                    client=client,
                    transaction_type=row['transaction_type'],
                    transaction_date=row['transaction_date'],
                    amount=row['amount'],
                    currency=row['currency']
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
