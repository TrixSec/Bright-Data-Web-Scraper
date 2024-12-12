from src.categories.core.marketplacesrc.apple_scraper import apple_main
from src.categories.core.marketplacesrc.olx_scraper import olx_main
from src.categories.core.marketplacesrc.google_play_scraper import gplay_main
from src.categories.core.marketplacesrc.yapo_chile_scraper import yapo_main
from colorama import init
from termcolor import colored

init()

def choose_marketplace():
    while True:
        print(colored("Choose a Marketplace:", 'yellow', attrs=['bold']))
        print(colored("1. Apple (apps.apple.com)", 'green'))
        print(colored("2. OLX Brazil", 'blue'))
        print(colored("3. Google Play Store (play.google.com)", 'cyan'))
        print(colored("4. Yapo Chile (new.yapo.cl)", 'magenta'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Apple!", 'green'))
            apple_main()
            break
        elif choice == '2':
            print(colored("You selected OLX Brazil!", 'blue'))
            olx_main()
            break
        elif choice == '3':
            print(colored("You selected Google Play Store!", 'cyan'))
            gplay_main()
            break
        elif choice == '4':
            print(colored("You selected Yapo Chile!", 'magenta'))
            yapo_main()
            break
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def marketplace_main():
    choose_marketplace()
