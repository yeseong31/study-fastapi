# https://docs.python.org/ko/3/library/asyncio-task.html#coroutines
import asyncio


async def hello_world():
    print('hello world')
    return 123


async def main():
    # 태스크: 코루틴을 동시에 예약하는 데 사용
    task = asyncio.create_task(hello_world())
    await task


if __name__ == '__main__':
    asyncio.run(hello_world())
    asyncio.run(main())
