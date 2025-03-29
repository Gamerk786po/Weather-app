# importing required libraries/modules
import requests
import json
# Main program
# running a while loop for infinite loop
while True:
    try:
        print("-------------------------------------------------------------------")
        print("****Enter exit to exit program..***")
        city_name = input("Enter the name of city or exit: ").capitalize().split()
        print("-------------------------------------------------------------------")
        # Main condition
        if "Exit" in city_name:
            break
        else:
            # assigning variables and others
            base_url = "http://api.openweathermap.org/data/2.5/forecast"
            api_key = "b7c4a2d6f48b37b752338b80f51ed58b"
            payload = {
                "q": city_name,
                "units": "metric",
                "appid": api_key
            }
            # Making a request
            response = requests.get(base_url, params=payload)
            # status code condition
            if response.status_code == 200:
                try:
                    data = response.json()
                    # indexing
                    # temperature info
                    temp = round(data['list'][0]['main']['temp'])
                    feels_like = round(data['list'][0]['main']['feels_like'])
                    min_temp = round(data['list'][0]['main']['temp_min'])
                    max_temp = round(data['list'][0]['main']['temp_max'])
                    humidity = round(data['list'][0]['main']['humidity'])
                    # weather info
                    main_weather = data['list'][0]['weather'][0]['main']
                    weather_condition = data['list'][0]['weather'][0]['description']
                    # rain and snow probability
                    pop = data['list'][0]['pop'] * 100
                    # wind info
                    wind_speed = round(data['list'][0]['wind']['speed'])
                    # giving output
                    print("-------------------------------------------------------------------")
                    print("Weather info:")
                    # temperature info
                    print("Temperature:")
                    print(f"\t Temperature: {temp}°C")
                    print(f"\t Feels like: {feels_like}°C")
                    print(f"\t Minimum temperature: {min_temp}°C")
                    print(f"\t Maximum temperature: {max_temp}°C")
                    print(f"\t Humidity: {humidity}%")
                    # weather info
                    print("Weather:")
                    print(f"\t Weather: {main_weather}({weather_condition})")
                    # precipitation
                    print("Precipitation condition:")
                    print(f"\t Precipitation percentage: {pop}%")
                    # wind
                    print("Wind condition:")
                    print(f"\t Wind speed: {wind_speed}km/h ")
                    print("-------------------------------------------------------------------")
                except json.JSONDecodeError as j:
                    print(f"Error : {j}")
                except KeyError as k:
                    print(f"Error : {k}")
                except ConnectionError as c:
                    print(f"Error : {c}")
                except Exception as e:
                    print(f"Error : {e}")
            else:
                print("Request failed..")
    except ConnectionError as c:
        print(f"Error: Connection failed..")
    except Exception as e:
        print(f"Error: {e}")
print("The weather app program has ended..")
