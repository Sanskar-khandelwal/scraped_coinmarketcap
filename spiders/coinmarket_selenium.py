from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from scrapy.selector import Selector
from selenium.webdriver.support.ui import WebDriverWait
import time
import scrapy


class CoinmarketappCoinsSpiderSelenium(scrapy.Spider):
    name = "coinmarket_selenium"
    allowed_domains = ["coinmarketcap.com"]
    start_urls = ["https://coinmarketcap.com"]

    def __init__(self):
        chrome_options = Options()
        # Set user agent string if needed
        user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(
            executable_path=chrome_path, chrome_options=chrome_options)
        driver.get("https://coinmarketcap.com")
        wait = WebDriverWait(driver, 10)
        time.sleep(10)

        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3)")
        # time.sleep(3)

        # driver.execute_script("window.scrollTo(document.body.scrollHeight/3, document.body.scrollHeight/2)")
        # time.sleep(3)

        # driver.execute_script("window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight)")
        # time.sleep(3)

        # For the scrolling of the page

        # scroll_increment = 300  # Adjust this value based on the scrolling speed you desire
        # previous_scrolled = 0

        # for _ in range(0, driver.execute_script("return document.body.scrollHeight"), scroll_increment):
        #     driver.execute_script(
        #         f"window.scrollTo({previous_scrolled}, {_});")
        #     previous_scrolled = _
        #     time.sleep(3)  # Adjust the sleep time based on your needs

        # Implicit wait to ensure elements load properly
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight/6)")
        time.sleep(10)

        driver.execute_script(
            "window.scrollTo(document.body.scrollHeight/6, document.body.scrollHeight/5)")
        time.sleep(3)

        driver.execute_script(
            "window.scrollTo(document.body.scrollHeight/5, document.body.scrollHeight/4)")
        time.sleep(3)
        driver.execute_script(
            "window.scrollTo(document.body.scrollHeight/4, document.body.scrollHeight/3)")
        time.sleep(3)
        driver.execute_script(
            "window.scrollTo(document.body.scrollHeight/3, document.body.scrollHeight/2)")
        time.sleep(3)
        driver.execute_script(
            "window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight)")
        time.sleep(3)
        driver.implicitly_wait(10)

        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        # Use Scrapy's Selector to parse the HTML content
        resp = Selector(text=self.html)
        for item in resp.xpath("//tbody/tr"):
            name = item.xpath('.//div//p[1]/text()').get()
            yield {
                'name': name
            }
