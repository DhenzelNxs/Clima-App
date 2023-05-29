from tkinter import * 
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz 
from PIL import Image, ImageTk


root=Tk()
root.title('Previsão do Tempo')
root.geometry('890x470+300+300')
root.configure(bg='#57adff')
root.resizable(False,False)

def create_gradient(canvas, width, height, color1, color2):
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * (y / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (y / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (y / height))
        color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        canvas.create_rectangle(0, y, width, y + 1, fill=color, width=0)


def getWather():
    try:
        city=textfield.get().strip()

        if city.strip() != '':
            geolocator=Nominatim(user_agent='geoapiExercises')
            location = geolocator.geocode(city)
            
            obj=TimezoneFinder()

            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

            timezone.config(text=result)
            long_lat.config(text=f'{round(location.latitude,4)}°N,{round(location.longitude,4)}°E')

            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime('%I:%M %p')
            clock.config(text=current_time)

            api="https://api.openweathermap.org/data/2.8/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid={API Key}"
            json_data = requests.get(api).json()

            temp = json_data['current']['temp']
            humidity = json_data['current']['humidity']
            pressure = json_data['current']['pressure']
            wind = json_data['current']['wind_speed']
            description = json_data['current']['weather'][0]['description']

            t.config(text=(temp,'°C'))
            h.config(text=(humidity,'%'))
            p.config(text=(pressure,'hPa'))
            w.config(text=(wind,'m/s'))
            d.config(text=description)


            dia1img=json_data['daily'][0]['weather'][0]['icon']
            imagem1= ImageTk.PhotoImage(file=f'CadastroApp/icon/{dia1img}@2x.png')
            img1.config(image=imagem1)
            img1.image=imagem1

            temp1 = json_data['daily'][0]['temp']['day']
            night1 = json_data['daily'][0]['temp']['night']

            dia1temp.config(text=f'Dia:{temp1}°C\nNoite:{night1}°C')

            dia2img=json_data['daily'][1]['weather'][0]['icon']
            img=(Image.open(f'CadastroApp/icon/{dia2img}@2x.png'))
            img_mod = img.resize((50,50))
            imagem2 = ImageTk.PhotoImage(img_mod)
            img2.config(image=imagem2)
            img2.image=imagem2

            temp2 = json_data['daily'][1]['temp']['day']
            night2 = json_data['daily'][1]['temp']['night']

            dia2temp.config(text=f'Dia:{temp2}\nNoite:{night2}')

            dia3img=json_data['daily'][2]['weather'][0]['icon']
            img=(Image.open(f'CadastroApp/icon/{dia3img}@2x.png'))
            img_mod = img.resize((50,50))
            imagem3 = ImageTk.PhotoImage(img_mod)
            img3.config(image=imagem3)
            img3.image=imagem3

            temp3 = json_data['daily'][2]['temp']['day']
            night3 = json_data['daily'][2]['temp']['night']

            dia3temp.config(text=f'Dia:{temp3}\nNoite:{night3}')

            dia4img=json_data['daily'][3]['weather'][0]['icon']
            img=(Image.open(f'CadastroApp/icon/{dia4img}@2x.png'))
            img_mod = img.resize((50,50))
            imagem4 = ImageTk.PhotoImage(img_mod)
            img4.config(image=imagem4)
            img4.image=imagem4

            temp4 = json_data['daily'][3]['temp']['day']
            night4 = json_data['daily'][3]['temp']['night']

            dia4temp.config(text=f'Dia:{temp4}\nNoite:{night4}')

            dia5img=json_data['daily'][4]['weather'][0]['icon']
            img=(Image.open(f'CadastroApp/icon/{dia5img}@2x.png'))
            img_mod = img.resize((50,50))
            imagem5 = ImageTk.PhotoImage(img_mod)
            img5.config(image=imagem5)
            img5.image=imagem5

            temp5 = json_data['daily'][4]['temp']['day']
            night5 = json_data['daily'][4]['temp']['night']

            dia5temp.config(text=f'Dia:{temp5}\nNoite:{night5}')


            dia6img=json_data['daily'][5]['weather'][0]['icon']
            img=(Image.open(f'CadastroApp/icon/{dia6img}@2x.png'))
            img_mod = img.resize((50,50))
            imagem6 = ImageTk.PhotoImage(img_mod)
            img6.config(image=imagem6)
            img6.image=imagem6

            temp6 = json_data['daily'][5]['temp']['day']
            night6 = json_data['daily'][5]['temp']['night']

            dia6temp.config(text=f'Dia:{temp6}\nNoite:{night6}')

            dia7img=json_data['daily'][6]['weather'][0]['icon']
            img=(Image.open(f'CadastroApp/icon/{dia7img}@2x.png'))
            img_mod = img.resize((50,50))
            imagem7 = ImageTk.PhotoImage(img_mod)
            img7.config(image=imagem7)
            img7.image=imagem7

            temp7 = json_data['daily'][6]['temp']['day']
            night7 = json_data['daily'][6]['temp']['night']

            dia7temp.config(text=f'Dia:{temp7}\nNoite:{night7}')



            pd = datetime.now()
            dia1.config(text=pd.strftime('%A'))

            sd = pd+timedelta(days=1)
            dia2.config(text=sd.strftime('%A'))

            td = pd+timedelta(days=2)
            dia3.config(text=td.strftime('%A'))

            qd = pd+timedelta(days=3)
            dia4.config(text=qd.strftime('%A'))

            qud = pd+timedelta(days=4)
            dia5.config(text=qud.strftime('%A'))

            sxd = pd+timedelta(days=5)
            dia6.config(text=sxd.strftime('%A'))

            std = pd+timedelta(days=6)
            dia7.config(text=std.strftime('%A'))
        else:
            print('Informe uma cidade existente!')
    except:
        print('Erro de conexão')
    
canvas = tk.Canvas(root, width=890, height=470)
canvas.pack()

color1 = (0,0,0)  # Cor inicial (branca)
color2 = (0, 0, 255)      # Cor final (azul)

create_gradient(canvas, 890,470, color1, color2)

image_icon = PhotoImage(file='CadastroApp/imagens/logo.png')
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file='CadastroApp/imagens/Rounded Rectangle 1.png')
Label(root,image=Round_box,bg='#57adff').place(x=30, y=110)

