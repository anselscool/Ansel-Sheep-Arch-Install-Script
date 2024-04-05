import os, subprocess

asais = """
    ___   _____ ___    _________
   /   | / ___//   |  /  _/ ___/
  / /| | \__ \/ /| |  / / \__ \ 
 / ___ |___/ / ___ |_/ / ___/ / 
/_/  |_/____/_/  |_/___//____/  
"""

print(asais)
print("ansel + whyisthesheep arch install script\n")

hostname = subprocess.run(["cat", "/etc/hostname"], capture_output=True, text=True).stdout.strip()
if hostname == "archiso":
    print("[MAIN]: Arch Linux installation environment detected")
else:
    print("[FATAL]: Arch Linux seems to already be installed to your disk")
    exit() # COMMENT THIS LINE IF THE HOSTNAME IS NOT "archiso"

ping_result = subprocess.run(["curl", "https://archlinux.org"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if ping_result.returncode != 6:
    print("[MAIN]: Internet active")
else:
    print("[FATAL]: Internet unreachable. Try using iwctl.")
    exit()

changekmp = input("[SETUP]: Do you wish to change the keyboard layout [Y/n] ")
changekmp = changekmp.upper().replace("Y", "")
if changekmp == "":
    newkeymap = input("[SETUP]: Set keymap (eg uk, us, it) ")
    os.system(f"loadkeys {newkeymap}")

