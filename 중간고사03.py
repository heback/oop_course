# Product 클래스
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 데코레이터 패턴: TaxDecorator
class TaxDecorator:
    def __init__(self, product):
        self.product = product

    def calculate_price(self):
        # 세금 10% 적용
        return self.product.price * 1.1

# 믹스인 패턴: DownloadableMixin
class DownloadableMixin:
    def download(self):
        print(f"상품 {self.name}을(를) 다운로드합니다.")

# 컴포지션: Warranty 클래스
class Warranty:
    def __init__(self, warranty_period):
        self.warranty_period = warranty_period

    def is_valid_warranty(self):
        return self.warranty_period > 0

    def use_warranty(self):
        if self.warranty_period > 0:
            self.warranty_period -= 1
            print(f"남은 보증 기간: {self.warranty_period}개월")
        else:
            print("보증 기간이 만료되었습니다.")

# Electronics 클래스 (컴포지션을 이용한 보증 관리)
class Electronics(Product):
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = Warranty(warranty_period)

    def repair(self):
        if self.warranty.is_valid_warranty():
            self.warranty.use_warranty()
            print(f"{self.name}의 수리를 진행합니다.")
        else:
            print(f"{self.name}의 보증 기간이 만료되었습니다.")

# Clothing 클래스
class Clothing(Product):
    def __init__(self, name, price, size, color):
        super().__init__(name, price)
        self.size = size
        self.color = color

    def wash_instructions(self):
        print(f"{self.name}의 세탁 방법: 찬물로 세탁하세요.")

# DigitalProduct 클래스 (믹스인 및 데코레이터 적용)
class DigitalProduct(Product, DownloadableMixin):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def calculate_price(self):
        tax_decorator = TaxDecorator(self)
        return tax_decorator.calculate_price()

# 실행 예시
# 의류 상품
tshirt = Clothing("티셔츠", 20000, "M", "블루")
tshirt.wash_instructions()

# 전자제품 상품 (보증 관리)
laptop = Electronics("노트북", 1500000, "BrandA", 2)
print(f"노트북 가격: {laptop.price} 원")
laptop.repair()  # 보증 사용
laptop.repair()  # 보증 사용
laptop.repair()  # 보증 만료

# 디지털 상품 (믹스인 및 데코레이터 패턴 적용)
ebook = DigitalProduct("Python Programming eBook", 10000, "5MB")
print(f"eBook 세금 포함 가격: {ebook.calculate_price()} 원")
ebook.download()
