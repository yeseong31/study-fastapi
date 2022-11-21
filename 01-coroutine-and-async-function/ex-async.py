import time
import asyncio


async def find_users_async(n):
    res = 0
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번째 사용자 데이터 조회 중...')
        await asyncio.sleep(1)
        res += 1
    print(f'> 총 {n}명의 사용자 비동기 조회 완료!')
    return res


async def process_async():
    start = time.time()
    result = await asyncio.gather(
            find_users_async(3),
            find_users_async(2),
            find_users_async(1))
    end = time.time()
    print(result)
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')


if __name__ == '__main__':
    asyncio.run(process_async())
