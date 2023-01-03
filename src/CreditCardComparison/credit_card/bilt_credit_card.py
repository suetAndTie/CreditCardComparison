from credit_card import CreditCard


class BiltCreditCard(CreditCard):
    category_point_dict = dict(
        ((k, v) for k, v in CreditCard.category_point_dict.items()),
        **{
            'Mortgage & Rent': 1,
            'Food & Dining': 3,
            'Hotel': 2,
            'Air Travel': 2,
        }
    )
    category_point_limit_dict = dict(
        ((k, v) for k, v in CreditCard.category_point_limit_dict.items()),
        **{
            'Mortgage & Rent': 50000,
        }
    )
