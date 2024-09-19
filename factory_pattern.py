class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("원을 그립니다.")

class Square(Shape):
    def draw(self):
        print("사각형을 그립니다.")

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            return None

# 사용 예시
if __name__ == "__main__":
    factory = ShapeFactory()
    shape = factory.get_shape("circle")
    shape.draw()  # 출력: 원을 그립니다.

