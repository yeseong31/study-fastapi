# https://requests.readthedocs.io/en/latest/
# pip install requests
import time

import requests


def fetcher(session, url):
    """해당되는 url의 HTML 데이터 전부를 얻어옴 - 동기"""
    with session.get(url=url) as response:
        return response.text


def main():
    urls = ['https://www.naver.com/', 'https://google.com/', 'https://instagram.com/'] * 30
    
    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)
    # session = requests.Session()
    # session.get(url=url)
    # session.close()


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'총 실행 시간: {end - start}')  # 동기 코드 실행 시 26초 소요
