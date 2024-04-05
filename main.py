import os, subprocess

hostname = os.system("cat /etc/hostname")
asais = """
    ___   _____ ___    _________
   /   | / ___//   |  /  _/ ___/
  / /| | \__ \/ /| |  / / \__ \ 
 / ___ |___/ / ___ |_/ / ___/ / 
/_/  |_/____/_/  |_/___//____/  
"""

print(asais)
print("ansel + whyisthesheep arch install script")

if hostname == "archiso":
    print("[MAIN]: Arch Linux installation environment detected")
else:
    print("[FATAL]: Arch seems already to be installed (development mode - skipping)")
    #exit()

ping_result = subprocess.run(["ping", "-c", "2", "archlinux.org"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if ping_result.returncode != 0:
    print("[MAIN]: Internet active")
else:
    print("[FATAL]: Internet unreachable. Try using iwctl.")
    exit()

changekmp = print("[SETUP]: Do you wish to change the keyboard layout [Y/n] ")
changekmp = changekmp.upper().replace("Y", "")
if changekmp == "":
    newkeymap = input("[SETUP]: Set keymap (eg uk, us, it) ")
    os.system(f"loadkeys $(newkeymap)")