class MoneyMachine:
    CURRENCY = '$'

    COIN_VALUE = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickels': 0.05,
        'pennies': 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: ")

    def insert_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUE:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUE[coin]
        return self.money_received

    def process_payment(self, price):
        self.insert_coins()
        if self.money_received < price :
            print("Sorry that's not enough money. Money refunded...")
            self.money_received = 0
            return False
        change = round(self.money_received - price, 2)
        print(f"Here is {self.CURRENCY}{change:.2f} in change.")
        self.profit += price
        return True
        