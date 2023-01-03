import numpy as np


class OptimalSpender:
    def __init__(self, credit_cards):
        self.credit_cards = credit_cards

    def __call__(self, purchases):
        for purchase in listify(purchases):
            credit_card = credit_card[
                np.argmax(
                    [
                        credit_card.get_purchase_points(purchase)
                        for credit_card in self.credit_cards
                    ]
                )
            ]
            credit_card.purchase(purchase)

        results = None  # TODO
        return results
