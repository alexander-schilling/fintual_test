import random
import string

def get_random_stock_name(name_length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(name_length))

def get_random_stock_base_price():
    return random.randint(1, 100) + random.random()

class Stock:
    def __init__(self):
        self.name = get_random_stock_name(3)
        self.base_price = get_random_stock_base_price()
        self.decrease_rate = -random.uniform(0, 0.25)
        self.increase_rate = random.uniform(0.25, 0.75)
        self.spike_chance = random.uniform(0, 0.25)
        self.spike_multiplier = random.uniform(1.0, 3.0)
        self.price_history = {}

    def get_stock_price_on_date(self, date):
        date_key = date.strftime('%Y-%m-%d')

        if date_key in self.price_history:
            return self.price_history[date_key]

        change_rate = random.uniform(self.decrease_rate, self.increase_rate)
        price_change = self.base_price * change_rate
        should_spike = random.random() < self.spike_chance

        if should_spike:
            price_change *= self.spike_multiplier

        yty_increase = date.year / 2000
        yty_change = (yty_increase ** 2) * self.base_price

        final_price = (
            self.base_price +
            price_change +
            yty_change
        )

        self.price_history[date_key] = final_price

        return final_price
