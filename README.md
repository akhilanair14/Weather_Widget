# Weather_Widget
Weather Widget GUI using Python Tkinter

This is Python Weather Widget that uses OpenWeatherMap API and Tkinter

Requirements - Python3, 
               OpenWeatherMap API key (You will get the key if you sign up at https://openweathermap.org/appid.)
               Install requests package in Python
               Install Python Imaging Library
               Tkinter is pre installed with Python 

This Widget takes Zipcodes, City Name as Input and provides Temperature and Sunrise and Sunset times at output. It displays the current weather data. The weather icon changes according to the temperature and takes the input from weather_icon.py file. weather_icon.py fetches the image from openweathermap API.

Use Pyinstaller to make this into an exectuable file with this command: pyinstaller.exe --onefile --icon=app_icon.ico WeatherApp.py. You will need pyinstaller installed for this 
purpose.

Please refer About the App document for additional information. 




