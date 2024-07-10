import logging
import asyncio
import random
from scraper import scrape_pages, setup_logging
from utils import save_to_csv, save_to_db, read_config, send_email, rotate_user_agent

def get_user_input():
    base_url = input("Enter the base URL of the website to scrape: ")
    num_pages = int(input("Enter the number of pages to scrape: "))
    save_to = input("Do you want to save data to 'csv' or 'db'? ")
    output_file = "article_titles.csv" if save_to == "csv" else None
    db_name = "scraper_data.db" if save_to == "db" else None
    use_selenium = input("Use Selenium for JavaScript rendering (yes/no)? ").lower() == "yes"
    
    selectors = {}
    while True:
        key = input("Enter the name of the data field to extract (or press Enter to finish): ")
        if not key:
            break
        selector = input(f"Enter the CSS selector or XPath for '{key}': ")
        selectors[key] = selector
    
    return base_url, num_pages, save_to, output_file, db_name, use_selenium, selectors

async def main():
    setup_logging()
    config = read_config()

    base_url, num_pages, save_to, output_file, db_name, use_selenium, selectors = get_user_input()
    
    headers = {
        'User-Agent': rotate_user_agent(config['user_agents']),
    }
    
    retries = config['retries']
    concurrency = config['concurrency']
    
    all_data = await scrape_pages(base_url, num_pages, headers, selectors, retries, concurrency)
    all_data = [data for data in all_data if data]  # Remove None entries

    if save_to == 'csv':
        save_to_csv(all_data, output_file)
    elif save_to == 'db':
        save_to_db(all_data, db_name)
    else:
        logging.error("Invalid save_to option")
    
    logging.info("Scraping completed")
    
    send_email(
        subject="Web Scraping Completed",
        body="The web scraping task has been completed successfully.",
        to_email=config['notification']['to_email'],
        from_email=config['notification']['from_email'],
        smtp_server=config['notification']['smtp_server'],
        smtp_port=config['notification']['smtp_port'],
        smtp_user=config['notification']['smtp_user'],
        smtp_pass=config['notification']['smtp_pass']
    )

if __name__ == "__main__":
    asyncio.run(main())
