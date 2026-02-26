# Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    # String representation -> str(obj) / print(obj)
    def __str__(self):
        return f"{self.currency} {self.amount}"

    # Integer conversion -> int(obj)
    def __int__(self):
        return int(self.amount)

    # Addition -> obj1 + obj2
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot add different currencies: {self.currency} and {other.currency}")
        return Currency(self.currency, self.amount + other.amount)

    # In-place addition -> obj1 += obj2
    def __iadd__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot add different currencies: {self.currency} and {other.currency}")
        self.amount += other.amount
        return self

c1 = Currency("USD", 100)
c2 = Currency("EUR", 50)

try:
    c3 = c1 + c2
    print(c3)
except ValueError as e:
    print(e)  # Cannot add different currencies: USD and EUR

#----------------------------------------------------------------------------------------------------

# Exercise 2: see the exercise_one.py and func.py files

#----------------------------------------------------------------------------------------------------

# Exercise 3: String Modules

import string
import random

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
print(random_string)

#----------------------------------------------------------------------------------------------------

# Exercise 4: Current Date

import datetime

current_date = datetime.date.today()
print(current_date)

#----------------------------------------------------------------------------------------------------

# Exercise 5: Amount of time left until January 1st

time_left = datetime.date(current_date.year + 1, 1, 1) - current_date
print("Amount of time left until January 1st: ", time_left)

#----------------------------------------------------------------------------------------------------

# Exercise 6: Birthday and minutes

def calculate_lifetime_minutes(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    lifetime_minutes = age * 365 * 24 * 60
    return lifetime_minutes
birthdate = datetime.date(2003, 11, 1)
minutes = calculate_lifetime_minutes(birthdate)
print(f"Lifetime minutes: {minutes}")

#----------------------------------------------------------------------------------------------------

# Exercise 7: Faker Module

from faker import Faker
users = []

def add_user(nbr_users):
    for _ in range(nbr_users):
        fake = Faker()
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code(),
        }
        users.append(user)

add_user(5)
for user in users:
    print(user)