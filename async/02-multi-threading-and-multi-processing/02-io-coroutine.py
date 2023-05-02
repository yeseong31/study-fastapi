import asyncio
import os
import threading
import time

import aiohttp


async def fetcher(session: aiohttp.ClientSession, url: str):
    """해당되는 url의 HTML 데이터 전부를 얻어옴 - 비동기"""
    # 어떤 프로세스에서 실행되는지 확인 --> 19904 process | 12772 url: https://google.com/
    print(f'{os.getpid()} process | {threading.get_ident()} url: {url}')
    async with session.get(url=url) as response:
        return await response.text()


async def main():
    urls = ['https://www.apple.com/', 'https://google.com/'] * 50
    
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'총 실행 시간: {end - start}')  # 총 실행 시간: 2.0148227214813232
