from bs4 import BeautifulSoup
import aiohttp
import asyncio


BASE_URL = 'https://bjpublic.tistory.com'
CATEGORY = '/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C'


async def fetch(session: aiohttp.ClientSession, url: str):
    """해당하는 URL에 대해 HTML 데이터를 가져옴"""
    async with session.get(url=url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        for anchor in soup.select('.section_area > ul > li > a'):
            link = f'{BASE_URL}{anchor["href"]}'
            title = anchor.find('p', class_='txt_thumb').text
            print(link, title)


async def main():
    urls = [f'{BASE_URL}{CATEGORY}?page={i}' for i in range(1, 23)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == '__main__':
    asyncio.run(main())
