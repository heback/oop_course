import random
import threading
import time
import pickle
import os

# 싱글톤 패턴을 적용한 GameManager 클래스
class GameManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(GameManager, cls).__new__(cls)
                    cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.player = Player()
        self.running = True

    def save_game(self):
        with open('savegame.dat', 'wb') as f:
            pickle.dump(self.player, f)
        print("게임 진행이 저장되었습니다.")

    def load_game(self):
        if os.path.exists('savegame.dat'):
            with open('savegame.dat', 'rb') as f:
                self.player = pickle.load(f)
            print("게임 진행을 불러왔습니다.")
        else:
            print("저장된 게임이 없습니다.")

    def game_loop(self):
        print("게임에 오신 것을 환영합니다!")
        while self.running:
            print("\n무엇을 하시겠습니까?")
            print("1. 모험을 떠난다")
            print("2. 상태를 확인한다")
            print("3. 게임 저장")
            print("4. 게임 불러오기")
            print("5. 게임 종료")
            choice = input("선택: ")
            if choice == '1':
                self.start_adventure()
            elif choice == '2':
                self.player.show_status()
            elif choice == '3':
                self.save_game()
            elif choice == '4':
                self.load_game()
            elif choice == '5':
                print("게임을 종료합니다.")
                self.running = False
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")

    def start_adventure(self):
        monster = MonsterFactory.create_monster()
        battle_system = BattleSystem()
        battle_system.start_battle(self.player, monster)
        if self.player.hp <= 0:
            print("당신은 패배했습니다. 게임 오버.")
            self.running = False
        else:
            exp_gain = monster.level * 50
            print(f"{exp_gain}의 경험치를 획득했습니다!")
            self.player.gain_exp(exp_gain)
            # 몬스터를 물리친 후 아이템 획득 처리 추가
            dropped_item = monster.drop_item()
            if dropped_item:
                print(f"{monster.name}이(가) {dropped_item.name}을(를) 떨어뜨렸습니다!")
                self.player.add_item(dropped_item)

# 팩토리 패턴을 적용한 몬스터 생성
class MonsterFactory:
    @staticmethod
    def create_monster():
        monsters = [Slime, Goblin, Dragon]
        monster_class = random.choice(monsters)
        return monster_class()

# 팩토리 패턴을 적용한 아이템 생성
class ItemFactory:
    @staticmethod
    def create_item(item_name):
        items = {
            "Health Potion": HealthPotion,
            "Ring of Strength": RingOfStrength,
            "Shield of Defense": ShieldOfDefense
        }
        item_class = items.get(item_name)
        if item_class:
            return item_class()
        else:
            raise ValueError(f"존재하지 않는 아이템입니다: {item_name}")

# 몬스터 클래스들
class Monster:
    def __init__(self, name, level, hp, attack, defense):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def drop_item(self):
        # 몬스터 종류에 따라 드롭 아이템 결정
        pass  # 하위 클래스에서 구현

class Slime(Monster):
    def __init__(self):
        super().__init__("슬라임", 1, 50, 5, 1)

    def drop_item(self):
        if random.random() < 0.3:  # 30% 확률로 체력 물약 드롭
            return ItemFactory.create_item("Health Potion")
        return None

class Goblin(Monster):
    def __init__(self):
        super().__init__("고블린", 2, 80, 10, 3)

    def drop_item(self):
        drop_chance = random.random()
        if drop_chance < 0.5:
            return ItemFactory.create_item("Health Potion")
        elif drop_chance < 0.7:
            return ItemFactory.create_item("Ring of Strength")
        return None

class Dragon(Monster):
    def __init__(self):
        super().__init__("드래곤", 3, 100, 15, 5)

    def drop_item(self):
        if random.random() < 0.8:  # 80% 확률로 아이템 드롭
            return ItemFactory.create_item("Shield of Defense")
        return None

# 플레이어 클래스
class Player:
    def __init__(self):
        self.name = "용사"
        self.level = 1
        self.max_hp = 100
        self.hp = 100
        self.attack = 15
        self.defense = 5
        self.exp = 0
        self.inventory = []
        # 초기 아이템 추가
        self.add_item(ItemFactory.create_item("Health Potion"))
        self.add_item(ItemFactory.create_item("Health Potion"))
        self.add_item(ItemFactory.create_item("Ring of Strength"))

    def is_alive(self):
        return self.hp > 0

    def gain_exp(self, amount):
        self.exp += amount
        while self.exp >= self.level * 100:
            self.exp -= self.level * 100
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 2
        print(f"레벨이 올랐습니다! 현재 레벨: {self.level}")

    def show_status(self):
        print(f"\n{self.name}의 상태")
        print(f"레벨: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"공격력: {self.attack}")
        print(f"방어력: {self.defense}")
        print(f"경험치: {self.exp}/{self.level * 100}")
        print("인벤토리:", [item.name for item in self.inventory])

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name}을(를) 인벤토리에 추가했습니다.")

