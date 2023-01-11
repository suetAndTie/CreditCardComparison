from functools import partial

from .credit_card import CreditCard
from CreditCardComparison.benefit import SignUpBenefit, MonthlyCreditBenefit


class AmericanExpressGoldCreditCard(CreditCard):
    def get_annual_fee(self):
        return 250

    def get_benefit_dict(self):
        return {
            'Sign Up Benefit': SignUpBenefit(
                self.start_date, points=90000, purchase_amount=4000, months=6
            ),
            'Uber Cash Monthly Benefit': MonthlyCreditBenefit(
                self.start_date,
                monthly_points=1000,
            ),
            'Dining Credit Monthly Benefit': MonthlyCreditBenefit(
                self.start_date,
                monthly_points=1000,
                company_list=[
                    'Grubhub',
                    'The Cheesecake Factory',
                    'Goldbelly',
                    'Wine.com',
                    'Milk Bar',
                    'Shake Shack',
                ],
            ),
        }

    def get_point_multiplier_dict(self):
        point_multiplier_dict = super().get_point_multiplier_dict()
        point_multiplier_dict.update(
            {
                'Food & Dining': 4,
                'Groceries': 4,
                'Air Travel': 3,
            }
        )
        return point_multiplier_dict

    def get_point_limit_dict(self):
        return {}
