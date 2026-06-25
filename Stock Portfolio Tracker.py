# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio_details = []

print("=== Stock Portfolio Tracker ===")

# Number of stocks to enter
n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input(f"\nEnter stock name {i + 1}: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock_name} - Quantity: {quantity}, Value: ${investment}"
        )

        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found in price list.")

# Display total investment
print("\n=== Portfolio Summary ===")
for detail in portfolio_details:
    print(detail)

print(f"\nTotal Investment Value: ${total_investment}")

# Save results to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("=== Portfolio Summary ===\n")
    for detail in portfolio_details:
        file.write(detail + "\n")
    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")2