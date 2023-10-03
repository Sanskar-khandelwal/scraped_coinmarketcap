import scrapy
from scrapy.http import Request
import json


class CrytosApiSpider(scrapy.Spider):
    name = "crytos_api"
    allowed_domains = ["coinmarketcap.com"]
    increment = 100
    startPostion = 101

    def start_requests(self):
        yield Request(url="https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap",
                      callback=self.parse, headers={
                          "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"
                      })

    def parse(self, response):
        data = json.loads(response.body)
        cryptodata = data.get('data').get('cryptoCurrencyList')
        for item in cryptodata:
            yield {
                'id': item.get('id'),
                'name': item.get('name'),
                'symbol': item.get('symbol'),
                'slug': item.get('slug'),
                'cmcRank': item.get('cmcRank'),
                'circulatingSupply': item.get('circulatingSupply'),
                'marketPairCount': item.get('marketPairCount'),
                'selfReportedCirculatingSupply': item.get('selfReportedCirculatingSupply'),
                'totalSupply': item.get('totalSupply'),
                'maxSupply': item.get('maxSupply'),
                'high24h': item.get('high24h'),
                'low24h': item.get('low24h'),
                'ath': item.get('ath'),
                'atl': item.get('atl'),

            }

        next_page = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start={self.startPostion}&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"

        totalCount = int(data.get('data').get('totalCount'))
        if self.startPostion < totalCount:
            self.startPostion += self.increment
            yield Request(url=next_page, callback=self.parse, headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"
            })
