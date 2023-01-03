from dateutil.relativedelta import relativedelta


from .benefit import Benefit
from CreditCardComparison.utils import string_to_datetime


class SignUpBenefit(Benefit):
    def __init__(self, start_date=None, points=None, purchase_amount=None, months=None, days=None):
        super().__init__(start_date)
        if points is None:
            raise ValueError('Must specify points.')
        if purchase_amount is None:
            raise ValueError('Must specify purchase amount.')
        if months is None and days is None:
            raise ValueError('Must specify either months or days.')
        if months is not None and days is not None:
            raise ValueError('Cannot specify both months and days.')

        self.points = points
        self.purchase_amount = purchase_amount
        self.months = months
        self.days = days
        self.purchase_sum = 0
        self.complete = False

    def __call__(self, purchase):
        purchase_date = string_to_datetime(purchase['Date'])
        if self.months is not None:
            valid_date = purchase_date <= self.start_date + relativedelta(months=self.months)
        elif self.days is not None:
            valid_date = purchase_date <= self.start_date + relativedelta(days=self.days)
        else:
            raise ValueError('Must specify either months or days.')

        self.purchase_sum += purchase['Amount']
        if not valid_date:
            return 0
        elif valid_date and self.complete:
            return 0
        else:
            if self.purchase_sum >= self.purchase_amount:
                self.complete = True
            return self.points
