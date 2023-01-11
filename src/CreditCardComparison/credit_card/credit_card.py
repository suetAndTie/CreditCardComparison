from abc import ABC, abstractmethod
import math

from CreditCardComparison.utils import string_to_datetime


CATEGORY_MAPPING = {
    'ATM Fee': 'Fees & Charges',
    # 'Air Travel': 'Travel',
    'Air Travel': 'Air Travel',
    'Alcohol & Bars': 'Food & Dining',
    'Amusement': 'Entertainment',
    'Auto & Transport': 'Auto & Transport',
    'Bank Fee': 'Fees & Charges',
    'Books': 'Shopping',
    'Books & Supplies': 'Shopping',
    'Business Services': 'Business Services',
    'Buy': 'Investments',
    'Cash & ATM': 'Uncategorized',
    'Charity': 'Gifts & Donations',
    'Clothing': 'Shopping',
    'Coffee Shops': 'Food & Dining',
    'Credit Card Payment': 'Transfer',
    'Deposit': 'Investments',
    'Dividend & Cap Gains': 'Investments',
    'Doctor': 'Health & Fitness',
    'Electronics & Software': 'Shopping',
    'Entertainment': 'Entertainment',
    'Eyecare': 'Health & Fitness',
    'Fast Food': 'Food & Dining',
    'Federal Tax': 'Taxes',
    'Fees & Charges': 'Fees & Charges',
    'Finance Charge': 'Financial',
    'Financial Advisor': 'Financial',
    'Food & Dining': 'Food & Dining',
    'Food Delivery': 'Food & Dining',
    # 'Gas & Fuel': 'Auto & Transport',
    'Gas & Fuel': 'Gas & Fuel',
    'Gift': 'Gifts & Donations',
    'Gifts & Donations': 'Gifts & Donations',
    # 'Groceries': 'Food & Dining',
    'Groceries': 'Groceries',
    'Gym': 'Health & Fitness',
    'Hair': 'Personal Care',
    'Health & Fitness': 'Health & Fitness',
    'Hobbies': 'Shopping',
    'Home Improvement': 'Home',
    'Home Services': 'Home',
    # 'Hotel': 'Travel',
    'Hotel': 'Hotel',
    'Income': 'Income',
    'Interest Income': 'Income',
    'Internet': 'Bills & Utilities',
    'Investment Transfer': 'Investments',
    'Investments': 'Investments',
    'Late Fee': 'Fees & Charges',
    'Laundry': 'Personal Care',
    'Misc Expenses': 'Misc Expenses',
    # 'Mortgage & Rent': 'Home',
    'Mortgage & Rent': 'Mortgage & Rent',
    'Movies & DVDs': 'Entertainment',
    'Parking': 'Auto & Transport',
    'Pharmacy': 'Health & Fitness',
    # 'Public Transportation': 'Auto & Transport',
    'Public Transportation': 'Public Transportation',
    'Reimbursement': 'Income',
    'Restaurants': 'Food & Dining',
    # 'Ride Share': 'Auto & Transport',
    'Ride Share': 'Ride Share',
    'Service Fee': 'Fees & Charges',
    'Shopping': 'Shopping',
    'State Tax': 'Taxes',
    'Television': 'Bills & Utilities',
    'Trade Commissions': 'Investments',
    'Transfer': 'Transfer',
    'Travel': 'Travel',
    # 'Utilities': 'Bills & Utilities',
    'Utilities': 'Utilities',
    'Vacation': 'Travel',
    'Venmo': 'Uncategorized',
}


class CreditCard(ABC):
    def __init__(self, start_date):
        if isinstance(start_date, str):
            start_date = string_to_datetime(start_date)
        self.start_date = start_date
        self.current_date = start_date
        self.annual_fee = self.get_annual_fee()
        self.benefit_dict = self.get_benefit_dict()
        self.point_multiplier_dict = self.get_point_multiplier_dict()
        self.point_limit_dict = self.get_point_limit_dict()
        self.combined_point_limit_dict = self.get_combined_point_limit_dict()
        self.point_dict = {}

    def calculate_remaining_category_points(self, mapped_category):
        limit = float('inf')
        for k, v in self.combined_point_limit_dict.items():
            if mapped_category in k:
                limit = min(limit, v)

        limit = min(limit, self.point_limit_dict.get(mapped_category, float('inf')))
        return max(
            0,
            limit - self.point_dict.get(mapped_category, 0),
        )

    def calculate_purchase_points(self, purchase):
        mapped_category = CATEGORY_MAPPING[purchase['Category']]
        return min(
            self.point_multiplier_dict[mapped_category] * int(purchase['Amount']),
            self.calculate_remaining_category_points(mapped_category),
        )

    def get_results(self):
        return {
            'Annual Fee': -self.annual_fee
            * math.ceil((self.current_date - self.start_date).days / 365),
            **{k: v / 100 for k, v in self.point_dict.items()},
        }

    def __call__(self, purchase):
        mapped_category = CATEGORY_MAPPING[purchase['Category']]

        if self.point_multiplier_dict.get(mapped_category, 0) == 0:
            return 0

        date = string_to_datetime(purchase['Date'])
        if date > self.current_date:
            self.current_date = date

        # calculate points
        points = self.calculate_purchase_points(purchase)
        self.point_dict[mapped_category] = self.point_dict.get(mapped_category, 0) + points

        # calculate benefits
        for benefit_name, benefit in self.benefit_dict.items():
            benefit_points = benefit(purchase)
            self.point_dict[benefit_name] = self.point_dict.get(benefit_name, 0) + benefit_points
            points += benefit_points

        return points

    @abstractmethod
    def get_annual_fee(self):
        # returns an annual fee in dollars
        return 0

    @abstractmethod
    def get_benefit_dict(self):
        # returns a dict of str -> benefit
        return {}

    def get_point_multiplier_dict(self):
        # returns the multiplier
        return {
            'Health & Fitness': 1,
            'Gifts & Donations': 1,
            'Taxes': 0,
            'Investments': 0,
            'Income': 0,
            'Financial': 0,
            'Food & Dining': 1,
            'Bills & Utilities': 1,
            'Uncategorized': 0,
            'Fees & Charges': 0,
            'Shopping': 1,
            'Auto & Transport': 1,
            'Transfer': 0,
            'Entertainment': 1,
            'Misc Expenses': 0,
            'Groceries': 1,
            'Business Services': 1,
            'Home': 0,
            'Travel': 1,
            'Personal Care': 1,
            'Mortgage & Rent': 0,
            'Gas & Fuel': 1,
            'Hotel': 1,
            'Air Travel': 1,
            'Ride Share': 1,
            'Public Transportation': 1,
            'Utilities': 1,
        }

    @abstractmethod
    def get_point_limit_dict(self):
        # return dict of mapped_category (str) to point limit (int)
        return {}

    def get_combined_point_limit_dict(self):
        # return dict of list of mapped_category (list[str]) to point limit (int)
        return {}
