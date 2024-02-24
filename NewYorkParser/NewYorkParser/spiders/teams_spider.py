import scrapy
from scrapy.crawler import CrawlerProcess

class HockeyTeamsSpider(scrapy.Spider):
    """
    Spider for scraping hockey team information from a site that lists team statistics in a form-based page.
    This spider specifically searches for teams, possibly filtering by criteria (e.g., location like 'New York').
    """
    name = 'hockey_teams'
    allowed_domains = ['www.scrapethissite.com']
    start_urls = ['https://www.scrapethissite.com/pages/forms/']

    def parse(self, response):
        """
        Initial parse method that sends a form request to filter team data by a specific query (e.g., 'New York').
        """
        yield scrapy.FormRequest(
            url='https://www.scrapethissite.com/pages/forms/',  # Target URL for the form request.
            formdata={'q': 'New York'},  # Form data sent with the request, filtering the results.
            method='GET',  # HTTP method used for the form request.
            callback=self.after_search  # Callback method to process the response after the form is submitted.
        )

    def after_search(self, response):
        """
        Callback method to process the data after the initial form request.
        Extracts and yields team statistics from the filtered results page.
        """
        teams = response.xpath('//tr[@class="team"]')  # Selects all team rows in the table.
        for team in teams:
            ot_losses = team.xpath('./td[@class="ot-losses"]/text()').get().strip()  # Extracts OT Losses, handling empty strings.
            ot_losses = 'N/A' if ot_losses == '' else ot_losses  # Defaults to 'N/A' if OT Losses is empty.

            yield {
                'Team Name': team.xpath('./td[@class="name"]/text()').get().strip(),
                'Year': team.xpath('./td[@class="year"]/text()').get().strip(),
                'Wins': team.xpath('./td[@class="wins"]/text()').get().strip(),
                'Losses': team.xpath('./td[@class="losses"]/text()').get().strip(),
                'OT Losses': ot_losses,
                'Win %': team.xpath('./td[contains(@class, "pct")]/text()').get().strip(),
                'Goals For (GF)': team.xpath('./td[@class="gf"]/text()').get().strip(),
                'Goals Against (GA)': team.xpath('./td[@class="ga"]/text()').get().strip(),
                '+ / -': team.xpath('./td[contains(@class, "diff")]/text()').get().strip(),
            }

        # Attempts to follow the 'Next' page link if it exists to scrape additional data.
        next_page_url = response.xpath('//a[@aria-label="Next"]/@href').get()
        if next_page_url:
            yield response.follow(next_page_url, self.after_search)  # Recursively follows the next page link.

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "result.json": {
                "format": "json",
                "encoding": "utf8",
                "indent": 4,
                "ensure_ascii": False  # Ensures non-ASCII characters are properly saved in the output file.
            },
        },
    })

    process.crawl(HockeyTeamsSpider)
    process.start()
