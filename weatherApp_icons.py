import os               # Functions to interact with Operating System
import urllib.request  # Defines Functions and Classes which help in opening URL's

day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']     # List of Photo's for Day
night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']   # List of Photo's for Night

base_url = 'https://openweathermap.org/img/w/'            # URL to fetch the photos from
img_dir = './img/'                                        # Creating an Image directory
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

for name in day:
    file_name = img_dir+name
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(base_url+name, file_name)         # Request the required image and assign appropriate name

for name in night:
    file_name = img_dir+name
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(base_url+name, file_name)         # Request the required image and assign appropriate name
