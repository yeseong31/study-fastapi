import os
import threading
import time

import requests


def fetcher(session, url):
    """해당되는 url의 HTML 데이터 전부를 얻어옴 - 동기"""
    # 어떤 프로세스에서 실행되는지 확인 --> 19904 process | 12772 url: https://google.com/
    print(f'{os.getpid()} process | {threading.get_ident()} url: {url}')
    with session.get(url=url) as response:
        return response.text


def main():
    urls = ['https://www.apple.com/', 'https://google.com/'] * 50
    
    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'총 실행 시간: {end - start}')  # 총 실행 시간: 41.64737272262573
