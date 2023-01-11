from functools import partial

from credit_card import CreditCard
from CreditCardComparison.benefit import SignUpBenefit, MonthlyCreditBenefit


class ChaseSapphirePreferredCreditCard(CreditCard):
    def get_annual_fee(self):
        return 95

    def get_benefit_dict(self):
        return {
            'Sign Up Benefit': SignUpBenefit(
                self.start_date, points=60000, purchase_amount=4000, months=3
            )
        }

    def get_point_multiplier_dict(self):
        point_multiplier_dict = super().get_point_multiplier_dict()
        point_multiplier_dict.update(
            {
                'Food & Dining': 3,
                'Air Travel': 5,
                'Travel': 5,
                'Hotel': 5,
            }
        )
        return point_multiplier_dict

    def get_point_limit_dict(self):
        return {}
