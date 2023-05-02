import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

sys.set_int_max_str_digits(10**6)

nums = [30] * 100
# nums = [50, 63, 32]


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 26.856146335601807

# cpu-basic의 경우보다 시간이 더 걸린 이유는
# 스레드 생성 시간과 반환 시간에 대한 비용이 더 들었기 때문
