import os

def scan2ifi():
    os.system("clear")
    os.system("sudo airmon-ng")
    inter = input("interfaces: ")
    os.system("sudo airodump-ng " + inter)

scan2ifi()
