echo "1. install with application"
echo "2. install no application"
read -p "> " pil
if [ $pil = "1" ]
then
    sudo apt install python3
    sudo python3 install-for-aplication.py
elif [ $pil = "2" ]
then
    sudo apt install python3
    sudo python3 install.py

fi
