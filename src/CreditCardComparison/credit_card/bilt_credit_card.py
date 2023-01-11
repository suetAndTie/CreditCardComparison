from credit_card import CreditCard


class BiltCreditCard(CreditCard):
    def get_annual_fee(self):
        return 0

    def get_benefit_dict(self):
        return {}

    def get_point_multiplier_dict(self):
        point_multiplier_dict = super().get_point_multiplier_dict()
        point_multiplier_dict.update(
            {
                'Mortgage & Rent': 1,
                'Food & Dining': 3,
                'Hotel': 2,
                'Air Travel': 2,
            }
        )
        return point_multiplier_dict

    def get_point_limit_dict(self):
        return {
            'Mortgage & Rent': 50000,
        }
