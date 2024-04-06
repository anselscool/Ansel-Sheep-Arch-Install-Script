import sys
import os

def confirm(message):
    checkconfirm = input(message)
    checkconfirm = checkconfirm.upper().replace("Y", "")
    if checkconfirm == "":
        return True
    else:
        return False

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
input("[POST-INSTALL]: Press ENTER to continue: ")
os.system("nano /etc/locale.gen")
os.system("locale-gen")
os.system("echo 'LANG=' > /etc/locale.conf")
os.system("clear")
print("[POST-INSTALL]: Please update the LANG variable (e.g LANG=en_GB.UTF-8)")
input("[POST-INSTALL]: Press ENTER to continue: ")
os.system("nano /etc/locale.conf")
os.system("clear")
print("[POST-INSTALL]: Please update the KEYMAP variable (e.g KEYMAP=uk or KEYMAP=us)")
input("[POST-INSTALL]: Press ENTER to continue: ")
os.system("nano /etc/vconsole.conf")
os.system("clear")
hostname = ("[USER]: Please choose a device hostname: ")
os.system(f"echo '{hostname}' > /etc/hostname")
os.system("clear")
print("[USER]: Please select a new root password: ")
os.system("passwd")
username = input("[USER]: Please input a username: ")
os.system(f"useradd -m -G wheel -s /bin/{shell} {username}")
print(f"[USER]: Please input a password for {username}")
os.system(f"passwd {hostname}")
print("[USER]: Please uncomment %wheel ALL=(ALL) ALL")
input("[USER]: Press ENTER to continue: ")
os.system("EDITOR=nano visudo")
if confirm("[USER]: Install and configure doas [Y/n]"):
    os.system("pacman -Syuu")
    os.system("pacman -S doas")
    os.system(f"echo 'permit {username}' > /etc/doas.conf")
print("[USER]: Enabling NetworkManager")
os.system(f"su {username} && systemctl enable NetworkManager")
os.system("clear")
os.system("lsblk")
disk = input("[SYSTEM]: Which disk (not partition) have you fortmatted and installed arch to (e.g /dev/sda NOT /dev/sda1): /dev/")
print("[SYSTEM]: Installing grub")
os.system(f"grub-install /dev/{disk}")
os.system("grub-mkconfig -o /boot/efi/grub/grub.cfg")