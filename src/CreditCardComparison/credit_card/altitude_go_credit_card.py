from functools import partial

from .credit_card import CreditCard
from CreditCardComparison.benefit import SignUpBenefit


class AltitudeGoCreditCard(CreditCard):
    category_point_dict = dict(
        ((k, v) for k, v in CreditCard.category_point_dict.items()),
        **{
            'Food & Dining': 4,
            'Gas & Fuel': 2,
            'Groceries': 2,
        }
    )
    benefit_class_dict = dict(
        ((k, v) for k, v in CreditCard.benefit_class_dict.items()),
        **{
            'Sign Up Benefit': partial(SignUpBenefit, points=20000, purchase_amount=1000, days=90),
        }
    )
