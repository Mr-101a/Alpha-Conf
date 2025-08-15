#!/bin/bash

echo "01 Starting installation for convertـconf ... 01"
echo "***************** created by Alpha Team *****************"
echo "               _
     /\       | |       ____     _    _      /\     
    /**\      | |      |  __ \  | |  | |    /**\   
   /*/\*\     | |      | |__) | | |__| |   /*/\*\   
  /*____*\    | |____  |  ___/  |  __  |  /*____*\   
 /_/    \_\   |_|____| |_|      |_|  |_| /_/    \_\	
 
       A       L        P       H       A
"


sudo apt update


if ! command -v python3 &> /dev/null
then
    echo "01 Python3 not found. Installing... 01"
    echo "***************** created by Alpha Team *****************"
    sudo apt install -y python3
    echo "***************** created by Alpha Team *****************"
fi

if ! command -v pip3 &> /dev/null
then
    echo "01 pip3 not found. Installing... 01"
    echo "***************** created by Alpha Team *****************"
    sudo apt install -y python3-pip
    echo "***************** created by Alpha Team *****************"
fi


echo "01 Installing Tkinter... 01"
echo "***************** created by Alpha Team *****************"
sudo apt install -y python3-tk
echo "***************** created by Alpha Team *****************"


echo "01 Installing zenity... 01"
echo "***************** created by Alpha Team *****************"
sudo apt install -y zenity
echo "***************** created by Alpha Team *****************"


#echo "***************** created by Alpha Team *****************"
chmod +x ./install_conf.sh 
echo "✅ Installation completed. Now you need to import ( ./install_code.sh ) into the terminal."
echo "***************** created by Alpha Team *****************"

