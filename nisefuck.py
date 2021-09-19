
import tkinter
import os
import sys
from time import sleep
from tkinter import *



def fakewifi():
    fake = Tk()
    fake.geometry("500x500")
    fake.title("fake wifi")
    label = tkinter.Label(fake, text="fake wifi")
    cek_interfaces = tkinter.Button(fake, text="fake wifi", command=fakew)
    start_stop = tkinter.Button(fake, text="change name wifi", command=change_name_wifi)
    tombol2 = tkinter.Button(fake, text="back", command=fake.destroy)
    label.pack()
    cek_interfaces.pack()
    start_stop.pack()
    tombol2.pack()

def airo():
    airodump = Tk()
    airodump.geometry("500x500")
    airodump.title("airodump-ng")
    label = tkinter.Label(airodump, text="airodump")
    scan = tkinter.Button(airodump, text="scanwifi", command=scanwifi)
    cap = tkinter.Button(airodump, text="captures", command=captures)
    tombol2 = tkinter.Button(airodump, text="back", command=airodump.destroy)
    label.pack()
    scan.pack()
    cap.pack()
    tombol2.pack()
    

def monitor():
    monitor_mode = Tk()
    monitor_mode.geometry("500x500")
    monitor_mode.title("monitor mode")
    label = tkinter.Label(monitor_mode, text="monitor mode")
    cek_interfaces = tkinter.Button(monitor_mode, text="check interfaces", command=airmon_ng)
    start_stop = tkinter.Button(monitor_mode, text="start/stop", command=s_t)
    tombol2 = tkinter.Button(monitor_mode, text="back", command=monitor_mode.destroy)
    label.pack()
    cek_interfaces.pack()
    start_stop.pack()
    tombol2.pack()

def aireplay():
    air = Tk()
    air.geometry("500x500")
    air.title("aireplay-ng")
    label = tkinter.Label(air, text="aireplay-ng")
    wifi = tkinter.Button(air, text="attack wifi", command= wifi_attack)
    client = tkinter.Button(air, text="attack client", command=client_attack)
    tombol2 = tkinter.Button(air, text="back", command=air.destroy)
    label.pack()
    wifi.pack()
    client.pack()
    tombol2.pack()

def aircrack():
    air = Tk()
    air.geometry("500x500")
    air.title("aircrack-ng")
    label = tkinter.Label(air, text="are you going to use aircrack-ng y/n:")
    enter = tkinter.Button(air, text="yes", command=aircrack_ng)
    kembali = tkinter.Button(air, text="back", command=air.destroy)
    label2 = tkinter.Label(air, text="if not click below")
    label.pack()
    enter.pack()
    label2.pack()
    kembali.pack()

def aircrack_ng():
    os.system("konsole -geometry 600x500 --hold -e python3 /opt/nisefuck/lib/aircrack-ng.py")

def client_attack():
    os.system("konsole -geometry 600x500 --hold -e python3 /opt/nisefuck/lib/attack-client.py")

def wifi_attack():
    os.system("konsole -geometry 600x500 --hold -e python3 /opt/nisefuck/lib/attack-wifi.py")

def s_t():
    os.system("xterm -bg black -fg white -hold -geometry 101x27 -e python3 /opt/nisefuck/lib/start.py")
 

def airmon_ng():
    os.system("xterm -bg black -fg white -hold -geometry 101x27 -e python3 /opt/nisefuck/lib/cek.py")
    

def scanwifi():
    os.system("konsole --hold -geometry 900x500 -e python3 /opt/nisefuck/lib/scanwifi.py")

def captures():
    os.system("konsole --hold -geometry 900x500 -e python3 /opt/nisefuck/lib/captures.py")

def fakew():
    os.system("konsole --hold -geometry 900x500 -e python3 /opt/nisefuck/lib/fakewifi.py")

def change_name_wifi():
    os.system("konsole --hold -geometry 900x500 -e python3 /opt/nisefuck/lib/change-wifi.py")
def tentang():
    ten = Tk()
    ten.title("about")
    githubb = tkinter.Label(ten, text="\ngithub:https://github.com/alanlol12\n")
    pem = tkinter.Label(ten, text="\nby: who")
    des = tkinter.Label(ten, text="\nwificrack use aircrack-ng\n")
    githubb.pack()
    pem.pack()
    des.pack()
def phising():
    os.system("konsole --hold -geometry 900x500 -e python3 /opt/nisefuck/lib/phising.py")

def wifi():
    awal = Tk()
    menu = Menu(awal)

    awal.config(menu=menu)

    

    awal.title("wificrack")
    awal.geometry("500x500")
    filemenu = Menu(menu)
    menu.add_cascade(label="info", menu=filemenu)
    filemenu.add_command(label="about", command=tentang)
    Label = tkinter.Label(awal, text="thanks for use this script")
    moni = tkinter.Button(awal, text="monitor mode", command=monitor)
    tombol = tkinter.Button(awal, text="airodump-ng", command=airo)
    airep = tkinter.Button(awal, text="aireplay-ng", command=aireplay)
    ai = tkinter.Button(awal, text="aircrack-ng", command=aircrack)
    fake = tkinter.Button(awal, text="fake wifi", command=fakewifi)
    tombol2 = tkinter.Button(awal, text="exit", command=awal.destroy)

    Label.pack()
    moni.pack()
    tombol.pack()
    airep.pack()
    ai.pack()
    fake.pack()
    tombol2.pack()
    awal.mainloop() 

aw = Tk()
menu = Menu(aw)

aw.config(menu=menu)

bg = PhotoImage(file="//opt/wificrack-gui/background/bg.png")
label = Label(aw, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)

aw.title("wificrack")
aw.geometry("500x500")
filemenu = Menu(menu)
menu.add_cascade(label="info", menu=filemenu)
filemenu.add_command(label="about", command=tentang)
Label = tkinter.Label(aw, text="thanks for use this script")
moni = tkinter.Button(aw, text="wifi", command=wifi)
tombol = tkinter.Button(aw, text="phising", command=phising)
tombol2 = tkinter.Button(aw, text="exit", command=aw.destroy)
Label.pack()
moni.pack()
tombol.pack()
tombol2.pack()
aw.mainloop()
