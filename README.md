# Advanced Web Scraper

This is an advanced web scraper built with Python. It uses `aiohttp` for asynchronous requests, `BeautifulSoup` for parsing HTML, and `selenium` for handling JavaScript-rendered content. The scraper can handle dynamic content, rotate User-Agent strings, use proxies, and store data in CSV or SQLite. It also includes robust error handling, retry logic with exponential backoff, and email notifications upon completion or failure.

## Features

- **Concurrent Requests**: Asynchronous scraping using `aiohttp`.
- **Data Cleaning**: Basic data cleaning and preprocessing.
- **Customizable Selectors**: User-defined CSS selectors or XPath expressions for data extraction.
- **Error Handling and Retry Logic**: Robust error handling and retry logic with exponential backoff.
- **User-Agent Rotation**: Rotate User-Agent strings to avoid being blocked.
- **Proxy Support**: Use proxies to avoid IP bans (to be integrated).
- **Email Notifications**: Send email notifications upon completion or failure.
- **Configuration File for Advanced Settings**: Easily configurable via `config.yaml`.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/advanced-web-scraper.git
   cd advanced-web-scraper
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required libraries:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install ChromeDriver (if using Selenium):**
   Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your PATH.

## Configuration

1. **Edit `config.yaml`** to configure advanced settings:
   ```yaml
   user_agents:
     - "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
     - "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
     - "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
   retries: 3
   concurrency: 5
   notification:
     to_email: "user@example.com"
     from_email: "scraper@example.com"
     smtp_server: "smtp.example.com"
     smtp_port: 587
     smtp_user: "your_smtp_user"
     smtp_pass: "your_smtp_password"
   ```

## Usage

1. **Run the scraper:**
   ```sh
   python main.py
   ```

2. **Follow the prompts** to input the base URL, number of pages to scrape, save options (CSV or database), and other configurations.

## Project Structure

- `scraper.py`: Contains the scraping logic.
- `utils.py`: Contains utility functions like saving to a CSV, database operations, and sending email notifications.
- `main.py`: The entry point that ties everything together and handles user input.
- `config.yaml`: Configuration file for advanced settings.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Issues

If you encounter any issues, please create an issue in the repository.

## Acknowledgements

This project uses the following libraries:
- `aiohttp`
- `beautifulsoup4`
- `selenium`
- `pyyaml`
```

### `requirements.txt`

Here's the content of `requirements.txt` for the project dependencies:

```plaintext
aiohttp
beautifulsoup4
selenium
pyyaml
```

