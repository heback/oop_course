from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof"


# 추상 클래스를 직접 인스턴스화할 수 없음
# animal = Animal()  # 오류 발생

# 서브클래스에서 추상 메서드 구현
dog = Dog()
print(dog.sound())

