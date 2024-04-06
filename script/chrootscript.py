import sys
import os
from time import sleep

asais = """
    ___   _____ ___    _________
   /   | / ___//   |  /  _/ ___/
  / /| | \__ \/ /| |  / / \__ \ 
 / ___ |___/ / ___ |_/ / ___/ / 
/_/  |_/____/_/  |_/___//____/  
"""

shell = sys.argv[1]
ucode = sys.argv[2]
timezone = sys.argv[3]

os.system("pacman -Sy")
os.system(f"pacman -S {shell} {ucode} neofetch xdg-user-dirs pipewire base-devel")
os.system(f"ln -sf /usr/share/zoneinfo/{timezone} /etc/localtime")
os.system("hwclock --systohc")

print(asais + "\nansel + whyisthesheep arch install script\n")
print("[POST-INSTALL]: Please uncomment your locale of choice (e.g en_GB.UTF-8 UTF-8)")
sleep(5)
os.system("nano /etc/locale.gen")
os.system("locale-gen")
os.system("echo 'LANG=' > /etc/locale.conf")
print("[POST-INSTALL]: Please update the LANG variable (e.g LANG=en_GB.UTF-8)")
sleep(5)
os.system("nano /etc/locale.conf")
print("[POST-INSTALL]: Please update the KEYMAP variable (e.g KEYMAP=uk or KEYMAP=us)")
sleep(5)
os.system("nano /etc/vconsole.conf")
os.system("clear")
hostname = ("[POST-INSTALL]: Please choose a device hostname: ")
os.system(f"echo '{hostname}' > /etc/hostname")
print("[POST-INSTALL]: Please select a new root password: ")
os.system("passwd")
