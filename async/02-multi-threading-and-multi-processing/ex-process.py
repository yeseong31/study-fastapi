import os
import time
from multiprocessing import Process


def func():
    print('연속적으로 실행하고자 하는 어떠한 작업')
    time.sleep(0.1)


def doubler(x):
    result = x + 10
    func()
    print(f'number: {x}, result: {result}, pid: {os.getpid()}')


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    procs = []
    
    for i, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number, ))
        procs.append(proc)
        proc.start()  # doubler 함수 호출
