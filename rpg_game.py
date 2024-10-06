import random
import pickle
import os


class GameManager:
    _instance = None

    def __new__(cls, *args, **kwargs):  # 싱글톤 패턴
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.player = Player()
        self.battle_system = BattleSystem()
        self.main_loop()

    def main_loop(self):
        while True:
            self.print_menu()
            choice = self.get_input()
            if choice == "battle":
                self.battle_system.start_battle(self.player, self.generate_monster())  # 퍼사드 패턴 (단순한 인터페이스)
            elif choice == "check":
                self.player.show_state()
            elif choice == "save":
                try:
                    with open("savegame.dat", "wb") as f:
                        pickle.dump(self.player, f)
                        print("게임 진행이 저장되었습니다.\n")
                except:
                    print("게임 진행을 저장할 수 없습니다.\n")
            elif choice == "open":
                if os.path.exists('savegame.dat'):
                    try:
                        with open("savegame.dat", "rb") as f:
                            self.player = pickle.load(f)
                            print("게임 진행을 불러왔습니다.\n")
                    except:
                        print("게임 진행을 불러올 수 없습니다.\n")
                else:
                    print("저장된 게임이 없습니다.\n")
            elif choice == "exit":
                print("게임을 종료합니다.\n")
                break

    @staticmethod
    def generate_monster():
        rdn = random.random()
        if rdn < 0.5:
            return MonsterFactory.get_monster("slime")
        elif rdn < 0.9:
            return MonsterFactory.get_monster("goblin")
        else:
            return MonsterFactory.get_monster("dragon")

    @staticmethod
    def print_menu():
        print("무엇을 하시겠습니까?\n"
              "1. 모험을 떠난다\n"
              "2. 상태를 확인한다\n"
              "3. 게임 저장\n"
              "4. 게임 불러오기\n"
              "5. 게임 종료\n")

    @staticmethod
    def get_input():
        while True:
            choice = input("선택: ")
            choice = choice.strip()
            if choice.isdigit() and 1 <= int(choice.isdigit()) <= 5:
                if int(choice) == 1:
                    valid_choice = "battle"
                    break
                elif int(choice) == 2:
                    valid_choice = "check"
                    break
                elif int(choice) == 3:
                    valid_choice = "save"
                    break
                elif int(choice) == 4:
                    valid_choice = "open"
                    break
                elif int(choice) == 5:
                    valid_choice = "exit"
                    break
            print("잘못된 입력입니다. 다시 선택해주세요.")

        return valid_choice


class BattleSystem:
    @staticmethod  # 전투 종료 조건 처리용 데코레이터
    def check_winner_decorator(func):
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            if args[0].hp == 0:
                return "monster"
            elif args[1].hp == 0:
                return "player"
            else:
                return None

        return wrapper

    def start_battle(self, player, monster):
        print(f"\n대결 상대 : {monster.name}")
        turn = 1
        while True:
            print(f"\n-- 턴 {turn} --")
            if turn % 2 == 1:
                winner = self.player_turn(player, monster)
            else:
                winner = self.monster_turn(player, monster)

            if winner is not None:
                self.end_battle(player, monster, winner)
                break
            turn += 1

    @staticmethod
    def end_battle(player, monster, winner):
        if winner == "player":
            print(f"\n당신이 승리했습니다.\n"
                  f"획득 경험치: +{monster.drop_exp}\n"
                  f"획득 아이템: {monster.drop_item.name if random.random() >= monster.drop_probability else '없음'}\n")
            player.change_exp(monster.drop_exp)
            player.add_item(monster.drop_item)

        elif winner == "monster":
            print(f"\n당신이 패배했습니다.\n"
                  f"감소 경험치: -{monster.minus_exp}\n")
            player.change_exp(-monster.minus_exp)

        player.set_info()

    @check_winner_decorator
    def player_turn(self, player, monster):
        while True:
            print(f"당신의 턴입니다.\n"
                  f"1. 공격\n"
                  f"2. 아이템 사용")
            choice = input("선택: ")
            if choice.isdigit() and 1 <= int(choice.isdigit()) <= 2:
                if int(choice) == 1:
                    valid_choice = "attack"
                    break
                elif int(choice) == 2:
                    valid_choice = "item"
                    break
            print("잘못된 입력입니다. 다시 선택해주세요.")

        if valid_choice == "attack":
            player.use_skill(monster)
        elif valid_choice == "item":
            while True:
                print("사용할 아이템을 선택하세요:")
                player.show_item()
                item_choice = input("선택: ")
                if item_choice.isdigit() and 1 <= int(item_choice.isdigit()) <= player.num_item:
                    player.use_item(int(item_choice)-1)
                    break
                print("잘못된 입력입니다. 다시 선택해주세요.")

    @check_winner_decorator
    def monster_turn(self, player, monster):
        if monster.hp/monster.max_hp < 0.1:  # 체력이 10% 미만으로 떨어지면 도망
            print(f"{monster.name} 이(가) 도망쳤습니다.")
            monster.change_hp(-monster.hp)
        else:
            monster.use_skill(player)


