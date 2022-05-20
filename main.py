print("""
# @Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
# @github https://github.com/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.xyz
""")

# FUNCTIONS
def cTerminal():
    """Check OS.system and clear terminal"""

    if os.name == "nt":  # posx, java, nt
        os.system("cls")
    else:
        os.system("clear")

# libraries
import os
import time

import pyfiglet

time.sleep(1.5)
cTerminal()

# banner
print(pyfiglet.figlet_format("TIC TAC TOE" ))

# application

