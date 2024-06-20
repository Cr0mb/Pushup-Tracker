import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

pushups_completed = 0
sets_completed = 0

filename = 'pushups.txt'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def write_date_if_needed():
    with open(filename, 'a') as file:
        current_date = datetime.now().strftime("%Y-%m-%d")
        file.write(f"Date: {current_date}\n")

def write_pushup_data(pushups_completed, sets_completed):
    with open(filename, 'a') as file:
        current_time = datetime.now().strftime("%H:%M:%S")
        file.write(f"Time: {current_time} | Sets Completed: {sets_completed} | Pushups Completed: {pushups_completed}\n")

def write_total_pushups(total_pushups):
    with open(filename, 'a') as file:
        file.write(f"Total Pushups Completed Today: {total_pushups}\n\n")

if __name__ == "__main__":
    write_date_if_needed()
    print(f"{Fore.YELLOW}Press Enter to add 15 pushups. Press 'q' to quit.{Style.RESET_ALL}")
    while True:
        user_input = input()
        if user_input.lower() == 'q':
            break
        elif user_input == '':
            pushups_completed += 15
            sets_completed += 1
            clear_console()  
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"{Fore.GREEN}Time: {current_time} | Sets Completed: {sets_completed} | Pushups Completed: {pushups_completed}{Style.RESET_ALL}", end='\r')
            write_pushup_data(pushups_completed, sets_completed)
        else:
            print(f"{Fore.RED}Invalid input. Press Enter to add 15 pushups. Press 'q' to quit.{Style.RESET_ALL}")

write_total_pushups(pushups_completed)
print(f"\n{Fore.CYAN}Total Sets Completed: {sets_completed} | Total Pushups Completed: {pushups_completed}{Style.RESET_ALL}")
