import pyautogui
import threading
import time
import keyboard
from colorama import init, Fore, Style

init(autoreset=True)
running = False

screen_width, screen_height = pyautogui.size()

def get_position_input(prompt):
    while True:
        try:
            x_input = input(Fore.CYAN + f"{prompt} - X: " + Style.RESET_ALL)
            y_input = input(Fore.CYAN + f"{prompt} - Y: " + Style.RESET_ALL)

            x = int(x_input)
            y = int(y_input)

            x = max(1, min(x, screen_width - 2))
            y = max(1, min(y, screen_height - 2))

            return (x, y)
        except ValueError:
            print(Fore.RED + "Błąd: wpisz poprawną liczbę całkowitą!" + Style.RESET_ALL)

HEADER = f"""
{Fore.MAGENTA + Style.BRIGHT}
    ___   __  ____________     ________    ____________ __ __________ 
   /   | / / / /_  __/ __ \   / ____/ /   /  _/ ____/ //_// ____/ __ |
  / /| |/ / / / / / / / / /  / /   / /    / // /   / ,<  / __/ / /_/ /
 / ___ / /_/ / / / / /_/ /  / /___/ /____/ // /___/ /| |/ /___/ _, _/ 
/_/  |_\____/ /_/  \____/   \____/_____/___/\____/_/ |_/_____/_/ |_|  
{Style.RESET_ALL}
"""

print(HEADER)
print(Fore.YELLOW + Style.BRIGHT + "Ustaw pozycje kliknięć:" + Style.RESET_ALL)
pos1 = get_position_input("Pierwsze kliknięcie")
pos2 = get_position_input("Drugie kliknięcie")
print()

creator = Fore.GREEN + "Keno" + Style.RESET_ALL
print(Fore.YELLOW + "Naciśnij F5, żeby włączyć/wyłączyć autoclicker. ESC = wyjście." + Style.RESET_ALL)
print(Fore.YELLOW + f"Skrypt stworzony przez: {creator}" + Style.RESET_ALL)

def clicker():
    global running
    while True:
        if running:
            pyautogui.click(pos1)
            pyautogui.click(pos2)
        time.sleep(0.1)

def toggle():
    global running
    running = not running
    ON = Fore.GREEN + Style.BRIGHT + "ON" + Style.RESET_ALL
    OFF = Fore.RED + Style.BRIGHT + "OFF" + Style.RESET_ALL
    status = ON if running else OFF
    print(Fore.CYAN + "[STATUS]" + Style.RESET_ALL, "Autoclicker:", status)

keyboard.add_hotkey("F5", toggle)

t = threading.Thread(target=clicker)
t.daemon = True
t.start()

keyboard.wait("esc")
print(Fore.RED + Style.BRIGHT + "Wyjście z programu..." + Style.RESET_ALL)
