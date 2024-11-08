# clients/urls.py
from django.urls import path
from .views import TransactionListView

urlpatterns = [
    path('transactions/<int:client_id>/', TransactionListView.as_view(), name='transaction-list'),
]
