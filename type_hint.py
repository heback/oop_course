# 어노테이션 방식
num = 1  # type: int
num = "1"
print(num, type(num))

# 타입 힌트 방식
num: str = 1
num = "1"
print(num, type(num))

# 힌팅은 언어 레벨에서
# 실질적으로 어떠한 제약 사항도 강요되지 않는다.
# 다시 말해, 변수나 함수에 추가한 타입 어노테이션이
# 부정확한다고 해서 경고나 오류가 발생하는 것은 아님.

def repeat(message, times = 2):
    # type: (str, int) -> list
    return [message] * times

print(repeat('111', 5))

from typing import *
num: List[int] = [1,2,3,4,5]
print(num)

dic: Dict[int, str] = {
    0: 'aaa',
    1: 'bbb'
}