# Import modules
import requests
import json
import datetime

# Define the countries and cities
countries = ["Netherlands", "Belgium", "Germany"]
cities = {"Netherlands": ["Amsterdam", "Rotterdam", "Utrecht"],
          "Belgium": ["Brussels", "Antwerp", "Ghent"],
          "Germany": ["Berlin", "Munich", "Cologne"]}

# Define the API key and the base URL for the OpenWeatherMap API
api_key = "YOUR_API_KEY"
base_url = "http://api.openweathermap.org/data/2.5/"

# Create an empty list to store the weather data
weather_data = []

# Loop through each country and each city and get the current and predicted weather data
for country in countries:
    for city in cities[country]:
        # Build the full URL with the city name and the API key
        full_url = base_url + "weather?q=" + city + "&appid=" + api_key + "&units=metric&lang=en"
        # Send a GET request to the API and get the response as a JSON object
        response = requests.get(full_url).json()
        # Extract the relevant information from the response, such as the city name, the temperature, the humidity, the wind speed and the weather description
        city_name = response["name"]
        temperature = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]
        weather_description = response["weather"][0]["description"]
        # Add this information to the weather data list as a dictionary
        weather_data.append({"country": country,
                         "city": city_name,
                         "temperature": temperature,
                         "humidity": humidity,
                         "wind_speed": wind_speed,
                         "weather_description": weather_description})
        
        # Build the full URL for the forecast of the next day with the same parameters as above
        full_url = base_url + "forecast?q=" + city + "&appid=" + api_key + "&units=metric&lang=en"
        # Send a GET request to the API and get the response as a JSON object
        response = requests.get(full_url).json()
        # Extract the relevant information from the response for the forecast of tomorrow at 12:00, such as the temperature, the humidity, the wind speed and the weather description
        # We use here the index 5 of the list of forecasts, which corresponds to 24 hours after the current time
        temperature_forecast = response["list"][5]["main"]["temp"]
        humidity_forecast = response["list"][5]["main"]["humidity"]
        wind_speed_forecast = response["list"][5]["wind"]["speed"]
        weather_description_forecast = response["list"][5]["weather"][0]["description"]
        # Add this information to the weather data list as a dictionary
        weather_data.append({"country": country,
                         "city": city_name,
                         "temperature_forecast": temperature_forecast,
                         "humidity_forecast": humidity_forecast,
                         "wind_speed_forecast": wind_speed_forecast,
                         "weather_description_forecast": weather_description_forecast})

# Print the weather data list in a readable format
for item in weather_data:
    # If the item contains the current weather data, print a line with the city name, the country, the temperature, the humidity, the wind speed and the weather description
    if "temperature" in item:
        print(f"The weather in {item['city']}, {item['country']} is now: {item['temperature']}°C, {item['humidity']}% humidity, {item['wind_speed']} m/s wind and {item['weather_description']}.")
    # If the item contains the predicted weather data, print a line with the city name, the country, the predicted temperature, the predicted humidity, the predicted wind speed and the predicted weather description
    elif "temperature_forecast" in item:
        print(f"The forecast for tomorrow in {item['city']}, {item['country']} is: {item['temperature_forecast']}°C, {item['humidity_forecast']}% humidity, {item['wind_speed_forecast']} m/s wind and {item['weather_description_forecast']}.")

# Import the matplotlib module
import matplotlib.pyplot as plt

# Create an empty list to store the city names
city_names = []
# Create an empty list to store the current temperatures
current_temperatures = []
# Create an empty list to store the forecasted temperatures
forecasted_temperatures = []

# Loop through the weather data list and extract the city names, current temperatures and forecasted temperatures
for item in weather_data:
    # If the item contains the current weather data, append the city name and the temperature to the corresponding lists
    if "temperature" in item:
        city_names.append(item["city"])
        current_temperatures.append(item["temperature"])
    # If the item contains the forecasted weather data, append the temperature to the corresponding list
    elif "temperature_forecast" in item:
        forecasted_temperatures.append(item["temperature_forecast"])

# Create a figure and a subplot
fig, ax = plt.subplots()
# Set the title of the plot
ax.set_title("Temperature changes for different cities")
# Set the x-axis label
ax.set_xlabel("City")
# Set the y-axis label
ax.set_ylabel("Temperature (°C)")
# Plot the current temperatures as a blue bar chart
ax.bar(city_names, current_temperatures, color="blue", label="Current")
# Plot the forecasted temperatures as a red bar chart
ax.bar(city_names, forecasted_temperatures, color="red", label="Forecast", alpha=0.5)
# Add a legend to the plot
ax.legend()
# Show the plot
plt.show()
