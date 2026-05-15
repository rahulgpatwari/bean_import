from dataclasses import dataclass
from datetime import datetime, date
from decimal import Decimal
from abc import ABC, abstractmethod

@dataclass
class Transaction: 
    date: date
    payee: str
    narration: str
    amount: Decimal
    currency: str
    source_account: str
    destination_account: str
    flag: str


class BaseParser(ABC): 

    @abstractmethod
    def parse(self, filepath) -> list[Transaction]:
        ...
