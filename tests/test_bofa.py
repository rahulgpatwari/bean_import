from bean_import.parsers.base import Transaction
from decimal import Decimal
from datetime import date

def test_result_is_decimal():
    t = Transaction(
        date = date(2026,5,15), 
        payee = "Dick Butkis", 
        narration = "George Pappadopolous", 
        amount = Decimal("100.12"), 
        currency = "USD", 
        source_account = "Liabilities:CreditCard:BofA", 
        destination_account = "Expenses:Shopping", 
        flag = "*"
        )
    assert isinstance(t.amount, Decimal)