# 아이템 클래스들
class Item:
    def __init__(self, name):
        self.name = name

    def use(self, target):
        pass

class HealthPotion(Item):
    def __init__(self):
        super().__init__("체력 물약")

    def use(self, target):
        heal_amount = 50
        target.hp = min(target.max_hp, target.hp + heal_amount)
        print(f"{target.name}의 체력이 {heal_amount}만큼 회복되었습니다.")

class RingOfStrength(Item):
    def __init__(self):
        super().__init__("힘의 반지")

    def use(self, target):
        target.attack += 5
        print(f"{target.name}의 공격력이 5만큼 증가했습니다.")

class ShieldOfDefense(Item):
    def __init__(self):
        super().__init__("방어의 방패")

    def use(self, target):
        target.defense += 5
        print(f"{target.name}의 방어력이 5만큼 증가했습니다.")

# 퍼사드 패턴을 적용한 전투 시스템
class BattleSystem:
    def __init__(self):
        self.skill_system = SkillSystem()
        self.item_system = ItemSystem()
        # self.status_effect_system = StatusEffectSystem()

    def start_battle(self, player, monster):
        print(f"\n{monster.name}이(가) 나타났다!")
        turn = 0
        while player.is_alive() and monster.is_alive():
            print(f"\n-- 턴 {turn + 1} --")
            # 플레이어의 턴
            print("\n당신의 턴입니다.")
            print("1. 공격")
            print("2. 아이템 사용")
            action = input("선택: ")
            if action == '1':
                damage = self.skill_system.calculate_damage(player, monster)
                monster.hp -= damage
                print(f"{monster.name}에게 {damage}의 피해를 입혔습니다.")
            elif action == '2':
                self.item_system.use_item(player)
            else:
                print("잘못된 입력입니다.")
                continue
            if not monster.is_alive():
                print(f"{monster.name}을(를) 물리쳤습니다!")
                break

            # 몬스터의 턴
            print(f"\n{monster.name}의 턴입니다.")
            monster_action = self.decide_monster_action(monster, player)
            if monster_action == 'attack':
                damage = self.skill_system.calculate_damage(monster, player)
                player.hp -= damage
                print(f"{monster.name}이(가) 당신에게 {damage}의 피해를 입혔습니다.")
            elif monster_action == 'skill':
                damage = self.skill_system.use_skill(monster, player)
                player.hp -= damage
            elif monster_action == 'flee':
                print(f"{monster.name}이(가) 도망쳤습니다!")
                break

            if not player.is_alive():
                print("당신은 쓰러졌습니다...")
                break

            turn += 1

    def decide_monster_action(self, monster, player):
        if monster.hp < monster.max_hp * 0.3:
            action = random.choice(['attack', 'skill', 'flee'])
        else:
            action = random.choice(['attack', 'skill'])
        return action

# 서브시스템: 스킬 시스템
class SkillSystem:
    def calculate_damage(self, attacker, defender):
        damage = max(0, attacker.attack - defender.defense)
        return damage

    def use_skill(self, attacker, defender):
        if isinstance(attacker, Player):
            print("사용할 스킬이 없습니다.")
            return 0
        else:
            print(f"{attacker.name}이(가) 화염 브레스를 사용했습니다!")
            damage = attacker.attack * 2 - defender.defense
            damage = max(0, damage)
            return damage

# 서브시스템: 아이템 시스템
class ItemSystem:
    def use_item(self, player):
        if not player.inventory:
            print("사용할 아이템이 없습니다.")
            return
        print("사용할 아이템을 선택하세요:")
        for idx, item in enumerate(player.inventory):
            print(f"{idx + 1}. {item.name}")
        choice = input("선택: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(player.inventory):
                item = player.inventory.pop(index)
                item.use(player)
            else:
                print("잘못된 선택입니다.")
        except ValueError:
            print("잘못된 입력입니다.")


# 게임 실행
if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.game_loop()
