from src.categories.core.news.google_news import google_news_main
from src.categories.core.news.bbc_news import bbc_main

from colorama import init
from termcolor import colored

init()

def choose_news():
    while True:
        print(colored("Choose a News Site:", 'yellow', attrs=['bold']))
        print(colored("1. Google News (news.google.com)", 'green'))
        print(colored("2. BBC News (bbc.com)", 'green'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Google News!", 'green'))
            google_news_main()
        if choice == '2':
            print(colored("You selected BBC News!", 'green'))
            bbc_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def news_main():
    choose_news()