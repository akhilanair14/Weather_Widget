import tkinter as tk
from tkinter import font          # Font Library
import requests                   # Library to send request to API
from PIL import Image, ImageTk    # Pillow libraries for Pictures
import datetime                   # Date time Library for Sunrise and Sunset Conversion

app = tk.Tk()                    # Create the GUI Window using the Tk() Function
app.title("My Weather Widget")   # App Title

HEIGHT =420                      # Initializing my Canvas measurement
WIDTH = 550                      # Initializing Canvas Measurement


# 5fcda53ff8126e670af0ac16244e595d
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

def format_response(weather):  # function to format the retrieved data
    try:
        name = weather['name']   # Getting the City Name
        desc = weather['weather'][0]['description']   # Getting the description of weather from JSON Data
        temp = weather['main']['temp']                # Getting the temperature from JSON Data
        feels_like = weather['main']['feels_like']    # Getting Feels Like value from JSON Data
        sunrise = weather['sys']['sunrise']           # Getting the time and date of Sunrise
        sunset = weather['sys']['sunset']             # Getting the time and date of Sunset
        val1 = datetime.datetime.fromtimestamp(sunrise)  # Converting Unix time to date
        val2 = datetime.datetime.fromtimestamp(sunset)   # Converting Unix time to date

        # Printing the result
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s \nFeels Like (°F): %d \nSunrise at: %s \nSunset at: %s ' % (name, desc, temp, feels_like, val1, val2)

    except:
        final_str = 'Invalid Entry'     # If the Input field is invalid

    return final_str


def get_weather(city):  # Function to get weather
    weather_key = '5fcda53ff8126e670af0ac16244e595d'
    url = 'https://api.openweathermap.org/data/2.5/weather'          # Current Weather API
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}  # Initializing the APP ID to weather key
    response = requests.get(url, params=params)  # requesting the information
    weather = response.json()   # storing the response in weather variable


    label['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']  # for icon image
    open_image(icon_name)


def open_image(icon):
    size = int(lower_frame.winfo_height() * 0.4)  # setting the height of the icon image
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)          # Draw Shapes in Application
background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)
canvas.pack()                                      # .pack() the widgets into the window

frame = tk.Frame(app, bg='sky blue', bd=5)         # Container Widget
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Helvetica', 12))  # Place to enter Zipcode or City, Single line text field to get value from user
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Helvetica', 12), command=lambda: get_weather(entry.get()))  #  Display Get Weather Button
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='sky blue', bd=10)  # creating the lower frame
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
label = tk.Label(lower_frame, font=('Helvetica', 26, 'bold'), fg='steel blue', bd=4) # Font of Result
label.config(font=40, bg=bg_color)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg=bg_color, bd=0, highlightthickness=0)  # icon measurements
weather_icon.place(relx=0.78, rely=0, relwidth=1, relheight=0.5)

app.mainloop() # Method to execute the application - Loops forever Until the app is closed  or program is terminated
