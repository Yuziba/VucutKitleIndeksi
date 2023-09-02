import tkinter

window = tkinter.Tk()
window.title("Vucut Kutle Indexi")
window.minsize(width=300, height=500)

sonuc = ""
def KiloBilgisiAl():
    kullaniciKilosu = int(entryKilo.get())      #Kilogram
    kullaniciBoyu = int(entryBoy.get())/100     #Metre
    vki = kullaniciKilosu/(kullaniciBoyu * kullaniciBoyu)

    if vki<18:
        sonuc = "Cok Zayifsiniz"
    elif 18<=vki<25:
        sonuc = "Kilonuz ideal"
    elif 25<=vki<30:
        sonuc = "Kilonuz biraz fazla"
    elif vki>=30:
        sonuc = "Cooook kilolusnuz"
    else:
        sonuc = "gecerli bir deger giriniz"
    print(vki)
    labelSonuc.config(text=sonuc)


labelKilo = tkinter.Label(text="Kilo bilginizi giriniz")
labelKilo.pack()

entryKilo = tkinter.Entry()
entryKilo.pack()

labelBoy = tkinter.Label(text="Boy bilginizi giriniz")
labelBoy.pack()
entryBoy = tkinter.Entry()
entryBoy.pack()

buttonKilo = tkinter.Button(text="Onayla",command=KiloBilgisiAl)
buttonKilo.pack(pady=20)

labelSonuc = tkinter.Label(text="aa")
labelSonuc.pack()












window.mainloop()

