import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from colors import *
import time


def main():
    os.system('clear')
    print(r"""
 ═════════════════════════════════════════════════════════════         
                    Netools v1.0 installer     
 ═════════════════════════════════════════════════════════════   
                    [Updated]: 2025|03|27  
 ═════════════════════════════════════════════════════════════
""")
    try:
        choice = str(input(f"{YELLOW}{BOLD}[?]{RESET} Would you like to proceed with the installation? Y/N: ")).lower()

        if choice.startswith("y"):
            print(f"\n{BLUE}{BOLD}[*]{RESET} Installing required packages...\n")
            time.sleep(0.5)
            try:
                os.system("sudo apt update")
                os.system("sudo apt install nmap")
                result = os.system("pip3 install -r requirements.txt --break-system-packages")
            except KeyboardInterrupt:
                print(f"{RED}{BOLD}[-]{RESET} Installation aborted.")
                sys.exit(1)
            if result == 0:
                print(f"\n{GREEN}{BOLD}[+]{RESET} Successfully Installed!\n")
            else:
                print(f"\n{RED}{BOLD}[ERROR]{RESET} Installation failed. Please check the error messages.\n{RESET}")
                sys.exit(1)
        elif choice.startswith("n"):
            print(f"\n{RED}{BOLD}[-]{RESET} Installation aborted.\n")
            sys.exit(1)
        else:
            input(f"{RED}{BOLD}[-]{RESET} Wrong choice! Press [ENTER] to continue.")
            main()
    except KeyboardInterrupt:
        print(f"\n{RED}{BOLD}[-]{RESET} Installation aborted.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()