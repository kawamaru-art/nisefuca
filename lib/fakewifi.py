import os

def fakewifi():
    os.system("sudo airmon-ng")
    inter = input("interfaces: ")
    os.system("clear")
    print("exemple:fuck_hacker")
    a = input("name fake wifi: ")
    b = input("channel what you want: ")
    c = input("beacon 0/1: ")
    os.system("konsole --hold -geometry 900x500 -e sudo airodump-ng " + inter + " &")
    print("fake wifi is done")
    os.system("sudo airbase-ng -c " + b + " -e " + a + " -s -W " + c + " " + inter)

fakewifi()