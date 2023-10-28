import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime,timedelta
from PIL import Image, ImageTk
import requests
import pytz

# Your OpenWeatherMap API key
api_key = "1fcbb3d2c2163d5e91bd1f924c0b6de5"

root = tk.Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.configure(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.configure(text=current_time)

    complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        print("Temperature:", temp)
        print("Humidity:", humidity)
        print("Pressure:", pressure)
        print("Wind Speed:", wind)
        print("Description:", description)
    else:
        print(f"City not found or there was an issue with the request. Status code: {data['cod']}")
    t.config(text=(temp,"k"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hpa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)

    #first cell
    firstdayimage = data['weather'][0]['icon']
    print(firstdayimage)
    photo1 = ImageTk.PhotoImage(file=f"C:\icon/{firstdayimage}@2x.png")

    #second cell
    #seconddayimage = data['weather'][1]['icon']
    #print(seconddayimage)

    #third cell
    #thirddayimage = data['weather'][2]['icon']
    #print(thirddayimage)

    #fourth cell
    #fourthdayimage = data['weather'][3]['icon']
    #print(fourthdayimage)

    #fifth cell
    #fifthtdayimage = data['weather'][4]['icon']
    #print(fifthdayimage)

    #sixth cell
    #sixthdayimage = data['weather'][5]['icon']
    #print(sixthdayimage)

    #seventh cell
    #seventhdayimage = data['weather'][6]['icon']
    #print(seventhdayimage)

    #days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


# Icon
image_icon = tk.PhotoImage(file="C:\Images/logo.png")
root.iconphoto(False, image_icon)

Round_box = tk.PhotoImage(file="C:\Images/Rounded Rectangle 1.png")
tk.Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

label1 = tk.Label(root, text="Temperature", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label1 = tk.Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=140)

label1 = tk.Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=160)

label1 = tk.Label(root, text="Wind Speed", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=180)

label1 = tk.Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=200)

# Searchbox
search_image = tk.PhotoImage(file="C:\Images/Rounded Rectangle 3.png")
myimage = tk.Label(image=search_image, bg="#57adff")
myimage.place(x=290, y=127)

weat_image = tk.PhotoImage(file="C:\Images/Layer 7.png")
weatherimage = tk.Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

search_icon = tk.PhotoImage(file="C:\Images/Layer 6.png")
myimage_icon = tk.Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=645, y=125)

# Bottom box
frame = tk.Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=tk.BOTTOM)

# Bottom boxes
firstbox = tk.PhotoImage(file="C:\Images/Rounded Rectangle 2.png")
secondbox = tk.PhotoImage(file="C:\Images/Rounded Rectangle 2 copy.png")

tk.Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
tk.Label(frame, image=firstbox, bg="#212120").place(x=300, y=30)
tk.Label(frame, image=firstbox, bg="#212120").place(x=400, y=30)
tk.Label(frame, image=firstbox, bg="#212120").place(x=500, y=30)
tk.Label(frame, image=firstbox, bg="#212120").place(x=600, y=30)
tk.Label(frame, image=firstbox, bg="#212120").place(x=700, y=30)
tk.Label(frame, image=firstbox, bg="#212120").place(x=800, y=30)

# Clock (place your clock here)
clock = tk.Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# Timezone (place your timezone here)
timezone = tk.Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = tk.Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

#thpw
t = tk.Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120)
h = tk.Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)
p = tk.Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)
w = tk.Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)
d = tk.Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)

#first cell
firstframe = tk.Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1 = tk.Label(firstframe,font="arial",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage = tk.Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

#second cell
secondframe = tk.Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)

day2 = tk.Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)

secondimage = tk.Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

#third cell
thirdframe = tk.Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)

day3 = tk.Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=5)

thirdimage = tk.Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=5)

secondimage = tk.Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

#fourth cell
fourthframe = tk.Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505, y=325)

day4 = tk.Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=10,y=5)

fourthimage = tk.Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)

#fifth cell
fifthframe = tk.Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)

day5 = tk.Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=10,y=5)

fifthimage = tk.Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)

#sixth cell
sixthframe = tk.Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)

day6 = tk.Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=10,y=5)

sixthimage = tk.Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)

#seventh cell
seventhframe = tk.Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=805,y=325)

day7 = tk.Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=10,y=5)

seventhimage = tk.Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=20)



root.mainloop()
