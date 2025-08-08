import requests


def get_weather(city):
    params = {"name": city, "count": 1, "format": "json"}
    response_city = requests.get(
        url=f"https://geocoding-api.open-meteo.com/v1/search",
        params=params
    )
    try:
        result_city = response_city.json()["results"][0]
        latitude = result_city["latitude"]
        longitude = result_city["longitude"]
    except:
        print("Города с таким названием нет в списке доступных\n")
        return

    params2 = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "timezone": "auto"
    }
    response_weather = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params=params2
    )
    try:
        temps = response_weather.json()["hourly"]["temperature_2m"]
    except:
        print("Ошибка при получении данных о погоде =(\n")
        return
    print(
        f"Погода для города: {result_city['name']}\n"
        f"Сегодня ночью: {temps[3]} °C\n"
        f"Сегодня днём: {temps[14]} °C\n"
        f"Сегодня вечером: {temps[20]} °C\n"
    )


while True:
    city = input("Введите название города на английском или 111 для выхода: ")
    if city == "111":
        break
    elif len(city) < 3 or len(city) > 50:
        print("Название города должно быть от 3 до 50 символов!\n")
        continue
    elif not city.isascii():
        print("Название города должно быть на английском!\n")
        continue
    elif not city.isalpha():
        flag = True
        for i in city:
            if i not in "-. " and not i.isalpha():
                flag = False
        if not flag:
            print("В названии города не должно быть недопустимых символов, введится валидное название!\n")
            continue
        else:
            get_weather(city)
    else:
        get_weather(city)