label1=Label(root,text='Temperatura', font=('Helvetica',11), fg='white', bg='#203243')
label1.place(x=50, y=120)

label2=Label(root,text='Humidade', font=('Helvetica',11), fg='white', bg='#203243')
label2.place(x=50, y=140)

label3=Label(root,text='Pressão', font=('Helvetica',11), fg='white', bg='#203243')
label3.place(x=50, y=160)

label4=Label(root,text='Vel. Vento', font=('Helvetica',11), fg='white', bg='#203243')
label4.place(x=50, y=180)

label5=Label(root,text='Descrição', font=('Helvetica',11), fg='white', bg='#203243')
label5.place(x=50, y=200)


Search_image=PhotoImage(file='CadastroApp/imagens/Rounded Rectangle 3.png')
myimage=Label(image=Search_image,bg='#57adff')
myimage.place(x=270, y=120)

weat_image=PhotoImage(file='CadastroApp/imagens/Layer 7.png')
weatherimage=Label(root,image=weat_image,bg='#203243')
weatherimage.place(x=290, y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg='#203243',border=0,fg='white')
textfield.place(x=370,y=130)
textfield.focus()

Search_icon=PhotoImage(file='CadastroApp/imagens/Layer 6.png')
myimage_icon=Button(image=Search_icon,borderwidth=0, cursor='hand2',bg='#203243',command=getWather)
myimage_icon.place(x=645,y=125)

frame=Frame(root,width=900,height=180,bg='#212120')
frame.pack(side=BOTTOM)

