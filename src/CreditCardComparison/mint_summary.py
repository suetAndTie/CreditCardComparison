import os
import argparse
import pandas as pd

from credit_card import AltitudeGoCreditCard, BiltCreditCard, AmericanExpressGoldCreditCard


def main(input_fn, output_fn):
    if output_fn is None:
        output_fn = os.path.splitext(input_fn)[0] + '_output.csv'

    df = pd.read_csv(input_fn)

    # convert transaction to negative if you receive money
    df['Amount'] = df.apply(
        lambda row: row['Amount'] * -1 if row['Transaction Type'] == 'credit' else row['Amount'],
        axis=1,
    )
    transactions = df.groupby('Category')['Amount'].sum()
    transactions.to_csv(output_fn)

    purchases = df[df['Transaction Type'] == 'debit'].to_dict('records')

    results_dict = {}
    for card in [
        AltitudeGoCreditCard('1/1/2022'),
        BiltCreditCard('1/1/2022'),
        AmericanExpressGoldCreditCard('1/1/2022'),
    ]:
        for purchase in purchases:
            card(purchase)

        results = card.get_results()
        print(results)

    total = 0
    for k, v in results_dict.items():
        print(k, v)
        total += v
    print('total', total)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a summary for a Intuit Mint transaction csv.'
    )
    parser.add_argument(
        'input',
        type=str,
        help='The input csv file.',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='The output transcripton json file.',
        required=False,
        default=None,
    )
    args = parser.parse_args()
    main(args.input, args.output)
