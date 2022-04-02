# import the module
import python_weather
import asyncio

async def getweather():
    client = python_weather.Client(format=python_weather.IMPERIAL)

    weather = await client.find("Atlanta")

    fahrenheit = weather.current.temperature
    kelven = ( fahrenheit - 32 ) / 1.8 + 273.15
    celsius = kelven -  273.15

    # print(f'Current temperature ', fahrenheit, '°F')
    print(f'Current temperature ', kelven, '°K')
    # print(f'Current temperature ', celsius, '°C')

    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature, '°F')

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())