# Scrapers

This repository hosts two distinct Scrapy projects designed for scraping dynamic web content. Each project targets a specific use case: one for scraping hockey team information and another for movie data, showcasing the flexibility of Scrapy in handling both form-based pages and AJAX-loaded content.

## Projects Overview

### 1. Movies Scraper

- **Directory**: `MoviesParser/`
- **Description**: Includes a Scrapy spider and a custom middleware for scraping movie information from a site that uses AJAX for content loading, targeting movies released between 2010 and 2015.

### 2. Hockey Teams Scraper

- **Directory**: `NewYorkParser/`
- **Description**: A Scrapy spider that filters and extracts hockey team statistics from a form-based web page, specifically focusing on teams possibly filtered by criteria such as location (e.g., 'New York').



## Features

- Demonstrates handling of both traditional form-based web pages and modern AJAX-loaded content.
- Utilizes custom Scrapy middleware to process JSON responses for AJAX-loaded data.
- Provides examples of dynamic request generation, data extraction, and data cleaning techniques.
- Showcases pagination handling and the scraping of data across multiple pages.


