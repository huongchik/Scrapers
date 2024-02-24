from scrapy import signals
from scrapy.http import TextResponse, Response
import json

class AsyncParsingMiddleware:
    """
    Middleware to process JSON responses for Scrapy spiders. If the request URL contains "ajax=true",
    the response is parsed as JSON and converted back to a TextResponse for further processing.
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        Initializes the middleware and connects it to the spider_opened signal.
        """
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        return middleware

    def process_response(self, request, response, spider):
        """
        Processes each response by checking if it is an AJAX request. If so, it attempts to parse the
        response as JSON and returns a new TextResponse object for further processing.
        """
        if "ajax=true" in request.url:
            try:
                data = json.loads(response.text)
                # Assuming further processing is needed on the data, it's converted back to a string
                new_response_body = json.dumps(data, ensure_ascii=False).encode('utf8')
                return TextResponse(url=response.url, body=new_response_body, encoding='utf8')
            except json.JSONDecodeError:
                spider.logger.error('Failed to decode JSON from response.')
                # Return the original response if JSON parsing fails
                return response
        # Return the original response if not an AJAX request or after handling errors
        return response

    def spider_opened(self, spider):
        """
        Logs a message when a spider is opened.
        """
        spider.logger.info(f'Spider opened: {spider.name}')


