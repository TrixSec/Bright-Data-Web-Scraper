import os
from src.categories.marketplace import marketplace_main
from src.categories.btwob import btwob_main
from src.categories.web import web_main
from src.categories.ecom import ecom_main
from src.categories.financial import financial_main
from src.categories.news import news_main
from src.categories.estate import estate_main
from src.categories.social import social_main
from src.categories.travel import travel_main
from src.categories.others import others_main

from colorama import init
from termcolor import colored

try:
    from config.config import API_KEY
except ImportError:
    API_KEY = ""

init()

def get_api_key():
    """
    Retrieve the Bright Data API key from the config module or prompt the user if it's missing.
    """
    if API_KEY:
        return API_KEY
    else:
        api_key = input(colored("Enter your Bright Data API key: ", "yellow")).strip()
        save_api_key(api_key)
        return api_key

def save_api_key(api_key):
    """
    Save the provided API key to the `config/config.py` file.
    """
    config_path = os.path.join("config", "config.py")
    with open(config_path, "w") as config_file:
        config_file.write(f'API_KEY = "{api_key}"\n')
    print(colored("API key saved successfully!", "green", attrs=["bold"]))

def main():
    """
    Main function to handle category selection and dispatch to subcategories.
    """
    get_api_key()

    print(colored("\nSelect a category to scrape:", "cyan", attrs=["bold"]))
    print(colored("1.", "green"), "Marketplace(4)")
    print(colored("2.", "green"), "B2B(1)")
    print(colored("3.", "green"), "Web(1)")
    print(colored("4.", "green"), "E-commerce(2)")
    print(colored("5.", "green"), "Financial(1)")
    print(colored("6.", "green"), "News(2)")
    print(colored("7.", "green"), "Real Estate(1)")
    print(colored("8.", "green"), "Social Media(2)")
    print(colored("9.", "green"), "Travel(1)")
    print(colored("10.", "green"), "Other(1)")
    print(colored("99.", "green"), "Exit")


    try:
        choice = int(input(colored("\nEnter your choice (1-10): ", "yellow")))
        
        if choice == 1:
            marketplace_main()
        elif choice == 2:
            btwob_main()
        elif choice == 3:
            web_main()
        elif choice == 4:
            ecom_main()
        elif choice == 5:
            financial_main()
        elif choice == 6:
            news_main()
        elif choice == 7:
            estate_main()
        elif choice == 8:
            social_main()
        elif choice == 9:
            travel_main()
        elif choice == 10:
            others_main()
        elif choice == 99:
            exit(1)
        else:
            print(colored("Category not yet implemented. Please try again later.", "red"))
    except ValueError:
        print(colored("Invalid input. Please enter a number between 1 and 10.", "red"))

if __name__ == "__main__":
    main()