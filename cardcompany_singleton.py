"""
1) 문제
카드 회사가 있습니다.
카드회사는 유일한 객체이고 회사 카드를 발급하면 항상 고유번호가 자동으로 생성됩니다.
10001부터 시작하여 카드가 생성될 때마다 10002, 10003 식으로 증가됩니다.
다음 코드가 수행되도록 Card 클래스와 CardCompany 클래스를 구현하세요.
"""

class Card:

    __card_num: int = 10001

    def __init__(self):
        self.user_card_num = Card.__card_num
        Card.__card_num += 1

    def get_user_card_num(self) -> int:
        return self.user_card_num

class CardCompany:

    __instance: 'CardCompany' = None

    @staticmethod
    def get_instance() -> 'CardCompany':
        if CardCompany.__instance is None:
            CardCompany.__instance = CardCompany()
        return CardCompany.__instance

    def create_card(self) -> Card:
        return Card()


def main():

    company: CardCompany = CardCompany.get_instance()

    card1: Card = company.create_card()
    card2: Card = company.create_card()

    print(card1.get_user_card_num())
    print(card2.get_user_card_num())

main()