# https://docs.python.org/3.7/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests


def fetcher(params):
    """해당되는 url의 HTML 데이터 전부를 얻어옴 - 비동기"""
    session, url = params
    print(f'{os.getpid()} process | {threading.get_ident()} url: {url}')
    with session.get(url=url) as response:
        return response.text


def main():
    urls = ['https://www.apple.com/', 'https://google.com/'] * 50
    
    executor = ThreadPoolExecutor(max_workers=10)  # 최대 스레드를 실행할 수
    
    with requests.Session() as session:
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))
        print(result)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'총 실행 시간: {end - start}')  # 총 실행 시간: 4.1906890869140625
