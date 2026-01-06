import asyncio

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}
delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}
counters={
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}

async def counter(c_name: str):
    # await asyncio.sleep(sleep_sec)
    while max_counts[c_name] > counters[c_name]:
        await asyncio.sleep(delays[c_name])
        counters[c_name] += 1
        print(f"{c_name}: {counters[c_name]}")

        
async def main():
    task1 = asyncio.create_task(counter("Counter 1"))
    task2 = asyncio.create_task(counter("Counter 2"))
    task3 = asyncio.create_task(counter("Counter 3"))
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())