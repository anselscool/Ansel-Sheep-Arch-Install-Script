import os
import subprocess
from time import sleep

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

print(asais + "\nansel + whyisthesheep arch install script\n")
packages = []

def checks():
    hostname = subprocess.run(["cat", "/etc/hostname"], capture_output=True, text=True).stdout.strip()
    if hostname == "archiso":
        print("[MAIN]: Arch Linux installation environment detected")
    else:
        print(f"[FATAL]: Arch Linux seems to already be installed to your disk (hostname: {hostname})")
        exit() # COMMENT THIS LINE IF THE HOSTNAME IS NOT "archiso"

    ping_result = subprocess.run(["curl", "https://archlinux.org"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ping_result.returncode != 6:
        print("[MAIN]: Internet active")
    else:
        print("[FATAL]: Internet unreachable. Try using iwctl.")
        exit()

    return

def prestrapsetup():
    if confirm("[SETUP]: Do you wish to change the keyboard layout [Y/n] "):
        newkeymap = input("[SETUP]: Set keymap (eg uk, us, fr, it) ")
        os.system(f"loadkeys {newkeymap}")
    
    print("[SETUP]: Please format Boot (~100mb) {OPTIONAL Swap (~Your ram)} Root (the remaining storage). Please take note of the /dev/names.")
    for i in range(0, 5):
        sleep(1.5)
        print(f"[SETUP]: Opening cfdisk {i+1}")
    os.system("cfdisk")
    os.system("clear")

    os.system("lsblk")
    print("\n")
    fstype = input("[SETUP]: Choose filetype (ext4 OR btrfs): ")
    rootlocation = input("[SETUP]: Root location: /dev/")
    print(f"[SETUP]: Using root location /dev/{rootlocation}")
    os.system(f"mkfs.{fstype} /dev/{rootlocation}")
    os.system("clear")

    os.system("lsblk")
    print("\n")
    bootlocation = input("[SETUP]: Boot location: /dev/")
    print(f"[SETUP]: Using boot location /dev/{bootlocation}")
    os.system(f"mkfs.fat -F 32 /dev/{bootlocation}")
    os.system("clear")

    os.system("lsblk")
    print("\n")
    if confirm("[SETUP]: Did you create a swap partition [Y/n] "):
        swaplocation = input("[SETUP]: Swap drive: /dev/")
        print(f"[SETUP]: Using swap location /dev/{swaplocation}")
        os.system(f"mkswap /dev/{swaplocation}")
    os.system("clear")

    os.system(f"mount /dev/{rootlocation} /mnt")
    os.system("mkdir -p /mnt/boot/efi")
    os.system("mkdir /mnt/tmp")
    os.system(f"mount /dev/{bootlocation} /mnt/boot/efi")
    os.system(f"swapon /dev/{swaplocation}")

    global kernel
    global editor

    kernel = input("[INSTALL]: Chose a kernel (examples: linux, linux-zen, linux-lts): ")
    shell = input("[INSTALL]: Chose a shell (examples: bash, fish, zsh): ")
    editor = input("[INSTALL]: Chose an editor (examples: vim, nano, neovim, micro): ")
    ucode = input("[INSTALL]: State your processor (amd/intel): ")
    ucode = ucode.replace(ucode, f"{ucode}-ucode")
    
    packages.append(shell)
    packages.append(ucode)

def pacstrap():
    print("[INSTALL]: Running pacstrap")
    os.system(f"pacstrap -K /mnt base linux-firmware base-devel grub networkmanager {kernel} {editor}")
    os.system("clear")
    print(asais + "\nansel + whyisthesheep arch install script\n")

def poststrapsetup():
    print("[POST-INSTALL]: Generating fstab")
    os.system("genfstab /mnt > /mnt/etc/fstab")
    timezone = input("[POST-INSTALL]: Set time zone format Region/City (e.g Europe/London): ")
    os.system(f"arch-chroot /mnt curl https://raw.githubusercontent.com/anselscool/asais/main/script/chrootscript.py > /tmp/chrootscript.py && python /tmp/chrootscript.py {packages[0]} {packages[1]} {timezone}")
    os.system("clear")
    print(asais + "\nansel + whyisthesheep arch install script\n")

def run():
    checks()
    prestrapsetup()
    pacstrap()
    poststrapsetup()

run()