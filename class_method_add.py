import math


class Point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


import mypy

def greeting(name: str) -> str:
    return 'Hello ' + name

greeting(3)         # Argument 1 to "greeting" has incompatible type "int"; expected "str"
greeting(b'Alice')  # Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
greeting("World!")  # No error

def bad_greeting(name: str) -> str:
    return 'Hello ' * name  # Unsupported operand types for * ("str" and "str")