firstbox=PhotoImage(file='CadastroApp/imagens/Rounded Rectangle 2.png')
secondbox=PhotoImage(file='CadastroApp/imagens/Rounded Rectangle 2 copy.png')

Label(frame,image=firstbox,bg='#212120').place(x=30, y=20)
Label(frame,image=secondbox,bg='#212120').place(x=300,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=400,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=500,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=600,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=700,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=800,y=30)


clock=Label(root,text='Horário',font=('Helvetica',30,'bold'),bg='#212120',fg='white')
clock.place(x=30,y=20)

timezone=Label(root,text='Local',font=('Helvetica',20),bg='#212120',fg='white')
timezone.place(x=700,y=20)

long_lat=Label(root,text='Lat/Long',font=('Helvetica',10),bg='#212120',fg='white')
long_lat.place(x=700,y=50)

t=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
t.place(x=150,y=120)

h=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
h.place(x=150,y=140)

p=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
p.place(x=150,y=160)

w=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
w.place(x=150,y=180)

d=Label(root,font=('Helvetica',11),fg='white',bg='#203243')
d.place(x=150,y=200)

primeiro = Frame(root,width=230,height=132,bg='#282829')
primeiro.place(x=35,y=315)

dia1 = Label(primeiro,font='arial 20',bg='#282829',fg='#fff')
dia1.place(x=100, y=5)

img1 = Label(primeiro,bg='#282829')
img1.place(x=1,y=15)

dia1temp = Label(primeiro,bg='#282829',fg='#57adff',font='arial 15 bold')
dia1temp.place(x=95,y=50)

segundo = Frame(root,width=70,height=115,bg='#282829')
segundo.place(x=305,y=325)

dia2 = Label(segundo,bg='#282829',fg='#fff')
dia2.place(x=10, y=5)

img2 = Label(segundo,bg='#282829')
img2.place(x=7,y=20)

dia2temp = Label(segundo,bg='#282829',fg='#fff')
dia2temp.place(x=2,y=70)

terceiro = Frame(root,width=70,height=115,bg='#282829')
terceiro.place(x=405,y=325)

dia3 = Label(terceiro,bg='#282829',fg='#fff')
dia3.place(x=10, y=5)

img3 = Label(terceiro,bg='#282829')
img3.place(x=7,y=20)

dia3temp = Label(terceiro,bg='#282829',fg='#fff')
dia3temp.place(x=2,y=70)

quarto = Frame(root,width=70,height=115,bg='#282829')
quarto.place(x=505,y=325)

dia4 = Label(quarto,bg='#282829',fg='#fff')
dia4.place(x=10, y=5)

img4 = Label(quarto,bg='#282829')
img4.place(x=7,y=20)

dia4temp = Label(quarto,bg='#282829',fg='#fff')
dia4temp.place(x=2,y=70)

quinto = Frame(root,width=70,height=115,bg='#282829')
quinto.place(x=605,y=325)

dia5 = Label(quinto,bg='#282829',fg='#fff')
dia5.place(x=10, y=5)

img5 = Label(quinto,bg='#282829')
img5.place(x=7,y=20)

dia5temp = Label(quinto,bg='#282829',fg='#fff')
dia5temp.place(x=2,y=70)

sexto = Frame(root,width=70,height=115,bg='#282829')
sexto.place(x=705,y=325)

dia6 = Label(sexto,bg='#282829',fg='#fff')
dia6.place(x=10, y=5)

img6 = Label(sexto,bg='#282829')
img6.place(x=7,y=20)

dia6temp = Label(sexto,bg='#282829',fg='#fff')
dia6temp.place(x=2,y=70)

setimo = Frame(root,width=70,height=115,bg='#282829')
setimo.place(x=805,y=325)

dia7 = Label(setimo,bg='#282829',fg='#fff')
dia7.place(x=10, y=5)

img7 = Label(setimo,bg='#282829')
img7.place(x=7,y=20)

dia7temp = Label(setimo,bg='#282829',fg='#fff')
dia7temp.place(x=2,y=70)


root.mainloop()
