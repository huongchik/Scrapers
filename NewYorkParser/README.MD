# Hockey Teams Scraper

This project is a Scrapy spider designed to scrape hockey team information from a website that lists team statistics on a form-based page. It focuses on extracting details about hockey teams, potentially filtering by criteria such as location (e.g., 'New York').

## Project Structure

- `NewYorkParser/spiders/teams_spider.py`: Contains the working code for the `HockeyTeamsSpider` spider.

## Features

- Filters hockey team data by specific query (e.g., 'New York') using a form request.
- Extracts team statistics from the filtered results page, including team name, year, wins, losses, OT losses, win percentage, goals for (GF), goals against (GA), and the plus/minus rating.
- Supports pagination by automatically following the 'Next' page link to scrape additional data.

## Setup

1. Ensure you have Python installed on your system.
2. Install Scrapy:
   ```bash
   pip install scrapy
    ```
## Usage
There are two ways to run the spider:

### Method 1: Using the Scrapy command
To run the spider, navigate to the project root directory and execute:
```bash
scrapy crawl hockey_teams -o result.json
```
This command will start the spider, scrape the data, and save the output in a file named result.json in the project root directory.

### Method 2: Running the Python script directly
You can also run the spider by executing the Python script directly:
```bash
python NewYorkParser/spiders/teams_spider.py
```
This method will initiate the CrawlerProcess within the script, starting the spider and saving the scraped data to result.json as configured in the script's settings.