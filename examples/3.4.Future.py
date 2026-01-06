import asyncio
import random

#1
async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value

async def create_and_use_future():
    task = asyncio.create_task(set_future_result('Успех', 2))
    if not task.done():
        print("Состояние Task до выполнения: Ожидание")
    else:
        print("Состояние Task до выполнения: Завершено")

    print("Задача запущена, ожидаем завершения...")
    await task
    
    if task.done():
        print("Состояние Task после выполнения: Завершено")
    else:
        print("Состояние Task после выполнения: Ожидание")

    result = task.result()
    print("Результат из Task:", result)

# asyncio.run(create_and_use_future())

#2
async def async_operation():
    print("Начало асинхронной операции.")
    try:
        await asyncio.sleep(2)
        print("Асинхронная операция успешно завершилась.")
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        raise

async def main():
    print("Главная корутина запущена.")
    task = asyncio.create_task(async_operation())
    await asyncio.sleep(0.1)
    print("Попытка отмены Task.")
    task.cancel()
    try:
        await task
        print("Результат Task:", task.result())
    except:
        print("Обработка исключения: Task был отменен.")
    
        if task.cancelled():
            print("Проверка: Task был отменен.")
        else:
            print("Проверка: Task не был отменен.")
    
    print("Главная корутина завершена.")
# asyncio.run(main())

#3
async def first_function(x: int):
    print(f"Выполняется первая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 1
    print(f"Первая функция завершилась с результатом {result}")
    return result

async def second_function(x: int):
    print(f"Выполняется вторая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x * 2
    print(f"Вторая функция завершилась с результатом {result}")
    return result

async def third_function(x: int):
    print(f"Выполняется третья функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 3
    print(f"Третья функция завершилась с результатом {result}")
    return result

async def fourth_function(x: int):
    print(f"Выполняется четвертая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x ** 2
    print(f"Четвертая функция завершилась с результатом {result}")
    return result

async def main():
    print("Начало цепочки асинхронных вызовов")
    task_1 = asyncio.create_task(first_function(1))
    await task_1
    task_2 = asyncio.create_task(second_function(task_1.result()))
    await task_2
    task_3 = asyncio.create_task(third_function(task_2.result()))
    await task_3
    task_4 = asyncio.create_task(fourth_function(task_3.result()))
    await task_4
    final_result = task_4.result()
    print(f"Конечный результат цепочки вызовов: {final_result}")

# asyncio.run(main())

# 4

async def waiter(future:asyncio.Future):
    await future
    print(f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу")

async def setter(future:asyncio.Future):
    ra = random.randint(1,3)
    await asyncio.sleep(ra)
    future.set_result(True)

async def main():
    future = asyncio.Future()
    task_1 = asyncio.create_task(waiter(future)) 
    task_2 = asyncio.create_task(setter(future)) 
    await asyncio.gather(task_1, task_2)


asyncio.run(main())
