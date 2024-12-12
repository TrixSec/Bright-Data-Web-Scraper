from src.categories.core.btwob.linkedin_scraper import linkedin_main
from colorama import init
from termcolor import colored

init()

def choose_btwob():
    while True:
        print(colored("Choose a B2B:", 'yellow', attrs=['bold']))
        print(colored("1. Linkedin (linkedin.com)", 'green'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Linkedin!", 'green'))
            linkedin_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def btwob_main():
    choose_btwob()