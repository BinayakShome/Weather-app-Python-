from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

def data_get():
    city=city_name.get()
    api_key = '30d4741c779ba94c470ca1f63045390a'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"

    response = requests.get(url)
    weather_data = response.json()
    hum_label1.config(text=f'{weather_data["main"]["humidity"]} %')
    wb_label1.config(text=f'{weather_data["weather"][0]["description"]}')
    temp_label1.config(text=f'{(weather_data["main"]["temp"]-32)*5/9:.2f}°C')
    ws_label1.config(text=f'{weather_data["wind"]["speed"]} m/s')

win = Tk()
win.title("Weather")
win.geometry("500x570")

filename=PhotoImage(file="C:\\Users\\KIIT0001\\Desktop\\Coding\\Web Development Projects\\Images\\pyimage.png")
background_label=Label(win,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)


name_label = Label(win,text="Weather App", font=("Time new Roman",30,"bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Agartala","Amritsar","Agra","Bangalore","Bhopal","Bhubaneswar","Chennai","Delhi","Dehradun","Dhanbad","Hyderabad","Guwahati","Kolkata","Kota","Mumbai","Nagpur","Patna","Silchar","Srinagar"]


com = ttk.Combobox(win,text="Weather App", values= list_name,font=("Time new Roman",20,"bold"),textvariable=city_name)
name_label.place(x=25, y=50, height=50, width=450)
com.place(x=25, y=120, height=50, width=450)


wb_label = Label(win,text="Weather Description", font=("Time new Roman",15,"bold"))
wb_label.place(x=25, y=260, height=50, width=210)

wb_label1 = Label(win, text="", font=("Time new Roman",15,))
wb_label1.place(x=250, y=260, height=50, width=210)

temp_label = Label(win,text="Temperature", font=("Time new Roman",15,"bold"))
temp_label.place(x=25, y=330, height=50, width=210)

temp_label1 = Label(win, text="", font=("Time new Roman",15,"bold"))
temp_label1.place(x=250, y=330, height=50, width=210)

ws_label = Label(win,text="Wind Speed", font=("Time new Roman",15,"bold"))
ws_label.place(x=25, y=400, height=50, width=210)

ws_label1 = Label(win, text="" , font=("Time new Roman",15,"bold"))
ws_label1.place(x=250, y=400, height=50, width=210)

hum_label = Label(win,text="Humidity", font=("Time new Roman",15,"bold"))
hum_label.place(x=25, y=470, height=50, width=210)

hum_label1 = Label(win, text="", font=("Time new Roman",15,"bold"))
hum_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win,text="Done",font=("Time new Roman",15,"bold"),command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()