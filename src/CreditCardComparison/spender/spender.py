import numpy as np

from CreditCardComparison.utils import listify


class Spender:
    def __init__(self, credit_card_list):
        self.credit_card_list = credit_card_list

    def get_results(self):
        results_dict = {}
        for credit_card in self.credit_card_list:
            results = credit_card.get_results()

            for k, v in results.items():
                results_dict[k] = results_dict.get(k, 0) + v

        return results_dict

    def __call__(self, purchases):
        for purchase in listify(purchases):
            credit_card = self.credit_card_list[
                np.argmax(
                    [
                        credit_card.calculate_purchase_points(purchase)
                        for credit_card in self.credit_card_list
                    ]
                )
            ]
            credit_card(purchase)
