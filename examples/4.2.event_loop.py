import asyncio
import random

log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Ошибка соединения с БД", "delay": 5.0},
    {"event": "Обновление конфигурации сервера", "delay": 3.5},
    ]

async def fetch_log(event: dict):
	delay = event["delay"]
	await asyncio.sleep(delay)
	event_str = event["event"]
	return f"Событие: '{event_str}' обработано с задержкой {delay} сек."

async def main():
	tasks = []
	for event in log_events:
		tasks.append(asyncio.create_task(fetch_log(event)))
	
	results = await asyncio.gather(*tasks)
	for result in results:
		print(result)

asyncio.run(main())