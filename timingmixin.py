import time


# 시간 측정 믹스인
class TimingMixin:
    def time_it(self, func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: "
              f"{end_time - start_time:.4f} seconds")
        return result


# 소수 판별 함수
class PrimeNumberOperations:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def count_primes(self, up_to):
        count = 0
        for number in range(2, up_to + 1):
            if self.is_prime(number):
                count += 1
        return count


# PrimeNumberOperations에 시간 측정 기능 추가
class TimedPrimeNumberOperations(
    PrimeNumberOperations,
    TimingMixin
):
    def timed_count_primes(self, up_to):
        return self.time_it(self.count_primes, up_to)


# 사용 예제
prime_op = TimedPrimeNumberOperations()

# 1부터 1,000,000까지의 소수를 찾는 시간을 측정
result = prime_op.timed_count_primes(1_000_000)
print(f"Number of primes up to 1,000,000: {result}")


