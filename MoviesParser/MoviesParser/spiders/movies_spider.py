import scrapy
import json
from scrapy.crawler import CrawlerProcess
import re

class MoviesSpider(scrapy.Spider):
    """
    Spider for scraping movie information from a site that uses AJAX for content loading.
    Specifically targets movies released between 2010 and 2015.
    """
    name = 'movies'
    allowed_domains = ['scrapethissite.com']  # Restricts scraping to this domain to avoid offsite requests
    start_urls = ['https://www.scrapethissite.com/pages/ajax-javascript/']  # Initial URL to start scraping from

    def start_requests(self):
        """
        Generates requests for different years to scrape movie data that is loaded via AJAX.
        """
        years = range(2010, 2016)
        for year in years:
            yield scrapy.Request(
                url=f'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={year}',
                callback=self.parse_movies
            )

    def parse_movies(self, response):
        """
        Parses the AJAX-loaded JSON response containing movie data.
        """
        data = json.loads(response.text)
        for movie in data:
            # Clean up movie titles by replacing sequences of whitespace with a single space
            title = re.sub(r'\s+', ' ', movie['title']).strip()
            yield {
                'Title': title,
                'Nominations': movie['nominations'],
                'Awards': movie['awards'],
                'Best Picture': movie.get('best_picture', 'N/A'),  # Use 'N/A' if 'best_picture' is not present
            }

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "movies.json": {
                "format": "json",
                "encoding": "utf8",
                "indent": 4,
                "ensure_ascii": False  # Ensures that non-ASCII characters are properly saved
            },
        },
    })

    process.crawl(MoviesSpider)
    process.start()
