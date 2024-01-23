from tkinter import *
from tkinter import ttk
import requests

def dataget():
    city=city_name.get()
    
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    wlabel1.config(text=data['weather'][0]['main'])
    wdlabel1.config(text=data['weather'][0]['description'])
    templabel1.config(text=str(int(data['main']['temp']-273.15)))
    prelabel1.config(text=data['main']['pressure'])

    
w=Tk()
w.title("weather app")
w.config(bg="blue")
w.geometry("600x600")
name=Label(w,text="Weather App",font=("Time New Roman",30,"bold"))
name.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
statenames=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(w,text="",values=statenames,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=150,height=50,width=450)

wlabel=Label(w,text="weather Climate",font=("Time New Roman",20))
wlabel.place(x=25,y=280,height=50,width=210)

wlabel1=Label(w,text="",font=("Time New Roman",20))
wlabel1.place(x=270,y=280,height=50,width=210)

wdlabel=Label(w,text="weather Description",font=("Time New Roman",20))
wdlabel.place(x=25,y=350,height=50,width=210)

wdlabel1=Label(w,text="",font=("Time New Roman",20))
wdlabel1.place(x=270,y=350,height=50,width=210)

templabel=Label(w,text="Temperature",font=("Time New Roman",20))
templabel.place(x=25,y=410,height=50,width=210)

templabel1=Label(w,text="",font=("Time New Roman",20))
templabel1.place(x=270,y=410,height=50,width=210)

prelabel=Label(w,text="pressure",font=("Time New Roman",20))
prelabel.place(x=25,y=470,height=50,width=210)

prelabel1=Label(w,text="",font=("Time New Roman",20))
prelabel1.place(x=270,y=470,height=50,width=210)

doneb=Button(w,text="Done",font=("Time New Roman",20,'bold'),command=dataget)
doneb.place(y=210,height=50,width=100,x=200)




    
