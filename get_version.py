import requests

url = "https://labrza.ru/api/v1/version/"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Версия API:", data)
except requests.exceptions.RequestException as e:
    print("Ошибка при обращении к API:", e)