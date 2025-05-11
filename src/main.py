from time import sleep
import json, requests, os


# Make sure to set the environment variable before starting the application
API_KEY = os.getenv("CURRENCY_API_KEY")
# API_KEY = ""


def welcome_message():
    print("## Welcome to Currency Convert v2 - written by Felix Feichtinger")
    print("##")
    print("## This program uses the currency abbreviation format (3 letters) to determine which currency you want to convert from and to.")
    print("## For a comprehensive overview of all these abbreviations, please refer to the following website:")
    print("##")
    print("## https://www.yourdictionary.com/articles/currency-abbreviations")

    input("\n(Press Enter to proceed)")


def invalid_input_message():
    print("\nInvalid input. Please try again.")


def unsupported_currency_message():
    print("\nUnsupported currency. Please try again")


def get_convert_from():
    convert_from = input("\nPlease specify the currency you want to convert from [3 letter abbreviation]: ")

    # Input consists of 3 letters (valid)
    if len(convert_from) == 3 and convert_from.isalpha():
        convert_from = convert_from.upper()

        for currency in SUPPORTED_CURRENCIES:
            # Currency is valid and exists
            if convert_from == currency:
                return currency
        
        unsupported_currency_message()
        return get_convert_from()

    # Input is invalid
    invalid_input_message()
    return get_convert_from()


def get_convert_to():
    convert_to = input("\nPlease specify the currency you want to convert to [3 letter abbreviation]: ")

    # Input consists of 3 letters (valid)
    if len(convert_to) == 3 and convert_to.isalpha():
        convert_to = convert_to.upper()

        for currency in SUPPORTED_CURRENCIES:
            # Currency is valid and exists
            if convert_to == currency:
                return currency
        
        unsupported_currency_message()
        return get_convert_to()

    # Input is invalid
    invalid_input_message()
    return get_convert_to()


def get_amount():
    amount = input("\nPlease enter the amount to convert: ")
    
    if amount.isdigit():
        amount = int(amount)
        return amount
    
    invalid_input_message()
    return get_amount()


def get_continue_choice():
    continue_choice = input("\nWhat do you want to do now?\n(0) Exit\n(1) Convert again\n(2) Repeat with same currencies\n")
    if continue_choice == "":
        invalid_input_message()

        return get_continue_choice()
    
    try:
        continue_choice = int(continue_choice)

    except ValueError:
        continue_choice = ""

    match continue_choice:
        case 0:
            return continue_choice
        case 1:
            return continue_choice
        case 2:
            return continue_choice
        case _:
            invalid_input_message()
            return get_continue_choice()


def get_exchange_rate(from_cur):
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_cur}'

    api_response = requests.get(url)
    api_data = api_response.json()

    from_cur_rates = api_data.get('conversion_rates')

    return from_cur_rates


def get_supported_currencies_list():
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR'

    api_response = requests.get(url)
    api_data = api_response.json()

    rates = api_data.get('conversion_rates')
    rate_keys = list(rates.keys())

    return rate_keys


def get_supported_currencies_string():
    all_rates = get_supported_currencies_list()
    all_rates_string = ""

    for rate in all_rates:
        rate_index = all_rates.index(rate)
        all_rates_string += f"[{rate}]"

        if (rate_index + 1) % 8 == 0:
            all_rates_string += "\n"

    return all_rates_string


def check_if_unique(from_var, to_var):
    if from_var != to_var:
        return True
    
    print("\nCurrency to convert from and to are identical. Please try again.")
    return False


def currency_conversion(amount, conversion_factor):
    result = round(amount * conversion_factor, 2)
    return result



running = True
first_run = True
from_currency, to_currency, check_result = (None, None, None)

SUPPORTED_CURRENCIES = get_supported_currencies_list()


# Main Loop
while running:
    if first_run:
        welcome_message()
    
    first_run = False

    if not from_currency:
        from_currency = get_convert_from()

    if not to_currency:
        to_currency = get_convert_to()

    if not check_result:
        unique = check_if_unique(from_currency, to_currency)

    # From and to currency are unique, so proceed
    if unique:
        amount = get_amount()
        conversion_factors = get_exchange_rate(from_currency)
        to_currency_factor = conversion_factors.get(to_currency)

        result = currency_conversion(amount, to_currency_factor)
        proceed = input(f"\n## Input: {amount} {from_currency}\n## Result: {str(result)} {to_currency}\n(Press Enter to proceed)")

        continue_choice = get_continue_choice()

        if continue_choice == 0:
            print("\nExiting ...")
            running = False

        elif continue_choice == 1:
            print("\nStarting again ...")
            from_currency = None
            to_currency = None
            check_result = None

        elif continue_choice == 2:
            print("\nRepeating with same currencies ...")


    elif check_result == 1:
        from_currency, to_currency, check_result = (None, None, None)
