from functools import partial

from .credit_card import CreditCard
from CreditCardComparison.benefit import SignUpBenefit, MonthlyCreditBenefit


class AmericanExpressGoldCreditCard(CreditCard):
    annual_fee = 250
    category_point_dict = dict(
        ((k, v) for k, v in CreditCard.category_point_dict.items()),
        **{
            'Food & Dining': 4,
            'Groceries': 4,
            'Air Travel': 3,
        }
    )
    benefit_class_dict = dict(
        ((k, v) for k, v in CreditCard.benefit_class_dict.items()),
        **{
            'Sign Up Benefit': partial(
                SignUpBenefit, points=90000, purchase_amount=4000, months=6
            ),
            'Uber Cash Monthly Benefit': partial(
                MonthlyCreditBenefit,
                monthly_points=1000,
            ),
            'Dining Credit Monthly Benefit': partial(
                MonthlyCreditBenefit,
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
    )
