import yfinance as yf


class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares, purchase_price):
        self.portfolio[ticker] = {
            'shares': shares,
            'purchase_price': purchase_price,
            'current_price': 0,
            'value': 0,
            'gain': 0
        }

    def update_prices(self):
        for ticker in self.portfolio:
            stock = yf.Ticker(ticker)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            self.portfolio[ticker]['current_price'] = current_price
            self.portfolio[ticker]['value'] = self.portfolio[ticker]['shares'] * current_price
            self.portfolio[ticker]['gain'] = (current_price - self.portfolio[ticker]['purchase_price']) * \
                                             self.portfolio[ticker]['shares']

    def display_portfolio(self):
        print(f"{'Ticker':<10} {'Shares':<10} {'Purchase Price':<15} {'Current Price':<15} {'Value':<10} {'Gain':<10}")
        for ticker, data in self.portfolio.items():
            print(
                f"{ticker:<10} {data['shares']:<10} {data['purchase_price']:<15} {data['current_price']:<15.2f} {data['value']:<10.2f} {data['gain']:<10.2f}")

    def portfolio_summary(self):
        total_value = sum(stock['value'] for stock in self.portfolio.values())
        total_gain = sum(stock['gain'] for stock in self.portfolio.values())
        print("\nPortfolio Summary:")
        print(f"Total Value: ${total_value:.2f}")
        print(f"Total Gain: ${total_gain:.2f}")


if __name__ == "__main__":
    tracker = StockPortfolioTracker()

    # Adding stocks to the portfolio
    tracker.add_stock('AAPL', 10, 150)
    tracker.add_stock('MSFT', 5, 250)
    tracker.add_stock('TSLA', 2, 700)

    # Update current prices and display portfolio
    tracker.update_prices()
    tracker.display_portfolio()
    tracker.portfolio_summary()
