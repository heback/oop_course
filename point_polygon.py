from math import hypot
from typing import Tuple, List, Optional, Iterable


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance(self, other: 'Point') -> float:
        return hypot(self.x - other.x, self.y - other.y)


class Polygon:
    def __init__(self) -> None:
        self.points: List[Point] = []

    def add_point(self, point: Point) -> None:
        self.points.append(point)

    def perimeter(self) -> float:
        pairs = zip(self.points, self.points[1:] + self.points[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)

'''
pairs = zip(self.points, self.points[1:] + self.points[:1])는 다각형(Polygon)의 둘레를 계산하기 위해 점(point)들을 짝지어주는 코드입니다. 
이 코드는 다각형의 각 변을 나타내는 점들의 쌍을 생성합니다.

코드의 의미:
self.points: 다각형의 각 꼭짓점을 저장하는 리스트입니다.
self.points[1:]: 첫 번째 점을 제외한 나머지 점들로 이루어진 리스트입니다.
self.points[:1]: 첫 번째 점만 포함된 리스트입니다.
self.points[1:] + self.points[:1]: 첫 번째 점을 제외한 나머지 점들 뒤에 첫 번째 점을 추가한 리스트입니다. 
이 리스트는 다각형의 마지막 점과 첫 번째 점을 연결하는 데 사용됩니다.
예시:
예를 들어, 점들이 self.points = [A, B, C, D]로 구성되어 있다고 가정해 보겠습니다.
self.points[1:]는 [B, C, D]이고, self.points[:1]는 [A]입니다.
따라서 self.points[1:] + self.points[:1]는 [B, C, D, A]가 됩니다.
zip 함수:
zip(self.points, self.points[1:] + self.points[:1])는 [A, B, C, D]와 [B, C, D, A]를 짝지어 다음과 같은 쌍을 생성합니다:
(A, B): A에서 B로 가는 변
(B, C): B에서 C로 가는 변
(C, D): C에서 D로 가는 변
(D, A): D에서 A로 가는 변 (마지막 점과 첫 번째 점을 연결)
이렇게 생성된 쌍들을 사용하여 다각형의 둘레(perimeter)를 계산할 수 있습니다. p1.distance(p2)는 이 점 쌍들 사이의 거리를 계산하는 함수로 가정됩니다.
'''