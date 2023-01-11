from credit_card import CreditCard


class BarclaysViewMastercardCreditCard(CreditCard):
    def get_annual_fee(self):
        return 0

    def get_benefit_dict(self):
        return {}

    def get_point_multiplier_dict(self):
        point_multiplier_dict = super().get_point_multiplier_dict()
        point_multiplier_dict.update(
            {
                'Food & Dining': 3,
                'Internet': 2,
                'Television': 2,
                'Groceries': 2,
            }
        )
        return point_multiplier_dict

    def get_point_limit_dict(self):
        return {}
