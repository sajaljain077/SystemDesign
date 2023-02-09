from abc import ABC, abstractmethod


class BasePizza(ABC):

    @abstractmethod
    def cost(self):
        pass

class FarmHouse(BasePizza):

    def cost(self):
        print("This is the Farm House Base Class")
        return 200


class Margherite(BasePizza):

    def cost(self):
        print("This is the Margherite Base Class")
        return 150


class VegDelight(BasePizza):

    def cost(self):
        print("This is the VegDelight Base Class")
        return 100


class ToppingDecorators(BasePizza):

    def cost(self):
        pass


class ExtraCheese(ToppingDecorators):

    def __init__(self, basePizza = BasePizza):
        self.basePizza = basePizza

    def cost(self):
        print("Adding Extra cheese toppings")
        return self.basePizza.cost()+10


class Mushrooms(ToppingDecorators):

    def __init__(self, basePizza = BasePizza):
        self.basePizza = basePizza

    def cost(self):
        print("Adding Mushrooms toppings")
        return self.basePizza.cost()+20


ec = Mushrooms(ExtraCheese(Margherite()))

print(ec.cost())