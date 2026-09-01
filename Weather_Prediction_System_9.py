# Project 25 - Weather Prediction System

print("=" * 45)
print("          WEATHER PREDICTION SYSTEM")
print("=" * 45)

temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
cloud_cover = float(input("Enter cloud cover (%): "))
wind_speed = float(input("Enter wind speed (km/h): "))

print("\n" + "=" * 45)
print("          WEATHER ANALYSIS")
print("=" * 45)

if humidity >= 80 and cloud_cover >= 70:
    prediction = "Rainy"
    reason = "High humidity and heavy cloud cover"

elif cloud_cover >= 70:
    prediction = "Cloudy"
    reason = "High cloud cover detected"

elif temperature >= 32 and humidity < 60:
    prediction = "Sunny"
    reason = "High temperature with low humidity"

elif wind_speed >= 35:
    prediction = "Stormy"
    reason = "Very high wind speed detected"

else:
    prediction = "Partly Cloudy"
    reason = "Weather conditions are moderate"

print(f"Temperature : {temperature}°C")
print(f"Humidity    : {humidity}%")
print(f"Cloud Cover : {cloud_cover}%")
print(f"Wind Speed  : {wind_speed} km/h")

print("\nPREDICTION")
print(f"Weather : {prediction}")
print(f"Reason  : {reason}")

print("=" * 45)
print("          Thank you for using the system!")
print("=" * 45)
