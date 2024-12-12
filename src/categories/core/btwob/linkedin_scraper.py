import requests
from colorama import init
from termcolor import colored
from config.config import API_KEY  
from config.endpoints import linkedin_people_endpoint, linkedin_company_endpoint
init()


def print_bold_colored(message, color="green"):
    print(colored(message, color, attrs=["bold"]))

def get_urls_from_user():
    """Prompts the user to input LinkedIn company URLs to scrape."""
    urls = []
    print_bold_colored("\nEnter LinkedIn company URLs to scrape (enter 'done' to finish):", "cyan")
    while True:
        url = input(colored("Enter URL: ", "yellow"))
        if url.lower() == 'done':
            break
        elif url:
            urls.append(url)
        else:
            print_bold_colored("Please enter a valid URL or 'done' to finish.", "red")
    return urls

def get_linkedin_profiles_from_user():
    """Prompts the user to input LinkedIn people's first and last names."""
    people = []
    print_bold_colored("\nEnter LinkedIn people's names (enter 'done' to finish):", "cyan")
    while True:
        first_name = input(colored("Enter First Name: ", "yellow"))
        if first_name.lower() == 'done':
            break
        last_name = input(colored("Enter Last Name: ", "yellow"))
        if last_name.lower() == 'done':
            break
        elif first_name and last_name:
            people.append({"first_name": first_name, "last_name": last_name})
        else:
            print_bold_colored("Please enter both first and last names.", "red")
    return people

