from src.categories.core.travel.booking import booking_main
from colorama import init
from termcolor import colored

init()

def choose_travel():
    while True:
        print(colored("Choose a Web:", 'yellow', attrs=['bold']))
        print(colored("1. Booking (booking.com)", 'green'))

        choice = input(colored("Enter the number of your choice: ", 'red', attrs=['bold']))
        
        if choice == '1':
            print(colored("You selected Booking!", 'green'))
            booking_main()
        else:
            print(colored("Invalid choice, please choose a valid option.", 'red', attrs=['bold']))

def travel_main():
    choose_travel()