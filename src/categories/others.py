from src.categories.core.others.wiki import wiki_main
from colorama import init
from termcolor import colored

init()

def choose_others():
    while True:
        print(colored("Choose a Others:", 'yellow', attrs=['bold']))
        print(colored("1. Wikipedia (en.wikipedia.com)", 'green'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Wikipedia!", 'green'))
            wiki_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def others_main():
    choose_others()