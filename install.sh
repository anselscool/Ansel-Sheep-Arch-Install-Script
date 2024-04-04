#!/bin/sh
set -e

cat << "EOF"
    ___   _____ ___    _________
   /   | / ___//   |  /  _/ ___/
  / /| | \__ \/ /| |  / / \__ \ 
 / ___ |___/ / ___ |_/ / ___/ / 
/_/  |_/____/_/  |_/___//____/  
                                                                    
EOF

echo "ansel + whyisthesheep arch install script"
if [ -f "/etc/os-release" ]; then
    echo "[FATAL]: Arch seems already to be installed"
    #exit 1
fi

echo "[MAIN]: Testing internet"
ping -c 2 archlinux.org > /dev/null
if [ $? -eq 0 ]; then
    echo "[MAIN]: Internet active"
else
    echo "[FATAL]: Internet unreachable. Try using iwctl."
    exit 1 # Idk how you got this error if you curled 1the script
fi

read -p "[SETUP]: Do you wish to change the keyboard layout [Y/n]" input
input_uppercase=$(echo "$input" | tr "[:lower:]" "[:upper:]")
if [[ "$input_uppercase" == "Y" || -z "$input" ]]; then
    read -p "[SETUP]: Set keymap (eg uk, us, it)" newkeymap
    loadkeys newkeymap
fi