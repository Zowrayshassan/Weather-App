
from tkinter import Tk, Label, PhotoImage, StringVar
from tkinter import ttk, Button
import requests 


def fetch_data():
    city = city_name.get()  # Retrieve the selected city
    if not city:
        return
    api_key = "9308978008024e1562ea302f3727aa63"  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if the city was found
        if data.get("cod") != 200:
            weather_label1.config(text="N/A")
            weather_d_label1.config(text="City not found")
            temp_label1.config(text="N/A")
            p_label1.config(text="N/A")
            return
        
        weather_label1.config(text=data["weather"][0]["main"])
        weather_d_label1.config(text=data["weather"][0]["description"])
        temp_celsius = data["main"]["temp"] - 273.15
        temp_label1.config(text=f"{temp_celsius:.2f} °C")
        p_label1.config(text=data["main"]["pressure"])
    except Exception as e:
        print(f"Error: {e}")
        weather_label1.config(text="Error")
        weather_d_label1.config(text="Error")
        temp_label1.config(text="N/A")
        p_label1.config(text="N/A")

window = Tk()
window.title("Weather App")
window.geometry("500x500")
window.configure(bg='#6EACDA')

logo = PhotoImage(file="download.png")
window.iconphoto(False, logo)

name_label = Label(window, text="Weather",
                    font=('Arial Rounded MT Bold', 40, "bold"), fg='#03346E', bg='#6EACDA')
name_label.place(x=0, y=30, height=50, width=500)

list_name = (('PK-JK', 'Azad Jammu & Kashmir'), ('PK-BA', 'Balochistan'), ('PK-TA', 'Federally Administered Tribal Areas'),             ('PK-GB', 'Gilgit-Baltistan'), ('PK-IS', 'Islamabad'), ('PK-KP', 'Khyber Pakhtunkhwa'), ('PK-PB', 'Punjab'),
             ('PK-SD', 'Sindh'))
city_name = StringVar()
com = ttk.Combobox(window, text="Weather", values=[name for code, name in list_name],
                   font=('arial', 12), textvariable=city_name)
com.place(x=60, y=100, height=40, width=400)

weather_label = Label(window, text="Climate",
                      font=('Arial', 15, "bold"), fg='#03346E', bg='#6EACDA')
weather_label.place(x=32, y=260, height=50, width=100)

weather_label1 = Label(window, text="",
                       font=('Arial', 15, "bold"), fg='#03346E')
weather_label1.place(x=300, y=260, height=35, width=120)

weather_d_label = Label(window, text="Weather Description",
                        font=('Arial', 15, "bold"), fg='#03346E', bg='#6EACDA')
weather_d_label.place(x=49, y=305, height=50, width=200)

weather_d_label1 = Label(window, text="",
                         font=('Arial', 15, "bold"), fg='#03346E')
weather_d_label1.place(x=300, y=310, height=35, width=150)

temp_label = Label(window, text="Temperature",
                   font=("Arial", 15, "bold"), fg="#03346E", bg="#6EACDA")
temp_label.place(x=16, y=350, height=50, width=190)

temp_label1 = Label(window, text="",
                    font=('Arial', 15, "bold"), fg='#03346E')
temp_label1.place(x=300, y=360, height=35, width=120)

p_label = Label(window, text="Pressure",
                font=("Arial", 15, "bold"), fg="#03346E", bg="#6EACDA")
p_label.place(x=3, y=397, height=50, width=190)

p_label1 = Label(window, text="",
                 font=('Arial', 15, "bold"), fg='#03346E')
p_label1.place(x=300, y=410, height=35, width=120)

done_button = Button(window, text="Done",
                     font=('arial', 12), command=fetch_data)
done_button.place(x=180, y=170, height=40, width=140)

window.mainloop()








