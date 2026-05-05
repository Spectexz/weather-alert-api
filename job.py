from main import send_alert, get_weather_data

def job():
    data = get_weather_data(city='Jakarta')
    text = f"Good Morning! \nCity:{data.get('Location')} \nTemperature: {data.get('Temperature')} \nCondition: {data.get('Condition')} \nHumidity: {data.get('Humidity')}"
    send_alert(text)

job()