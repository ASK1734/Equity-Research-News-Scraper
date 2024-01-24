 # Equity Research News Scraper

## Overview
As an equity researcher, staying informed with the latest financial news is crucial for making well-informed decisions. This tool is designed to streamline the process of gathering recent news related to specific stocks or market sectors.

## About Annue
Annue is a renowned and extensive online platform for financial news. Recognized for its comprehensive coverage and timely updates, it serves as an invaluable resource for researchers, investors, and financial analysts.

## Tool Functionality
This script allows users to input either a stock ID or stock name to automatically retrieve related news from the past 10 days. It's tailored to assist in gathering and analyzing current market trends and company-specific news, enhancing the efficiency of your research process.

## Features
- **Keyword-Based Search**: Enter the stock ID or name to find relevant news articles.
- **Time-Sensitive Retrieval**: Focuses on news from the most recent 10 days, ensuring the relevance of the information.
- **Targeted Source**: Extracts news from China Times, a leading publication with a focus on the Chinese market.
- **Recent News**: The script specifically crawls news from the last two days, providing you with the most current updates.

## Installation and Dependencies
To use this tool, you need to have the following Python libraries installed:
- `re` - For regular expressions, crucial in parsing text.
- `time` - For handling time-related functions.
- `requests` - For making HTTP requests to retrieve web pages.
- `BeautifulSoup` from `bs4` - For parsing HTML and XML documents.
- `json` - For parsing JSON data.
- `datetime`, `timedelta` from `datetime` - For manipulating dates and times.
- `brotli` - For handling Brotli compression, often used in web data.
- `pytz` - For dealing with time zone calculations.

You can install these dependencies using pip. Run the following command:
```bash
pip install requests beautifulsoup4 brotli pytz
```

## How to Use
1. **Install Dependencies**: Follow the instructions above to install the necessary libraries.
2. **Run the Script**: Execute the script and enter the desired stock ID or name when prompted.
3. **View Results**: The script will display a list of news articles related to your query.

## Limitations
Please note that the script currently only supports news retrieval from Annue. Future updates may include additional sources.

