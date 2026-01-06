import asyncio
import random

students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}


async def study_course(student: str):
    course = students[student]['course']
    print(f'{student} начал проходить курс {course}.')
    reading_time = students[student]['steps'] / students[student]['speed']
    reading_time = round(reading_time, 2)
    await asyncio.sleep(reading_time)
    print(f'{student} прошел курс {course} за {reading_time} ч.')


async def main():
    tasks = []
    for student in students:
        tasks.append(asyncio.create_task(study_course(student)))
    await asyncio.gather(*tasks)

asyncio.run(main())

