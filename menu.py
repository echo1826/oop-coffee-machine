class MenuItem:
    def __init__(self, name, price, water, coffee, milk):
        self.name = name
        self.price = price
        self.ingredients = {
            'water': water,
            'coffee': coffee,
            'milk': milk
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem('espresso', 1.5, 50, 18, 0),
            MenuItem('latte', 2.5, 200, 24, 150),
            MenuItem('cappuccino', 3.0, 250, 24, 100)
        ]

