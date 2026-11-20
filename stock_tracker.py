"""Simple stock portfolio tracker.

Uses a hardcoded dictionary of stock prices. User inputs stock symbols and
quantities; total investment value is displayed and optionally saved to a
.txt or .csv file.
"""
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 170,
    "META": 300,
}


def main():
    portfolio = {}
    print("Available stocks:", ", ".join(f"{k} (${v})" for k, v in STOCK_PRICES.items()))
    print("Enter stock symbols and quantities. Type 'done' when finished.\n")

    while True:
        name = input("Stock symbol (or 'done'): ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Unknown stock. Choose from:", list(STOCK_PRICES.keys()))
            continue
        try:
            qty = int(input("Quantity: "))
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
            continue
        if qty < 0:
            print("Quantity cannot be negative.")
            continue
        portfolio[name] = portfolio.get(name, 0) + qty

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    lines = []
    total = 0
    print("\n--- Portfolio Summary ---")
    for sym, qty in portfolio.items():
        price = STOCK_PRICES[sym]
        value = price * qty
        total += value
        line = f"{sym}: {qty} x ${price} = ${value}"
        lines.append(line)
        print(line)
    print(f"Total investment value: ${total}")

    save = input("\nSave result to file? (y/n): ").strip().lower()
    if save == "y":
        fmt = input("Format (txt/csv): ").strip().lower()
        if fmt == "csv":
            with open("portfolio.csv", "w") as f:
                f.write("Symbol,Quantity,Price,Value\n")
                for sym, qty in portfolio.items():
                    f.write(f"{sym},{qty},{STOCK_PRICES[sym]},{STOCK_PRICES[sym] * qty}\n")
                f.write(f"TOTAL,,,{total}\n")
            print("Saved to portfolio.csv")
        else:
            with open("portfolio.txt", "w") as f:
                f.write("\n".join(lines) + f"\nTotal investment value: ${total}\n")
            print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
