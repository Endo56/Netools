from Tools.Scanners import scanner_menu
from Update import update
from colors import *
import sys
import os


if os.geteuid() != 0:
    print(f"{RED}{BOLD}[ERROR]{RESET} Haval framework must be run as Root.")
    sys.exit(1)

def show_menu():
    menu = f"""
{GREEN}{BOLD}Available Commands:{RESET}
===================
  {GREEN}{BOLD}scan{RESET}   - Starting the scanner
  {GREEN}{BOLD}sniff{RESET}  - Starting the sniffer
  {GREEN}{BOLD}help{RESET}   - Display information about the framework
  {GREEN}{BOLD}update{RESET} - Updates this framework via GitHub
  {GREEN}{BOLD}exit{RESET}   - Exiting the program"""
    print(menu)

def show_help_msg():
    msg = f"""
Commands:
=========
  {GREEN}{BOLD}scan{RESET}
  {BOLD}Description:{RESET} Scans the specified network for alive hosts
        {BOLD}Usage:{RESET} Type {BLUE}{BOLD}'scan'{RESET} to perform a port scan or a network scan

  {GREEN}{BOLD}sniff{RESET}
  {BOLD}Description:{RESET} Captures network packets in real-time
        {BOLD}Usage:{RESET} Type {BLUE}{BOLD}'sniff'{RESET} to capture network packets

  {GREEN}{BOLD}update{RESET}
  {BOLD}Description:{RESET} Updating the framework via GitHub
        {BOLD}Usage:{RESET} Enter {BLUE}{BOLD}'update'{RESET} to update the framework
    """
    print(msg)

def show_banner():
    os.system('clear')
    banner = rf"""{GREEN}          _______           _______  _       
|\     /|(  ___  )|\     /|(  ___  )( \      
| )   ( || (   ) || )   ( || (   ) || (      
| (___) || (___) || |   | || (___) || |      
|  ___  ||  ___  |( (   ) )|  ___  || |      
| (   ) || (   ) | \ \_/ / | (   ) || |      
| )   ( || )   ( |  \   /  | )   ( || (____/\
|/     \||/     \|   \_/   |/     \|(_______/{RESET}
 
- Version 1.0 -"""
    print(banner)

def main():
    while True:
        show_banner()
        show_menu()
        try: 
            command = input("\nHaval > ").lower()
        except KeyboardInterrupt:
            print()
            sys.exit(1)

        if command.startswith("sc"):
            show_banner()
            scanner_menu.show_menu()
        elif command.startswith("sn"):
            pass
        elif command.startswith("h"):
            show_help_msg()
            input(f"Press {GREEN}{BOLD}[ENTER]{RESET} to continue")
        elif command.startswith("up"):
            update.main()
        elif command.startswith("ex"):
            print()
            sys.exit(1)
        else:
            main()


if __name__ == "__main__":
    main()

