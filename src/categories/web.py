from src.categories.core.web.martindale import martindale_main
from colorama import init
from termcolor import colored

init()

def choose_web():
    while True:
        print(colored("Choose a Web:", 'yellow', attrs=['bold']))
        print(colored("1. Martindale (martindale.com)", 'green'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Martindale!", 'green'))
            martindale_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def web_main():
    choose_web()