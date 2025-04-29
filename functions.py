#libraries
import numpy as np

#ratio function, returns None if either value missing or denominator is zero
def get_ratio(numerator, denominator):
    if numerator is None or denominator is None:
        return None
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None

#P/E ratio function
def pe_ratio(price, eps):
    return get_ratio(price, eps)

#forward P/E ratio function
def forward_pe(price, forward_eps):
    return get_ratio(price, forward_eps)

#P/B ratio function
def price_to_book(price, book_value_per_share):
    return get_ratio(price, book_value_per_share)

#dividend yield (%) function, returns 'None' if divide by zero
def dividend_yield(dividend_per_share, current_price):
    if dividend_per_share is None or current_price is None:
        return None
    try:
        return (dividend_per_share / current_price) * 100
    except ZeroDivisionError:
        return None

#price formatting function, to 2 decimal places or 'None' if invalid
def format_price(price):
    if price is None:
        return None
    try:
        return round(float(price), 2)
    except (ValueError, TypeError):
        return None

#format decimal to percentage function, to 2 decimal places or 'None' if invalid
def format_percentage(value):
    if value is None:
        return None
    try:
        return f"{value * 100:.2f}%"
    except (ValueError, TypeError):
        return None
