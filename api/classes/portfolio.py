from .stock import Stock

class Portfolio:
    def __init__(self, assets):
        self.stocks = []

        self.__populate_stocks(assets)

    def get_stock(self, stock_name):
        for stock in self.stocks:
            if stock.name == stock_name:
                return stock

        return None

    def get_profit(self, start_date, end_date):
        initial_value = 0
        final_value = 0

        for stock in self.stocks:
            initial_value += stock.get_price_from_date(start_date)
            final_value += stock.get_price_from_date(end_date)

        return self.__calculate_annualized_return(initial_value, final_value)
    
    def add_stock(self, stock_name, stock_id):
        self.stocks.append(Stock(stock_name, stock_id))

    def remove_stock(self, stock_name):
        for stock in self.stocks:
            if stock.name == stock_name:
                self.stocks.remove(stock)

    def toggle_stock(self, stock_name, stock_id):
        stock = self.get_stock(stock_name)

        if stock is not None:
            self.remove_stock(stock_name)
        else:
            self.add_stock(stock_name, stock_id)

    def __populate_stocks(self, assets):
        for asset in assets:
            self.stocks.append(Stock(asset["name"], asset["id"]))

    def __calculate_annualized_return(self, initial_value, final_value):
        try:
            return (final_value - initial_value) / initial_value * 100
        except:
            return 0
