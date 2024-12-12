from src.categories.core.social.insta_scraper import insta_main
from src.categories.core.social.quora_scraper import quora_main
from colorama import init
from termcolor import colored

init()

def choose_social():
    while True:
        print(colored("Choose a Social Media:", 'yellow', attrs=['bold']))
        print(colored("1. Instagram (instagram.com)", 'green'))
        print(colored("2. Quora (quora.com)", 'green'))


        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Instagram!", 'green'))
            insta_main()
        if choice == '2':
            print(colored("You selected Quora!", 'green'))
            quora_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def social_main():
    choose_social()