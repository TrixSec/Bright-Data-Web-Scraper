from src.categories.core.ecomm.google_scraper import google_main
from src.categories.core.ecomm.amazon_scraper import amazon_main
from colorama import init
from termcolor import colored

init()

def choose_ecom():
    while True:
        print(colored("Choose a E-Commerce:", 'yellow', attrs=['bold']))
        print(colored("1. Google (google.com)", 'green'))
        print(colored("2. Amazon (amazon.com)", 'green'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Google!", 'green'))
            google_main()
        elif choice == '2':
            print(colored("You selected Google!", 'green'))
            amazon_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def ecom_main():
    choose_ecom()