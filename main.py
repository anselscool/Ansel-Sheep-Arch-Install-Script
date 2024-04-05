import os
import subprocess
from time import sleep

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
    changekmp = input("[SETUP]: Do you wish to change the keyboard layout [Y/n] ")
    changekmp = changekmp.upper().replace("Y", "")
    if changekmp == "":
        newkeymap = input("[SETUP]: Set keymap (eg uk, us, fr, it) ")
        os.system(f"loadkeys {newkeymap}")
    
    print("[SETUP]: Please format Boot (~100mb) Swap (~Your ram) Root (the remaining storage)")
    for i in range(0, 2):
        sleep(1)
        print(f"[SETUP]: Opening cfdisk {i}")
    os.system("cfdisk")

def pacstrap(packages):
    pass

def poststrapsetup():
    pass

def ricing():
    pass

def run():
    checks()
    prestrapsetup()
    pacstrap(packages)
    poststrapsetup()
    ricing()
