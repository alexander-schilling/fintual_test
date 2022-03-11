from classes.portfolio import Portfolio
from classes.menu import Menu
from tools.assets import ASSETS

def main():
    portfolio = Portfolio(ASSETS)
    menu = Menu(portfolio)

    menu.run()

main()
