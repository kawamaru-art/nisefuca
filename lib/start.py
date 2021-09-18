import os

def wow():
    os.system("sudo airmon-ng")
    inter = input("interfaces:")
    sta = input("start/stop?: ")
    os.system("sudo airmon-ng " + sta + " " + inter)
    print ("close The windows")

wow()
