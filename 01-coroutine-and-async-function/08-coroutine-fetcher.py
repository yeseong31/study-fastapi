# https://docs.aiohttp.org/en/stable/

# requests 모듈은 '동기' 실행만을 지원함
# 비동기 실행을 위해서는 aiohttp 모듈이 필요함
# pip install aiohttp

import asyncio
import time

import aiohttp


async def fetcher(session, url):
    """해당되는 url의 HTML 데이터 전부를 얻어옴 - 비동기"""
    async with session.get(url=url) as response:
        return await response.text()


async def main():
    urls = ['https://www.naver.com/', 'https://google.com/', 'https://instagram.com/'] * 30
    
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'총 실행 시간: {end - start}')  # 비동기 코드 실행 시 3.42초 소요
