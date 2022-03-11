from tools.utils import string_to_date
from tools.assets import ASSETS

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
                "function": self.__change_stocks,
                "label": "Change stocks"
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

        i = 1
        for asset in ASSETS:
            chosen = self.portfolio.get_stock(asset["name"])
            print(f"[ {'X' if chosen else ' ' } ] {i}. {asset['name']}")
            i += 1

        print("0. Go back")
        print()
    
    def __change_stocks(self):
        while True:
            self.__display_stocks()

            stock_choice = input("Write the number of the stock you want to toggle: ")

            if stock_choice == "0":
                break
            else:
                try:
                    stock_choice = int(stock_choice)
                except:
                    print("Invalid stock, try again...")
                    continue

                if stock_choice < 1 or stock_choice > len(ASSETS):
                    print("Invalid stock, try again...")
                    continue

                try:
                    asset = ASSETS[stock_choice - 1]
                    self.portfolio.toggle_stock(asset["name"], asset["id"])
                except Exception as e:
                    print(e)
