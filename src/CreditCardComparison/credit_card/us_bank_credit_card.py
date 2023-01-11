from functools import partial

from .credit_card import CreditCard
from CreditCardComparison.benefit import SignUpBenefit


class AltitudeGoCreditCard(CreditCard):
    def get_annual_fee(self):
        return 0

    def get_benefit_dict(self):
        return {
            'Sign Up Benefit': SignUpBenefit(
                self.start_date, points=20000, purchase_amount=1000, days=90
            )
        }

    def get_point_multiplier_dict(self):
        point_multiplier_dict = super().get_point_multiplier_dict()
        point_multiplier_dict.update(
            {
                'Food & Dining': 4,
                'Gas & Fuel': 2,
                'Groceries': 2,
            }
        )
        return point_multiplier_dict

    def get_point_limit_dict(self):
        return {}


class CashPlusCreditCard(CreditCard):
    def get_annual_fee(self):
        return 0

    def get_benefit_dict(self):
        return {
            'Sign Up Benefit': SignUpBenefit(
                self.start_date, points=20000, purchase_amount=1000, days=90
            )
        }

    def get_point_multiplier_dict(self):
        point_multiplier_dict = super().get_point_multiplier_dict()
        point_multiplier_dict.update(
            {
                'Utilities': 5,
                'Ride Share': 5,
                'Public Transportation': 5,
                'Groceries': 2,
                'Hotel': 5,
                'Air Travel': 5,
            }
        )
        return point_multiplier_dict

    def get_point_limit_dict(self):
        return {}

    def get_combined_point_limit_dict(self):
        return {
            ('Utilities', 'Ride Share', 'Public Transportation'): 10000 * 4,
        }
