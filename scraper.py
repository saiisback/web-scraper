import aiohttp
import asyncio
from bs4 import BeautifulSoup
import logging
import random
import time
from utils import exponential_backoff

async def fetch(session, url, headers, retries):
    for attempt in range(retries):
        try:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()
                html = await response.text()
                return html
        except aiohttp.ClientError as e:
            logging.warning(f"Error fetching {url}, attempt {attempt + 1}: {e}")
            await asyncio.sleep(exponential_backoff(attempt))
    logging.error(f"Failed to fetch {url} after {retries} attempts")
    return None

async def scrape_page(session, url, headers, selectors, retries):
    html = await fetch(session, url, headers, retries)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        data = {}
        for key, selector in selectors.items():
            element = soup.select_one(selector)
            data[key] = element.get_text(strip=True) if element else None
        return data
    return None

async def scrape_pages(base_url, num_pages, headers, selectors, retries, concurrency):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for page in range(1, num_pages + 1):
            url = f"{base_url}/page/{page}"
            tasks.append(scrape_page(session, url, headers, selectors, retries))
        return await asyncio.gather(*tasks)

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler('scraper.log'),
                                  logging.StreamHandler()])
