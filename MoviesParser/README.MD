# Movies Scraper

This project comprises a Scrapy spider along with a custom middleware designed to scrape movie information from a site that dynamically loads content using AJAX, specifically targeting movies released between 2010 and 2015.

## Project Structure

- `MoviesParser/spiders/movies_spider.py`: Contains the `MoviesSpider` for scraping movie data.
- `MoviesParser/async_parsing_middleware.py`: Implements the `AsyncParsingMiddleware` to handle AJAX-loaded JSON responses.

## Features

- Dynamically generates requests for movies released from 2010 to 2015, parsing AJAX-loaded content.
- Extracts movie titles, nominations, awards, and whether it won Best Picture, handling missing data gracefully.
- Uses a custom middleware to process JSON responses, facilitating the parsing of AJAX-loaded data.
- Cleans up movie titles to ensure a consistent format.

## Setup

1. Ensure Python and Scrapy are installed on your system.
2. Clone this project to your local machine.

## Installation

Run the following command to install the necessary dependencies:

```bash
pip install scrapy
```
## Usage
To run the spider, navigate to the project root directory and execute:
```bash
scrapy crawl movies -o movies.json
```
Alternatively, you can run the spider script directly with Python:
```bash
python MoviesParser/spiders/movies_spider.py
```
This command initiates the crawling process, saving the scraped movie data into movies.json.

## Middleware Usage
The AsyncParsingMiddleware is automatically utilized by the spider to handle AJAX-loaded JSON responses. It ensures that JSON data is correctly processed and made available for scraping, enhancing the spider's ability to extract detailed movie information.