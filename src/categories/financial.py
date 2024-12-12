from src.categories.core.financial.yahoo_scraper import yahoo_main
from colorama import init
from termcolor import colored

init()

def choose_financial():
    while True:
        print(colored("Choose a Financial:", 'yellow', attrs=['bold']))
        print(colored("1. Yahoo (yahoo.com)", 'green'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Yahoo!", 'green'))
            yahoo_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def financial_main():
    choose_financial()