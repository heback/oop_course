# 서브시스템 클래스들
class AccountNumberCheck:
    def __init__(self):
        self.account_number = 123456789

    def account_active(self, acc_num):
        if acc_num == self.account_number:
            return True
        else:
            print("계좌 번호가 유효하지 않습니다.")
            return False

class SecurityCodeCheck:
    def __init__(self):
        self.security_code = 1234

    def code_correct(self, sec_code):
        if sec_code == self.security_code:
            return True
        else:
            print("보안 코드가 유효하지 않습니다.")
            return False

class FundsCheck:
    def __init__(self):
        self.cash_in_account = 1000.0

    def have_enough_money(self, cash_to_withdraw):
        if cash_to_withdraw > self.cash_in_account:
            print("잔액이 부족합니다.")
            return False
        else:
            self.decrease_cash_in_account(cash_to_withdraw)
            print(f"{cash_to_withdraw}원이 인출되었습니다.")
            return True

    def make_deposit(self, cash_to_deposit):
        self.increase_cash_in_account(cash_to_deposit)
        print(f"{cash_to_deposit}원이 입금되었습니다.")

    def decrease_cash_in_account(self, amount):
        self.cash_in_account -= amount

    def increase_cash_in_account(self, amount):
        self.cash_in_account += amount

# 퍼사드 클래스
class BankAccountFacade:
    def __init__(self, account_number, security_code):
        self.account_number = account_number
        self.security_code = security_code

        self.acc_checker = AccountNumberCheck()
        self.code_checker = SecurityCodeCheck()
        self.fund_checker = FundsCheck()

    def withdraw_money(self, cash_to_get):
        print("------ 인출 거래 시작 ------")
        if (self.acc_checker.account_active(self.account_number) and
            self.code_checker.code_correct(self.security_code) and
            self.fund_checker.have_enough_money(cash_to_get)):
            print("거래 완료: 인출 성공")
        else:
            print("거래 실패: 인출 불가")
        print("---------------------------\n")

    def deposit_money(self, cash_to_deposit):
        print("------ 입금 거래 시작 ------")
        if (self.acc_checker.account_active(self.account_number) and
            self.code_checker.code_correct(self.security_code)):
            self.fund_checker.make_deposit(cash_to_deposit)
            print("거래 완료: 입금 성공")
        else:
            print("거래 실패: 입금 불가")
        print("---------------------------\n")

# 클라이언트 코드
if __name__ == "__main__":
    # 올바른 계좌 정보로 퍼사드 객체 생성
    bank_account = BankAccountFacade(123456789, 1234)

    # 인출 시도
    bank_account.withdraw_money(500.0)

    # 입금 시도
    bank_account.deposit_money(200.0)

    # 잔액보다 많은 금액 인출 시도
    bank_account.withdraw_money(800.0)

