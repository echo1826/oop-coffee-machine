class CoffeeMaker:
    def __init__(self, water=300, coffee=100, milk=200):
        self.resources = {
            'water': water,
            'coffee': coffee,
            'milk': milk,
        }

    def report(self):
        for ingredient_name in self.resources:
            print(f"{ingredient_name}: {self.resources[ingredient_name]}")

    def resources_suffcient(self, order):
        for item in order.ingredients:
            if self.resources[item] < order.ingredients[item]:
                return False
        return True

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy!")
