import os
import time
from multiprocessing import Pool


def f(x):
    print(f'값 {x}에 대한 작업 pid: {os.getpid()}')
    time.sleep(0.1)
    return x ** 2


if __name__ == '__main__':
    # 프로세스 객체의 개수 지정
    p = Pool(3)
    start = time.time()
    
    # --- Pool 객체를 사용하지 않고 일반적인 방법을 사용했을 때 ---
    # for i in range(10):
    #     print(f(i))
    # --- Pool 객체를 사용했을 때 ---
    print(p.map(f, range(10)))
    
    end = time.time()
    print(f'총 작업 시간: {end - start}')
    
    
# Pool 객체를 사용하지 않았을 때: 총 작업 시간: 1.0051686763763428
# Pool 객체를 사용했을 때: 총 작업 시간: 0.5025663375854492
