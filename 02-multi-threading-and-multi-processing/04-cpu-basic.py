import os
import threading
import time
import sys

sys.set_int_max_str_digits(10**6)

nums = [30] * 100
# nums = [50, 63, 32]


def cpu_bound_func(num):
    print(f'{os.getpid()} process | {threading.get_ident()} thread')
    total = 1
    for i in range(1, num):
        for j in range(1, num):
            for k in range(1, num):
                total *= i * j * k
    return total


def main():
    results = [cpu_bound_func(num) for num in nums]
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 24.497793436050415
