from classes.portfolio import Portfolio
from classes.menu import Menu

def main():
    portfolio = Portfolio()

    menu = Menu(portfolio)
    menu.run()

main()
