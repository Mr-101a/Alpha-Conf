#!/bin/bash

echo "🔧  در حال انجام است Convertـconf نصب"
echo " "
echo " "
echo "               _
     /\       | |       ____     _    _      /\     
    /**\      | |      |  __ \  | |  | |    /**\   
   /*/\*\     | |      | |__) | | |__| |   /*/\*\   
  /*____*\    | |____  |  ___/  |  __  |  /*____*\   
 /_/    \_\   |_|____| |_|      |_|  |_| /_/    \_\	
 
       A       L        P       H       A
"


possible_names=(
    "./convertـconf"
    "./Convertـconf"
    "./convertـconf"
    "./convertـconf.run"
    "./convertـconf.bin"
)

found_executable=""

 
for name in "${possible_names[@]}"; do
    if [ -f "$name" ]; then
        found_executable="$name"
        echo "✔ File founded : $found_executable"
        break
    fi
done


if [ -z "$found_executable" ]; then
    echo "❌ No executable files with known names were found **"
    exit 1
fi


sudo cp "$found_executable" /usr/local/bin/convertـconf
sudo chmod +x /usr/local/bin/convertـconf



echo "ــــ--ــــ✅ Installation is complete ــــ--ــــ"
echo " "
echo "ــ--ــ created by Alpha Team || channel : t.me/Alpha_Development_Team  ــ--ــ"
echo " "
echo "** You can run the program by entering ‍‍‍‍‍‍( convertـconf ) command **"


