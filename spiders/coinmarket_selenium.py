from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from scrapy.selector import Selector
import time
import scrapy
from scrapy_splash import SplashRequest


class CoinmarketappCoinsSpiderSelenium(scrapy.Spider):

    name = "coinmarket_selenium"
    allowed_domains = ["coinmarketcap.com"]
    starturls = [
        'https://coinmarketcap.com'
    ]

    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_path = which("chromedriver")
        driver = webdriver.Chrome()
        driver.get("https://coinmarketcap.com")
        time.sleep(3)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight/3)")
        time.sleep(3)

        driver.execute_script(
            "window.scrollTo(document.body.scrollHeight/3, document.body.scrollHeight/2)")
        time.sleep(3)

        driver.execute_script(
            "window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight)")
        time.sleep(3)

        self.html = driver.page_source
        print(html)
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        print(resp)