def scrape_linkedin_company_data(API_KEY, urls):
    """Scrapes LinkedIn company data using the Bright Data API."""
    print_bold_colored(f"\nScraping data for LinkedIn Companies...", "cyan")

    payload = [{"url": url} for url in urls]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    print_bold_colored(f"\nSending scraping request to LinkedIn company endpoint: {linkedin_company_endpoint}", "cyan")
    try:
        response = requests.post(linkedin_company_endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            print_bold_colored("Scraping completed successfully!", "green")
            scraped_data = response.json()
            process_data(scraped_data)
        else:
            print_bold_colored(f"Error: {response.status_code} - {response.text}", "red")
    except Exception as e:
        print_bold_colored(f"An error occurred: {e}", "red")

def scrape_linkedin_people_data(API_KEY, people):
    """Scrapes LinkedIn people's profiles using the Bright Data API."""
    print_bold_colored(f"\nScraping data for LinkedIn People...", "cyan")

    payload = [{"first_name": person["first_name"], "last_name": person["last_name"]} for person in people]

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    print_bold_colored(f"\nSending scraping request to LinkedIn people endpoint: {linkedin_people_endpoint}", "cyan")
    try:
        response = requests.post(linkedin_people_endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            print_bold_colored("Scraping completed successfully!", "green")
            data = response.json()
            process_scraped_data(data)
        else:
            print_bold_colored(f"Error: {response.status_code} - {response.text}", "red")
    except Exception as e:
        print_bold_colored(f"An error occurred: {e}", "red")

def process_data(scraped_data):
    for company in scraped_data:
        print(colored(f"Timestamp: {company['timestamp']}", 'yellow', attrs=['bold']))
        print(colored(f"ID: {company['id']}", 'green', attrs=['bold']))
        print(colored(f"Name: {company['name']}", 'cyan', attrs=['bold']))
        print(colored(f"Country: {company['country_code']}", 'blue', attrs=['bold']))
        
        # Locations
        print(colored("Locations:", 'magenta', attrs=['bold']))
        for location in company['locations']:
            print(colored(f"  - {location}", 'white'))

        # Social media info
        print(colored(f"Followers: {company['followers']}", 'red', attrs=['bold']))
        print(colored(f"Employees on LinkedIn: {company['employees_in_linkedin']}", 'red', attrs=['bold']))

        # Company details
        print(colored("About:", 'magenta', attrs=['bold']))
        print(colored(company['about'], 'white'))

        print(colored(f"Specialties: {company['specialties']}", 'green', attrs=['bold']))
        print(colored(f"Company Size: {company['company_size']}", 'yellow', attrs=['bold']))
        print(colored(f"Organization Type: {company['organization_type']}", 'blue', attrs=['bold']))
        print(colored(f"Industries: {company['industries']}", 'cyan', attrs=['bold']))
        print(colored(f"Website: {company['website']}", 'magenta', attrs=['bold']))
        print(colored(f"Crunchbase URL: {company['crunchbase_url']}", 'magenta', attrs=['bold']))
        print(colored(f"Founded: {company['founded']}", 'yellow', attrs=['bold']))
        print(colored(f"Company ID: {company['company_id']}", 'green', attrs=['bold']))
        
        # Employees Info
        print(colored("Employees:", 'magenta', attrs=['bold']))
        for employee in company['employees']:
            print(colored(f"  - {employee['title']} ({employee['link']})", 'white'))

        # Headquarters
        print(colored(f"Headquarters: {company['headquarters']}", 'cyan', attrs=['bold']))
        
        # Image and logo
        print(colored(f"Company Image: {company['image']}", 'green', attrs=['bold']))
        print(colored(f"Company Logo: {company['logo']}", 'blue', attrs=['bold']))
        
        # Similar companies
        print(colored("Similar Companies:", 'magenta', attrs=['bold']))
        for similar in company['similar']:
            print(colored(f"  - {similar['title']} ({similar['Links']})", 'yellow'))
        
        # Latest updates
        print(colored("Latest Updates:", 'magenta', attrs=['bold']))
        for update in company['updates']:
            print(colored(f"  - {update['title']} (Likes: {update['likes_count']}, Comments: {update.get('comments_count', 0)})", 'white'))
            print(colored(f"    {update['text']}", 'white'))
            if 'images' in update:
                for image in update['images']:
                    print(colored(f"    Image URL: {image}", 'white'))
            print()

def process_scraped_data(data):
    """Process and display the scraped LinkedIn profile data."""

    # Extracting basic information
    timestamp = data.get("timestamp", "N/A")
    linkedin_id = data.get("linkedin_id", "N/A")
    name = data.get("name", "N/A")
    country_code = data.get("country_code", "N/A")
    position = data.get("position", "N/A")
    city = data.get("city", "N/A")
    
    # Extracting current company information
    current_company = data.get("current_company", {})
    company_name = current_company.get("name", "N/A")
    company_link = current_company.get("link", "N/A")
    company_title = current_company.get("title", "N/A")
    
    # About section
    about = data.get("about", "N/A")
    
    # Experience
    experience = data.get("experience", [])
    
    # Display the processed data
    print(colored(f"\nTimestamp: {timestamp}", "cyan", attrs=["bold"]))
    print(colored(f"LinkedIn ID: {linkedin_id}", "cyan"))
    print(colored(f"Name: {name}", "yellow"))
    print(colored(f"Country: {country_code}", "green"))
    print(colored(f"Position: {position}", "magenta"))
    print(colored(f"City: {city}", "blue"))
    
    print(colored(f"\nCurrent Company: {company_name}", "cyan"))
    print(colored(f"Company Link: {company_link}", "cyan"))
    print(colored(f"Company Title: {company_title}", "cyan"))
    
    print(colored("\nAbout:", "cyan"))
    print(about)
    
    if experience:
        print(colored("\nExperience:", "cyan"))
        for exp in experience:
            company = exp.get("company", "N/A")
            duration = exp.get("duration", "N/A")
            location = exp.get("location", "N/A")
            positions = exp.get("positions", [])
            
            print(colored(f"\nCompany: {company}", "green"))
            print(colored(f"Duration: {duration}", "green"))
            print(colored(f"Location: {location}", "green"))
            
            for pos in positions:
                position_description = pos.get("description", "N/A")
                print(colored(f"Position Description: {position_description}", "yellow"))
    else:
        print(colored("\nNo experience data available.", "red"))
    
    print(colored("\nData processed successfully!", "green"))
    


def linkedin_main():
    
    print_bold_colored("\nSelect LinkedIn Scraping Type:", "cyan")
    print_bold_colored("1.", "green"), print("Company Information")
    print_bold_colored("2.", "green"), print("People Profiles")

    try:
        choice = int(input(colored("\nEnter your choice (1 or 2): ", "yellow")))
        
        if choice == 1:
            urls = get_urls_from_user()
            if urls:
                scrape_linkedin_company_data(API_KEY, urls)
            else:
                print_bold_colored("No URLs provided. Exiting the script.", "red")

        elif choice == 2:
            people = get_linkedin_profiles_from_user()
            if people:
                scrape_linkedin_people_data(API_KEY, people)
            else:
                print_bold_colored("No names provided. Exiting the script.", "red")

        else:
            print_bold_colored("Invalid choice. Please select 1 or 2.", "red")
    
    except ValueError:
        print_bold_colored("Invalid input. Please enter a valid number (1 or 2).", "red")

