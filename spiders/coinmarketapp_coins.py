import scrapy
from scrapy_splash import SplashRequest


class CoinmarketappCoinsSpider(scrapy.Spider):
    script = ''' 
                function main(splash)
                        local num_scrolls = 10
                        local scroll_delay = 1
                        local scroll_to = splash:jsfunc("window.scrollTo")
                        local get_body_height = splash:jsfunc(
                            "function() {return document.body.scrollHeight;}"
                        )
                        assert(splash:go(splash.args.url))
                        splash:wait(3)

                        for _ = 1, num_scrolls do
                            local height = get_body_height()
                            for i = 1, 10 do
                                scroll_to(0, height * i/10)
                                splash:wait(scroll_delay/10)
                            end
                        end        
                        return splash:html()  
            end
'''
    name = "coinmarketapp_coins"
    allowed_domains = ["coinmarketcap.com"]

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"
    }

    def start_requests(self):
        yield SplashRequest(url="https://www.coinmarketcap.com", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script,
        }, headers=self.headers)

    def parse(self, response):
        print(response.body)
        for item in response.xpath("//tbody/tr"):
            name = item.xpath('.//div//p[1]/text()').get()

            yield {
                'name': name
            }
