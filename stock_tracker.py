import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}


def display_stock_prices():
    print("\nAvailable Stocks:")
    print("-" * 30)
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    print("-" * 30)


def add_stock():
    stock = input("Enter Stock Symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not available!")
        return

    try:
        qty = int(input("Enter Quantity: "))

        if qty <= 0:
            print("Quantity must be positive!")
            return

        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"{qty} shares of {stock} added successfully!")

    except ValueError:
        print("Invalid quantity!")


def remove_stock():
    stock = input("Enter Stock Symbol to Remove: ").upper()

    if stock in portfolio:
        del portfolio[stock]
        print("Stock removed successfully!")
    else:
        print("Stock not found in portfolio!")


def view_portfolio():
    if not portfolio:
        print("\nPortfolio is empty!")
        return

    total_value = 0

    print("\nPortfolio Summary")
    print("-" * 60)
    print(f"{'Stock':<10}{'Qty':<10}{'Price':<15}{'Value'}")
    print("-" * 60)

    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_value += value

        print(
            f"{stock:<10}{qty:<10}${stock_prices[stock]:<14}${value}"
        )

    print("-" * 60)
    print(f"Total Portfolio Value = ${total_value}")


def calculate_profit_loss():
    if not portfolio:
        print("Portfolio is empty!")
        return

    invested_amount = float(
        input("Enter Total Invested Amount ($): ")
    )

    current_value = sum(
        qty * stock_prices[stock]
        for stock, qty in portfolio.items()
    )

    profit_loss = current_value - invested_amount

    print("\nCurrent Value =", current_value)

    if profit_loss > 0:
        print("Profit =", profit_loss)
    elif profit_loss < 0:
        print("Loss =", abs(profit_loss))
    else:
        print("No Profit No Loss")


def save_to_csv():
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Stock", "Quantity"])

        for stock, qty in portfolio.items():
            writer.writerow([stock, qty])

    print("Portfolio saved to portfolio.csv")


def load_from_csv():
    try:
        with open("portfolio.csv", "r") as file:
            reader = csv.reader(file)

            next(reader)

            portfolio.clear()

            for row in reader:
                stock, qty = row
                portfolio[stock] = int(qty)

        print("Portfolio loaded successfully!")

    except FileNotFoundError:
        print("No saved portfolio found!")


while True:

    print("\n===== STOCK PORTFOLIO TRACKER =====")
    print("1. View Stock Prices")
    print("2. Add Stock")
    print("3. Remove Stock")
    print("4. View Portfolio")
    print("5. Calculate Profit/Loss")
    print("6. Save Portfolio")
    print("7. Load Portfolio")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_stock_prices()

    elif choice == "2":
        add_stock()

    elif choice == "3":
        remove_stock()

    elif choice == "4":
        view_portfolio()

    elif choice == "5":
        calculate_profit_loss()

    elif choice == "6":
        save_to_csv()

    elif choice == "7":
        load_from_csv()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")