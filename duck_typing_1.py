class Duck:
    def quack(self):
        return "Quack"


class Person:
    def quack(self):
        return "I'm quacking like a duck!"


def make_it_quack(duck):
    print(duck.quack())


duck = Duck()
person = Person()

make_it_quack(duck)    # Output: Quack
make_it_quack(person)  # Output: I'm quacking like a duck!

