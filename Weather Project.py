from tkinter import*
from tkinter import ttk
import requests
def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=759e6e7cd8bd54bf316dfe3ebfdb6f39").json()
    WClimate1.config(text=data["weather"][0]["main"])
    Wdesc1.config(text=data["weather"][0]["description"])
    Temp1.config(text=str(int(data["main"]["temp"]-273.15)))
    TempMix1.config(text=data["main"]["temp_min"])
    TempMax1.config(text=data["main"]["temp_max"])
    Press1.config(text=data["main"]["pressure"])
    
    
win=Tk()
win.title("Weather ForeCast")
win.config(bg="pink")
win.geometry("500x570")

name_label=Label(win,text="Weather Forecast" ,font=("Time New Roman",25,"bold"))
name_label.place(x=25,y=50,height=45,width=450)


city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat"
           ,"Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand"
           ,"Karnataka","Kerala","Madhya Pradesh","Maharashtra"
           ,"Manipur","Meghalaya","Mizoram","Nagaland",
           "Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand"
           ,"West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli",
           "Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


com=ttk.Combobox(win,font=("Time New Roman",20,"bold"),values=list_name,textvariable=city_name)
com.place(x=50,y=120,height=35,width=400)



WClimate=Label(win,text="Weather climate" ,font=("Time New Roman",10))
WClimate.place(x=25,y=230,height=30,width=150)

WClimate1=Label(win,text="" ,font=("Time New Roman",10))
WClimate1.place(x=200,y=230,height=30,width=200)


Wdesc=Label(win,text="Weather Description" ,font=("Time New Roman",10))
Wdesc.place(x=25,y=280,height=30,width=150)

Wdesc1=Label(win,text="" ,font=("Time New Roman",10))
Wdesc1.place(x=200,y=280,height=30,width=200)


Temp=Label(win,text="Temprature" ,font=("Time New Roman",10))
Temp.place(x=25,y=330,height=30,width=150)

Temp1=Label(win,text="" ,font=("Time New Roman",10))
Temp1.place(x=200,y=330,height=30,width=200)


TempMix=Label(win,text="Temprature Mix" ,font=("Time New Roman",10))
TempMix.place(x=25,y=380,height=30,width=150)

TempMix1=Label(win,text=" " ,font=("Time New Roman",10))
TempMix1.place(x=200,y=380,height=30,width=200)


TempMax=Label(win,text="Temprature Max" ,font=("Time New Roman",10))
TempMax.place(x=25,y=430,height=30,width=150)

TempMax1=Label(win,text=" " ,font=("Time New Roman",10))
TempMax1.place(x=200,y=430,height=30,width=200)

Press=Label(win,text="Pressure" ,font=("Time New Roman",10))
Press.place(x=25,y=480,height=30,width=150)

Press1=Label(win,text="" ,font=("Time New Roman",10))
Press1.place(x=200,y=480,height=30,width=200)


btn=Button(win,text="Check Weather" ,font=("Time New Roman",15),command=data_get)
btn.place(x=150,y=175,height=30,width=200)




win.mainloop()

