stock_prices = {"AAPL": 180, "TSLA": 250, "INFY": 1500}
portfolio = {}
total = 0

while True:
    stock = input("Enter stock name (or 'done'): ").upper()
    if stock == "DONE":
        break
    qty = int(input(f"Enter quantity for {stock}: "))
    if stock in stock_prices:
        portfolio[stock] = qty
        total += stock_prices[stock] * qty

print("Total Investment:", total)
