def get_interest_rate() -> float:
    rate_str = input("Enter the annual interest rate: ").strip()
    if rate_str.endswith("%"):
        rate_str = rate_str[:-1]

    try:
        return float(rate_str)
    except ValueError:
        raise ValueError("Invalid interest rate entered.")


def calculate_monthly_mortgage(loan_amount: float, annual_rate_percent: float, years: int) -> float:
    """Return the monthly payment for a mortgage.

    Uses the standard amortization formula. If the interest rate is zero,
    the payment is simply the loan amount divided by the number of payments.
    """

    n_payments = years * 12
    monthly_rate = (annual_rate_percent / 100.0) / 12.0

    if monthly_rate == 0:
        return loan_amount / n_payments

    power = (1 + monthly_rate) ** n_payments
    return loan_amount * (monthly_rate * power) / (power - 1)


def main():
    print("*" * 66)
    print(" HOME MORTGAGE PAYMENT CALCULATOR ".center(66))
    print("*" * 66)
    print(
        "In this program, we will calculate your monthly mortgage payment. You will enter the cost of the home\n"
        "you are buying and how much of a down payment you are making. You will then enter the annual interest\n"
        "rate as well as the length of the loan in years. The program will take this information and compute your\n"
        "monthly mortgage payment. If your down payment is less than 20% of the cost of the home, you will\n"
        "have to pay a mortgage insurance fee of $100 per month."
    )

    try:
        home_cost = float(input("Enter the cost of the home: $ "))
        down_payment = float(input("Enter the down payment you are making: $ "))
        annual_rate = get_interest_rate()
        years = int(input("Enter the length of the loan in years: "))
    except ValueError as exc:
        print(f"Input error: {exc}")
        return

    loan_amount = home_cost - down_payment
    if loan_amount < 0:
        print("Down payment cannot exceed the cost of the home.")
        return

    monthly_mortgage = calculate_monthly_mortgage(loan_amount, annual_rate, years)

    if down_payment < 0.20 * home_cost:
        mortgage_insurance = 100.0
    else:
        mortgage_insurance = 0.0

    total_per_month = monthly_mortgage + mortgage_insurance

    print("\nHere is a summary of your loan:")
    print(f"{'Loan amount:':20s} $ {loan_amount:,.2f}")
    print(f"{'Annual interest rate:':20s} {annual_rate:.1f}%")
    print(f"{'Number of years:':20s} {years}")
    print(f"{'Monthly mortgage:':20s} $ {monthly_mortgage:,.2f}")
    print(f"{'Mortgage insurance:':20s} $ {mortgage_insurance:,.2f}")
    print(f"{'Total per month:':20s} $ {total_per_month:,.2f}")
    print("*" * 66)
    print("Thank you for using this program".center(66))
    print("*" * 66)


if __name__ == "__main__":
    main()
