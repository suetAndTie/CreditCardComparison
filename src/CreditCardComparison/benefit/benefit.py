from abc import ABC, abstractmethod
from datetime import datetime

from ..utils import string_to_datetime


class Benefit(ABC):
    def __init__(self, start_date=None):
        if start_date is None:
            raise ValueError('Must specify start date.')
        if isinstance(start_date, str):
            start_date = string_to_datetime(start_date)
        self.start_date = start_date

    @abstractmethod
    def __call__(self, purchase):
        return 0
