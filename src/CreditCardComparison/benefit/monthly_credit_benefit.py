from dateutil.relativedelta import relativedelta


from .benefit import Benefit
from CreditCardComparison.utils import string_to_datetime


class MonthlyCreditBenefit(Benefit):
    def __init__(self, start_date=None, monthly_points=None, company_list=None):
        super().__init__(start_date)
        if monthly_points is None:
            raise ValueError('Must specify points.')
        if company_list is None:
            company_list = []

        self.monthly_points = monthly_points
        self.monthly_complete = {}
        self.company_list = company_list

    def __call__(self, purchase):
        purchase_date = string_to_datetime(purchase['Date'])

        key = f'{purchase_date.year}/{purchase_date.month}'
        if not self.monthly_complete.get(key, False):
            if len(self.company_list):
                # TODO: make this more robust
                for company in self.company_list:
                    if company.lower() in purchase['Description'].lower():
                        self.monthly_complete[key] = True
                        return self.monthly_points
                return 0
            else:
                self.monthly_complete[key] = True
                return self.monthly_points
        else:
            return 0
