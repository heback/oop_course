class Fruit:

    def __init__(self, name: str):
        self.name = name


class Orange(Fruit):

    def __init__(
            self,
            orchard: str,
            date_picked: str,
            weight: float):
        self.name = 'orange'
        self.orchard = orchard
        self.date_picked = date_picked
        self.weight = weight


class Apple(Fruit):

    def __init__(
            self,
            date_picked: str,
            color: str,
            weight: float
    ):
        self.name = 'apple'
        self.date_picked = date_picked
        self.color = color
        self.weight = weight

