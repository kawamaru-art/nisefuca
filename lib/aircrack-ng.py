import os

def aircrack_ng():
    wr = input("input the wordlist: ")
    capp = input("input file format .cap: ")
    os.system("aircrack-ng " + capp + " -w " + wr)

aircrack_ng()
