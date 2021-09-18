import os
import sys
from time import sleep
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] wificrack installer has root for run it:)\n\033[1;m""")

def main():
   os.system("clear")
   print ("""\033[0;36m
   ====================================================================================================================================================
   |        .__  _____.__                            __                          .__          .__                 __         .__  .__                  |
   |__  _  _|__|/ ____\__| ________________    ____ |  | __           ____  __ __|__|         |__| ____   _______/  |______  |  | |  |   ___________   |
   |\ \/ \/ /  \   __\|  |/ ___\_  __ \__  \ _/ ___\|  |/ /  ______  / ___\|  |  \  |  ______ |  |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \_  __ \  |
   | \     /|  ||  |  |  \  \___|  | \// __ \\  \___|    <  /_____/  / /_/  >  |  /  | /_____/ |  |   |  \\___ \   |  |  / __ \|  |_|  |_\  ___/|  | \/  |
   |  \/\_/ |__||__|  |__|\___  >__|  (____  /\___  >__|_ \         \___  /|____/|__|         |__|___|  /____  > |__| (____  /____/____/\___  >__|     |
   |                          \/           \/     \/     \/        /_____/                            \/     \/            \/               \/         |
   ==================================================================================================================================================== \033[0;32m""")
   print ("type install or out")
   print ("[!]install")
   print ("[!]out")
   p = input(">>> ")
   if p == "install":
      install1 = os.system("""apt install python3 && apt install aircrack-ng && apt install python3-tornado && apt install python3-tk && apt install konsole && apt install xterm""")

      install2 = os.system("""mkdir -p /opt/wificrack-gui && cp Wificrack-guiroot.desktop /usr/share/applications && cp wificrack-gui.desktop /usr/share/applications && cp icon.png /opt/wificrack-gui && cp wificrack-gui.py /opt/wificrack-gui && cp -R background/ /opt/wificrack-gui && cp -R lib/ /opt/wificrack-gui && cp run.sh /usr/bin/wificrack-gui && chmod +x /usr/bin/wificrack-gui && echo "\nwificrackgui complete install execute: 'wificrack-gui'\n" """)
   elif p == "out":
      exit()
   else:
      print ("wrong command")
      sleep(3)
      main() 

main()

