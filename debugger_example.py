class Taco:
    def __init__(self, filling) -> None:
        self.filling = filling

    def get_filling(self):
        return self.filling


class Person:
    def __init__(self, name, hungry=True) -> None:
        self.name = name
        self.hungry = hungry
        self.taco = None

    def give_taco(self, taco):
        self.taco = taco

    def eat(self):
        if self.hungry:
            if self.taco is not None:
                print("Person " + self.name + " ate a " + self.taco.get_filling() + " taco")
                self.hungry = False
            else:
                print("Person " + self.name + " has no food to eat")
        else:
            print("Person " + self.name + " is not hungry")


if __name__ == "__main__":
    fish_taco = Taco(1)
    joe = Person("Joe", hungry=True)
    joe.give_taco(fish_taco)
    joe.eat()
