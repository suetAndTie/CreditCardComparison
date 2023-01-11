import os
import argparse
import pandas as pd

from credit_card import (
    AltitudeGoCreditCard,
    BiltCreditCard,
    CashPlusCreditCard,
    BarclaysViewMastercardCreditCard,
)
from spender import Spender


def main(input_fn, output_fn):
    if output_fn is None:
        output_fn = os.path.splitext(input_fn)[0] + '_output.csv'

    df = pd.read_csv(input_fn)

    # convert transaction to negative if you receive money
    df['Amount'] = df.apply(
        lambda row: row['Amount'] * -1 if row['Transaction Type'] == 'credit' else row['Amount'],
        axis=1,
    )
    # Save out summary
    transactions = df.groupby('Category')['Amount'].sum()
    transactions.to_csv(output_fn)

    # only get valid purchases from credit card
    purchases = df[df['Transaction Type'] == 'debit'].to_dict('records')

    spender = Spender([AltitudeGoCreditCard('1/1/2020')])
    spender(purchases)
    results = spender.get_results()
    print('CURRENT')
    print(results)
    print('total', sum(results.values()))
    print()

    spender = Spender(
        [
            AltitudeGoCreditCard('1/1/2020'),
            BiltCreditCard('1/1/2022'),
            CashPlusCreditCard('1/1/2022'),
            BarclaysViewMastercardCreditCard('1/1/2020'),
        ]
    )
    spender(purchases)
    results = spender.get_results()
    print('NEW')
    print(results)
    print('total', sum(results.values()))


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
