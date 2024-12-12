from src.categories.core.realestate.toctoc import toctoc_main
from colorama import init
from termcolor import colored

init()

def choose_estate():
    while True:
        print(colored("Choose a Estate Site:", 'yellow', attrs=['bold']))
        print(colored("1. Toctoc (toctoc.com)", 'green'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected TocToc!", 'green'))
            toctoc_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def estate_main():
    choose_estate()