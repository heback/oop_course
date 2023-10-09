from datetime import datetime


class Fruit:

    def __init__(self, name: str):
        self.name = name


class Orange(Fruit):

    def __init__(
            self,
            orchard: str,
            date_picked: str,
            weight: float):
        super().__init__('orange')
        self.orchard = orchard
        self.date_picked = date_picked
        self.weight = weight

    def __str__(self):
        return f'생산지: {self.orchard}, 수확일자: {self.date_picked}, 무게: {self.weight}'


class Apple(Fruit):

    def __init__(
            self,
            date_picked: str,
            color: str,
            weight: float
    ):
        super().__init__('apple')
        self.date_picked = date_picked
        self.color = color
        self.weight = weight

    def __str__(self):
        return f'수확일자: {self.date_picked}, 색깔: {self.color}, 무게: {self.weight}'


class Basket:

    def __init__(self, amount: int, orchard:str,weight: float):
        date = datetime.now().date()
        self.oranges: list[Orange] = [Orange(orchard, date, weight) for _ in range(amount) ]

    def __str__(self):
        return f'오렌지 개수: {len(self.oranges)}'


class Barrel:

    def __init__(self, amount: int, color:str, weight: float):
        date = datetime.now().date()
        self.apples: list[Apple] = [Apple(date, color, weight) for _ in range(amount)]

    def adds(self, amount: int, color:str, weight: float):
        date = datetime.now().date()
        self.apples.extend([Apple(date, color, weight) for _ in range(amount)])

    def __str__(self):
        return f'사과 개수: {len(self.apples)}'


class Sales:

    def __init__(self, fruit_type: str, location: str, amount: int):
        self.time = datetime.now()
        self.fruit_type = fruit_type
        self.location = location
        self.amount = amount

    def __str__(self):
        return f'{self.fruit_type} {self.location} {self.amount}'


class InventoryManagement:

    __baskets: list[Basket] = []
    __barrels: list[Apple] = []
    __sales: list[Sales] = []

    def add_baskets(self, baskets: int, amount: int, orchard:str,  weight: float) -> 'InventoryManagement':
        for _ in range(baskets):
            self.__baskets.append(Basket(amount, orchard, weight))
        return self

    def add_basket(self, basket: Basket) -> 'InventoryManagement':
        self.__baskets.append(basket)
        return self

    def add_barrels(self, barrels: int, amount: int, color: str, weight: float) -> 'InventoryManagement':
        for _ in range(barrels):
            self.__barrels.append(Barrel(amount, color, weight))
        return self

    def add_barrel(self, barrel: Barrel) -> 'InventoryManagement':
        self.__barrels.append(barrel)
        return self

    def check_baskets(self) -> int:
        return len(self.__baskets)

    def check_barrels(self) -> int:
        return len(self.__barrels)

    def sales_basket(self, baskets: int, location: str):
        if baskets <= self.check_baskets():
            self.__sales.append(Sales('Orange', location, baskets))
            self.__baskets.pop()
        else:
            print(f'현재 오렌지 재고량: {self.check_baskets()}, 요청하신 거래는 거절되었습니다.')

    def sales_barrel(self, barrels: int, location: str):
        if barrels <= self.check_barrels():
            self.__sales.append(Sales('Apple', location, barrels))
            self.__barrels.pop()
        else:
            print(f'현재 사과 재고량: {self.check_barrels()}, 요청하신 거래는 거절되었습니다.')

    def print_report(self):
        print('오렌지 재고')
        for o in self.__baskets:
            print(o)
        print('-'*50)
        print('사과 재고')
        for o in self.__barrels:
            print(o)
        print('-' * 50)
        print('판매 이력')
        for o in self.__sales:
            print(o)
        print('-' * 50)

def main():
    b1 = Basket(30, '청송',  300.0)
    b2 = Basket(20, '청송',  500.0)
    a1 = Barrel(20, '빨강', 100.0)
    a1.adds(10, '파랑', 120.0)

    inventory = InventoryManagement().add_basket(b1).add_basket(b2).add_barrel(a1)

    inventory.sales_basket(1, '대구')
    inventory.sales_barrel(4, '대구')

    inventory.add_baskets(10, 30, '청송', 200.0)
    inventory.add_barrels(15, 30, '빨강', 120.0)

    inventory.print_report()


if __name__ == '__main__':
    main()
