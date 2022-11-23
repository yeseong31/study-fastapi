# https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C
import asyncio
import os
import re

import aiofiles
import aiohttp

import config

BASE_URL = 'https://openapi.naver.com/v1/search/image'
BASE_IMAGE_PATH = './images'

amount = 20
headers = {
    'X-Naver-Client-Id': config.NAVER_CLIENT_ID,
    'X-Naver-Client-Secret': config.NAVER_CLIENT_SECRET
}


async def img_downloader(session: aiohttp.ClientSession, img: str):
    img_name = img.split('/')[-1].split('?')[0]
    img_name = re.sub(r'[?*<":>/]', '', img_name)
    try:
        os.mkdir(BASE_IMAGE_PATH)
    except FileExistsError:
        pass
    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f'{BASE_IMAGE_PATH}/{img_name}', mode='wb') as file:
                await file.write(await response.read())


async def fetch(session: aiohttp.ClientSession, url: str):
    """해당하는 URL에 대해 HTML 데이터를 가져옴"""
    async with session.get(url=url, headers=headers) as response:
        result = await response.json()
        items = result['items']
        images = [item['link'] for item in items]
        await asyncio.gather(*[img_downloader(session, img) for img in images])


async def main():
    keyword = 'cat'
    urls = [f'{BASE_URL}?query={keyword}&display={amount}&start={i * amount + 1}' for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == '__main__':
    asyncio.run(main())
