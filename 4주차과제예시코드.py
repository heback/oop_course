from datetime import date

# 데코레이터 정의
def requires_login(func):
    def wrapper(self, *args, **kwargs):
        if not self.logged_in:
            raise Exception("사용자가 로그인되어 있지 않습니다.")
        return func(self, *args, **kwargs)
    return wrapper

def log_activity(func):
    def wrapper(self, *args, **kwargs):
        self.log(f"{func.__name__} 메서드 시작")
        result = func(self, *args, **kwargs)
        self.log(f"{func.__name__} 메서드 종료")
        return result
    return wrapper

# LoggerMixin 정의
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

# 상품 클래스 계층 구조
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # 내부적으로 사용되는 변수

    @property
    def price(self):
        # 세금 포함 가격 계산 (10% 세금)
        return self._price * 1.1

    @price.setter
    def price(self, value):
        self._price = value

class Clothing(Product):
    def __init__(self, name, price, size, color):
        super().__init__(name, price)
        self.size = size
        self.color = color

    def wash_instructions(self):
        print(f"상품 {self.name}의 세탁 방법: 찬물로 세탁하세요.")

class Electronics(Product):
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period  # 보증 기간 (개월 수)

    # check_warranty 데코레이터 정의
    def check_warranty(func):
        def wrapper(self, *args, **kwargs):
            if self.warranty_period <= 0:
                print(f"상품 {self.name}의 보증 기간이 만료되었습니다.")
            else:
                self.warranty_period -= 1  # 보증 기간 1개월 감소
                return func(self, *args, **kwargs)
        return wrapper

    @check_warranty
    def repair(self):
        print(f"상품 {self.name}의 수리를 진행합니다.")

class Food(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date  # datetime.date 객체

    @property
    def is_valid(self):
        if date.today() <= self.expiration_date:
            print(f"상품 {self.name}은(는) 유효합니다.")
            return True
        else:
            print(f"상품 {self.name}은(는) 유효 기간이 지났습니다.")
            return False

class DownloadableMixin:
    def download(self):
        print(f"상품 {self.name}을(를) 다운로드합니다.")

class DigitalProduct(Product, DownloadableMixin):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def download(self):
        print(f"상품 {self.name}({self.file_size})을(를) 다운로드합니다.")

# 사용자 클래스 계층 구조
class User(LoggerMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.logged_in = False

    def login(self):
        self.logged_in = True
        print(f"{self.username}님이 로그인했습니다.")

    def logout(self):
        self.logged_in = False
        print(f"{self.username}님이 로그아웃했습니다.")

class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.cart = []

    @requires_login
    @log_activity
    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product.name}이(가) 장바구니에 추가되었습니다.")

    @requires_login
    @log_activity
    def checkout(self):
        print("결제가 진행됩니다.")
        self.cart.clear()

class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.products = []

    @requires_login
    @log_activity
    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name}이(가) 상품 목록에 추가되었습니다.")

    @requires_login
    @log_activity
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name}이(가) 상품 목록에서 제거되었습니다.")
        else:
            print(f"{product.name}이(가) 상품 목록에 없습니다.")

class Admin(User):
    @requires_login
    @log_activity
    def ban_user(self, user):
        print(f"{user.username}님이 차단되었습니다.")

    @requires_login
    @log_activity
    def modify_product(self, product, **kwargs):
        for key, value in kwargs.items():
            setattr(product, key, value)
        print(f"{product.name}의 정보가 수정되었습니다.")

# 주문 처리 시스템
class DiscountStrategy:
    def calculate_discounted_price(self, price):
        return price  # 기본적으로 할인 없음

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate_discounted_price(self, price):
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def calculate_discounted_price(self, price):
        return max(0, price - self.amount)

class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total_price = 0

    def calculate_total(self):
        self.total_price = sum(item.price for item in self.items)
        print(f"총 가격: {int(self.total_price)}원")

    def apply_discount(self, discount_strategy):
        self.total_price = discount_strategy.calculate_discounted_price(self.total_price)
        print(f"할인 적용 가격: {int(self.total_price)}원")

class OrderProcessor:
    def __init__(self, order, discount_strategy):
        self.order = order
        self.discount_strategy = discount_strategy

    def process_order(self):
        self.order.calculate_total()
        self.order.apply_discount(self.discount_strategy)
        print("주문이 완료되었습니다.")

# 실행 예제
if __name__ == "__main__":
    # 상품 생성
    tshirt = Clothing("티셔츠", 20000, "M", "블루")
    laptop = Electronics("노트북", 1500000, "BrandA", 2)
    apple = Food("사과", 3000, expiration_date=date(2024, 12, 31))
    ebook = DigitalProduct("파이썬 프로그래밍 eBook", 10000, "5MB")

    # 상품 메서드 테스트
    tshirt.wash_instructions()
    laptop.repair()
    laptop.repair()  # 보증 기간 감소 확인
    laptop.repair()  # 보증 기간 만료 시도
    is_apple_valid = apple.is_valid  # 유효 기간 확인
    ebook.download()  # 다운로드 기능 테스트

    print("\n")

    # 사용자 생성 및 동작 테스트
    customer = Customer("customer1", "customer1@example.com")
    customer.login()
    customer.add_to_cart(tshirt)
    customer.add_to_cart(ebook)
    customer.checkout()
    customer.logout()

    print("\n")

    seller = Seller("seller1", "seller1@example.com")
    seller.login()
    seller.add_product(tshirt)
    seller.add_product(laptop)
    seller.remove_product(apple)  # 목록에 없는 상품 제거 시도
    seller.remove_product(tshirt)
    seller.logout()

    print("\n")

    admin = Admin("admin1", "admin1@example.com")
    admin.login()
    admin.ban_user(customer)
    admin.modify_product(laptop, price=1400000)
    admin.logout()

    print("\n")

    # 주문 처리 테스트
    order = Order(customer, [tshirt, ebook])
    discount = PercentageDiscount(10)  # 10% 할인 적용
    processor = OrderProcessor(order, discount)
    processor.process_order()