class Fighter:
    def __init__(self, name, max_hp, attack_power, defense_power):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack_power = attack_power
        self.defense_power = defense_power

    def change_hp(self, amount):
        self.hp += amount
        if self.hp < 0:
            self.hp = 0
        elif self.hp > self.max_hp:
            self.hp = self.max_hp

    def change_attack_power(self, amount):
        self.attack_power += amount
        if self.attack_power < 0:
            self.attack_power = 0

    def change_defense_power(self, amount):
        self.defense_power += amount
        if self.defense_power < 0:
            self.defense_power = 0

    def use_skill(self, target):
        pass


class Player(Fighter):
    def __init__(self, level=1, max_hp=100, attack_power=15, defense_power=15, max_exp=100, inventory=None):
        super().__init__(name="용사", max_hp=max_hp, attack_power=attack_power, defense_power=defense_power)
        self.level = level
        self.exp = 0
        self.max_exp = max_exp
        self.inventory = inventory
        if inventory is None:
            self.inventory = []
            self.inventory.append(ItemFactory.get_item("health_potion"))
            self.inventory.append(ItemFactory.get_item("health_potion"))
            self.inventory.append(ItemFactory.get_item("ring_of_strength"))  # 기본 아이템 가지고 시작
        self.num_item = len(self.inventory)

    def show_state(self):
        print(f"\n용사의 상태\n"
              f"레벨: {self.level}\n"
              f"HP: {self.hp}/{self.max_hp}\n"
              f"공격력: {self.attack_power}\n"
              f"방어력: {self.defense_power}\n"
              f"경험치: {self.exp}/{self.max_exp}\n"
              f"인벤토리: {self.inventory}\n")

    def show_item(self):
        for i in range(len(self.inventory)):
            print(f"{i+1}. {self.inventory[i].name}")

    def use_item(self, idx):
        item = self.inventory.pop(idx)
        self.num_item -= 1
        item.apply(self)

    def add_item(self, item):
        self.inventory.append(item)
        self.num_item += 1

    def change_exp(self, amount):
        level_exp = {2: 100, 3: 200, 4: 300, 5: 400}
        self.exp += amount
        if self.exp < 0:
            self.exp = 0
        for level in level_exp:
            if self.level < level and level_exp[level] <= self.exp:
                if self.level <= 5:
                    self.exp -= level_exp[level]
                    self.level += 1
                    self.max_exp = level_exp[level]
                    print(f"레벨 {level}로 상승했습니다!\n")
                else:
                    print(f"이미 최대 레벨에 도달했습니다.\n")
        self.set_info()

    def set_info(self):
        level_info = {1: (100, 15, 15, 100), 2: (200, 20, 20, 200),
                      3: (300, 40, 20, 300), 4: (400, 40, 40, 400), 5: (500, 50, 50, 'MAX')}
        change_info = level_info[self.level]
        self.hp = change_info[0]
        self.max_hp = change_info[0]
        self.attack_power = change_info[1]
        self.defense_power = change_info[2]
        self.max_exp = change_info[3]

    def use_skill(self, target):  # 플레이어 스킬 : 일반 공격
        net_damage = self.attack_power - target.defense_power
        if net_damage < 0:
            net_damage = 0
        net_damage *= random.randint(70, 130)/100
        net_damage = int(net_damage)
        target.change_hp(-net_damage)
        print(f"{self.name}이(가) {target.name}에게 '일반 공격' 스킬을 사용했습니다.\n"
              f"{target.name}의 hp가 {net_damage}만큼 감소해 {target.hp} 이(가) 되었습니다.")


class Monster(Fighter):
    def __init__(self, name, max_hp, attack_power, defense_power, drop_exp, minus_exp, drop_item, drop_probability):
        super().__init__(name=name, max_hp=max_hp, attack_power=attack_power, defense_power=defense_power)
        self.drop_exp = drop_exp
        self.minus_exp = minus_exp
        self.drop_item = drop_item
        self.drop_probability = drop_probability


