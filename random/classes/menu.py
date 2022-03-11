from .portfolio import Portfolio
from tools.utils import string_to_date

class Menu:
    def __init__(self, portfolio):
        self.running = False
        self.portfolio = portfolio
        self.options = {
            "1": {
                "function": self.__get_portfolio_profit,
                "label": "Get portfolio profit by date"
            },
            "2": {
                "function": self.__display_stocks,
                "label": "Display stocks"
            },
            "3": {
                "function": self.__change_portfolio,
                "label": "Change portfolio"
            },
            "0": {
                "function": self.exit_menu,
                "label": "Exit"
            }
        }

    def run(self):
        self.running = True

        while self.running:
            self.__display_menu()
            choice = input("Enter your choice: ")
            self.__handle_choice(choice)

    def exit_menu(self):
        self.running = False

    def __display_menu(self):
        print()
        for option in self.options:
            print(f"{option}. {self.options[option]['label']}")
        print()

    def __handle_choice(self, choice):
        try:
            self.options[choice]["function"]()
        except:
            print("Invalid choice, try again...")

    def __get_portfolio_profit(self):
        try:
            start_date = string_to_date(input("Enter start date (YYYY-MM-DD): "))
            end_date = string_to_date(input("Enter end date (YYYY-MM-DD): "))
        except:
            print("Invalid date, try again...")
            return

        try:
            print(f"Annualized return: {self.portfolio.get_profit(start_date, end_date)}%")
        except Exception as e:
            print(e)

    def __display_stocks(self):
        print()
        print("Current stocks:")
        self.portfolio.display_stocks()

    def __change_portfolio(self):
        self.portfolio = Portfolio()
        print("New portfolio created")
