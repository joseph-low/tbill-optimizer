import pytz
import math
from datetime import datetime, timedelta


PRINCIPAL = 150000
INTEREST_RATE = 5/100
TRADE_FEE = 5
TIMEZONE = pytz.timezone('Australia/Sydney')


def compound_interest(principal, interest_rate, reinvest_cycles, compound_years):
    future_value = principal * (pow((1 + interest_rate / reinvest_cycles), (reinvest_cycles * compound_years)))
    interest_earned = future_value - principal
    return future_value, interest_earned


def next_optimal_startdate(days_to_earn_1k):
    current_datetime = datetime.now(TIMEZONE)
    next_best_startdate = current_datetime + timedelta(days=days_to_earn_1k)
    return next_best_startdate.strftime('%d %b %Y')


def default_earnings(reinvest_cycles, cycle_duration):
    annual_earnings = (PRINCIPAL * INTEREST_RATE) - TRADE_FEE
    daily_earnings = annual_earnings / 365
    total_earnings = daily_earnings * cycle_duration * reinvest_cycles
    rate_of_return = total_earnings / PRINCIPAL * 100
    return round(total_earnings, 2), round(rate_of_return, 2)


def optimized_earnings(reinvest_cycles, cycle_duration):
    new_principal = PRINCIPAL
    total_earnings = 0

    for i in range(reinvest_cycles):
        print(f"Principal for cycle #{(i+1)}: {new_principal}")
        annual_earnings = (new_principal * INTEREST_RATE) - TRADE_FEE
        daily_earnings = annual_earnings / 365
        cycle_earnings = cycle_duration * daily_earnings

        total_earnings += cycle_earnings
        new_principal += 1000
        print(f"Interest earned after cycle #{(i+1)}: ${round(cycle_earnings, 2)}")

    rate_of_return = total_earnings / PRINCIPAL * 100
    return round(total_earnings, 2), round(rate_of_return, 2)


def main():
    annual_earnings = (PRINCIPAL * INTEREST_RATE) - TRADE_FEE
    daily_earnings = annual_earnings / 365
    days_to_earn_1k = math.ceil(1000 / daily_earnings)
    reinvest_cycles = math.floor(365 / days_to_earn_1k)

    print("\n--------------------------- SUMMARY ---------------------------\n")
    print(f"Principal: ${round(PRINCIPAL, 2):,}")
    print(f"Interest rate: {INTEREST_RATE * 100}%")
    print(f"Days to earn next $1k: {days_to_earn_1k}")
    print(f"Number of times you can reinvest (per year): {reinvest_cycles}")
    print(f"Total duration: {days_to_earn_1k * reinvest_cycles} / 365 days")
    print(f"Look for next maturity date: {next_optimal_startdate(days_to_earn_1k)}")

    print("\n--------------------------- DEFAULT ---------------------------\n")
    standard_earnings, standard_ror = default_earnings(reinvest_cycles, days_to_earn_1k)
    print(f"Default Earnings: ${standard_earnings:,}      Default ROR: {standard_ror}%")

    print("\n--------------------------- OPTIMIZED ---------------------------\n")
    optimised_earnings, optimised_ror = optimized_earnings(reinvest_cycles, days_to_earn_1k)
    print(f"Optimised Earnings: ${optimised_earnings:,}      Optimised ROR: {optimised_ror}%")

    print("\n--------------------------- DIFFERENCE ---------------------------\n")
    earning_difference, ror_difference = round((optimised_earnings-standard_earnings), 2), round((optimised_ror-standard_ror), 2)
    print(f"Earnings Difference: ${earning_difference:,}      ROR Difference: {ror_difference}%\n")



if __name__ == '__main__':
    main()
