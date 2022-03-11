from .stock import Stock

NUMBER_OF_STOCKS = 3

class Portfolio:
    def __init__(self):
        self.stocks = []
        self.__populate_stocks()

    def get_profit(self, start_date, end_date):
        initial_value = 0
        final_value = 0

        for stock in self.stocks:
            initial_value += stock.get_stock_price_on_date(start_date)
            final_value += stock.get_stock_price_on_date(end_date)

        return self.__calculate_annualized_return(initial_value, final_value)

    def display_stocks(self):
        for stock in self.stocks:
            print(f"{stock.name}: BP {stock.base_price} - DR {stock.decrease_rate} - IR {stock.increase_rate} - SC {stock.spike_chance} - SM {stock.spike_multiplier}")

    def __populate_stocks(self):
        for _ in range(NUMBER_OF_STOCKS):
            self.stocks.append(Stock())

    def __calculate_annualized_return(self, initial_value, final_value):
        try:
            return (final_value - initial_value) / initial_value * 100
        except:
            return 0
