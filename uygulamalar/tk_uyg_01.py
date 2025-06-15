# 1-150 arasında rastgele 5 sayı üreten 
# Yazdır buttonuna tıklayınca bu sayıları yazdıran
# Yazdıra basınca her zaman rastgele üretir
# Saydamlaştır buttonuna basınca saydamlaştıran
# Dondur butonu saydamlaştırmayı sonlandırıp
# Maksimum ve minimum da ekran ayarı yapar...

import tkinter as tk
import random as rd

gui = tk.Tk()
gui.title("Rastgele Sayılar")
gui.geometry("500x500")

def rastgele():
    global liste
    liste = []
    for i in range(5):
        while len(liste)!=5:
            b = rd.randint(1, 150)
            if b  not in liste:
                liste.append(b)

def yazdir():
    rastgele()
    tk.Label(gui, text = liste).pack()

def saydamlastir():
    gui.wm_attributes("-alpha", 0.3)
    
def dondur():
    gui.wm_attributes("-alpha", 0.9)

def maxyap():
    gui.attributes("-fullscreen", True)
    # gui.state("zoomed") --> Bu sadece Windows işletim sistemlerinde çalışır...

def normal():
    gui.attributes("-fullscreen", False)
    
def minyap():
    gui.state("iconic")

tk.Button(gui, text="yazdır..", command = yazdir, fg="black", bg="yellow").pack()
tk.Button(gui, text="Saydam..", command = saydamlastir, fg="black", bg="yellow").pack()
tk.Button(gui, text="S_Döndür..", command = dondur, fg="black", bg="yellow").pack()
tk.Button(gui, text="Maksimum..", command = maxyap, fg="black", bg="yellow").pack()
tk.Button(gui, text="Normal...", command = normal, fg="black", bg="yellow").pack()
tk.Button(gui, text="Minimum..", command = minyap, fg="black", bg="yellow").pack()

gui.mainloop()

