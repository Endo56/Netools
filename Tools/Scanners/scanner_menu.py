from Tools.Scanners import network_scan
from Tools.Scanners import port_scan
from colors import *
import Netools


def show_menu():
    menu = f"""
{GREEN}{BOLD}Available Tools:{RESET}
================
  {GREEN}{BOLD}1{RESET}) Network Scanner - Detect live hosts on the network
  {GREEN}{BOLD}2{RESET}) Port Scanner    - Detect open ports
    
Type {GREEN}{BOLD}'Back'{RESET} or {GREEN}{BOLD}'Ctrl + C'{RESET} to the main menu
    """
    while True:
        Netools.show_banner()
        print(menu)
        try:
            choice = input("Netools/Scan > ").lower()
        except KeyboardInterrupt:
            return

        if choice == "1":
            network_scan.main()
        elif choice == "2":
            port_scan.main()
        elif choice.startswith("bac") or choice.startswith("exi"):
            return
        else:
            continue