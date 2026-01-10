import asyncio

async def coroutine_1(delay=0.1):
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(0.3)  # Первая задержка
    print("Второе сообщение от корутины 1")
    await asyncio.sleep(0.3)  # Вторая задержка
    print("Третье сообщение от корутины 1")
    await asyncio.sleep(delay)  # Третья задержка
    print("Четвертое сообщение от корутины 1")

async def coroutine_2(delay=0.1):
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(0.2)  # Первая задержка
    print("Второе сообщение от корутины 2")
    await asyncio.sleep(delay)  # Вторая задержка
    print("Третье сообщение от корутины 2")
    await asyncio.sleep(0.7)  # Третья задержка
    print("Четвертое сообщение от корутины 2")


async def coroutine_3(delay=0.1):
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(delay)  # Первая задержка
    print("Второе сообщение от корутины 3")
    await asyncio.sleep(0.3)  # Вторая задержка
    print("Третье сообщение от корутины 3")
    await asyncio.sleep(0.4)  # Третья задержка
    print("Четвертое сообщение от корутины 3")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )

asyncio.run(main())