class Slime(Monster):
    def __init__(self):
        item = ItemFactory.get_item("health_potion")
        super().__init__(name="슬라임", max_hp=30, attack_power=20, defense_power=10,
                         drop_exp=30, minus_exp=5, drop_item=item, drop_probability=0.1)

    def use_skill(self, target):  # 슬라임 스킬 : 상대방의 방어력을 감소시킨 뒤 공격
        target.change_defense_power(-3)
        net_damage = self.attack_power - target.defense_power
        if net_damage < 0:
            net_damage = 0
        net_damage *= (random.randint(80, 120) / 100)
        net_damage = int(net_damage)
        target.change_hp(-net_damage)
        print(f"{self.name}이(가) {target.name}에게 '슬라임 펀치' 스킬을 사용했습니다.\n"
              f"{target.name}의 hp가 {net_damage}만큼 감소해 {target.hp} 이(가) 되었습니다.\n"
              f"{target.name}의 방어력이 3만큼 감소해 {target.defense_power} 이(가) 되었습니다.")


class Goblin(Monster):
    def __init__(self):
        if random.randint(0, 1) == 0:
            item = ItemFactory.get_item("health_potion")
        else:
            item = ItemFactory.get_item("ring_of_strength")
        super().__init__(name="고블린", max_hp=80, attack_power=30, defense_power=5,
                         drop_exp=40, minus_exp=10, drop_item=item, drop_probability=0.4)

    def use_skill(self, target):  # 고블린 스킬 : 플레이어에게 입힌 피해량의 절반만큼 체력 회복
        net_damage = self.attack_power - target.defense_power
        if net_damage < 0:
            net_damage = 0
        net_damage *= (random.randint(80, 120) / 100)
        net_damage = int(net_damage)
        target.change_hp(-net_damage)
        self.change_hp(int(net_damage*0.5))
        print(f"{self.name}이(가) {target.name}에게 '고블린 습격' 스킬을 사용했습니다.\n"
              f"{target.name}의 hp가 {net_damage}만큼 감소해 {target.hp} 이(가) 되었습니다.\n"
              f"{self.name}의 hp가 {int(net_damage*0.5)}만큼 증가해 {self.hp} 이(가) 되었습니다.")


class Dragon(Monster):
    def __init__(self):
        item = ItemFactory.get_item("shield_of_defense")
        super().__init__(name="드래곤", max_hp=500, attack_power=60, defense_power=60,
                         drop_exp=100, minus_exp=30, drop_item=item, drop_probability=0.8)

    def use_skill(self, target):  # 공격 후 본인 체력 일정량 회복
        net_damage = self.attack_power - target.defense_power
        if net_damage < 0:
            net_damage = 0
        net_damage *= (random.randint(95, 105) / 100)
        net_damage = int(net_damage)
        target.change_hp(-net_damage)
        self.change_hp(30)
        print(f"{self.name}이(가) {target.name}에게 '드래곤의 화염' 스킬을 사용했습니다.\n"
              f"{target.name}의 hp가 {net_damage}만큼 감소해 {target.hp} 이(가) 되었습니다.\n"
              f"{self.name}의 hp가 30만큼 증가해 {self.hp} 이(가) 되었습니다.")


class MonsterFactory:  # 팩토리 패턴
    @staticmethod
    def get_monster(monster_type):
        if monster_type == "slime":
            return Slime()
        elif monster_type == "goblin":
            return Goblin()
        elif monster_type == "dragon":
            return Dragon()


class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f'{self.name}'

    def apply(self, target):
        pass


class HealthPotion(Item):
    def __init__(self):
        super().__init__(name="체력 물약", amount=60)

    def apply(self, target):
        target.change_hp(self.amount)
        print(f"{target.name}의 체력이 {self.amount}만큼 회복되어 {target.hp} 이(가) 되었습니다.")


class RingOfStrength(Item):
    def __init__(self):
        super().__init__(name="힘의 반지", amount=40)

    def apply(self, target):
        target.change_attack_power(self.amount)
        print(f"{target.name}의 공격력이 {self.amount}만큼 증가해 {target.attack_power} 이(가) 되었습니다.")


class ShieldOfDefense(Item):
    def __init__(self):
        super().__init__(name="방어의 방패", amount=50)

    def apply(self, target):
        target.change_defense_power(self.amount)
        print(f"{target.name}의 방어력이 {self.amount}만큼 증가해 {target.defense_power} 이(가) 되었습니다.")


class ItemFactory:  # 팩토리 패턴
    @staticmethod
    def get_item(item_type):
        if item_type == "health_potion":
            return HealthPotion()
        elif item_type == "ring_of_strength":
            return RingOfStrength()
        elif item_type == "shield_of_defense":
            return ShieldOfDefense()


start_game = GameManager()
