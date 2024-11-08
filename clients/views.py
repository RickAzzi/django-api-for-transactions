from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from django.utils.dateparse import parse_date
from rest_framework.exceptions import ValidationError


class TransactionListView(APIView):
    def get(self, request, client_id):
        # Ensure client_id is provided
        if not client_id:
            raise ValidationError("Client ID is required.")

        # Validate start_date and end_date query parameters
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        if start_date and not parse_date(start_date):
            raise ValidationError("Invalid start date format. Expected YYYY-MM-DD.")
        if end_date and not parse_date(end_date):
            raise ValidationError("Invalid end date format. Expected YYYY-MM-DD.")
        
        # Fetch and filter transactions by client_id and date range
        transactions = Transaction.objects.filter(client_id=client_id)
        if start_date and end_date:
            transactions = transactions.filter(date__range=[start_date, end_date])

        # Serialize and return the transactions
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
