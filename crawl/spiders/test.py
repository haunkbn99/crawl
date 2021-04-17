import scrapy
class Crawling(scrapy.Spider):
    name = 'test'
    start_urls = ['https://xoso.com.vn']
    def parse(self,response):
        joke = response.xpath("//div[@class='section-content']")
        yield {
                'special-prize': joke.xpath(".//span[@class='special-prize']/text()").extract_first(),
                'prize1': joke.xpath(".//span[@class='prize1']/text()").extract_first(),
                'prize2_item0': joke.xpath(".//span[@id='mb_prize2_item0']/text()").extract_first(),
                'prize2_item1': joke.xpath(".//span[@id='mb_prize2_item1']/text()").extract_first(),
                'prize3_item0': joke.xpath(".//span[@id='mb_prize3_item0']/text()").extract_first(),
                'prize3_item1': joke.xpath(".//span[@id='mb_prize3_item1']/text()").extract_first(),
                'prize3_item2': joke.xpath(".//span[@id='mb_prize3_item2']/text()").extract_first(),
                'prize3_item3': joke.xpath(".//span[@id='mb_prize3_item3']/text()").extract_first(),
                'prize3_item4': joke.xpath(".//span[@id='mb_prize3_item4']/text()").extract_first(),
                'prize3_item5': joke.xpath(".//span[@id='mb_prize3_item5']/text()").extract_first(),
                'prize4_item0': joke.xpath(".//span[@id='mb_prize4_item0']/text()").extract_first(),
                'prize4_item1': joke.xpath(".//span[@id='mb_prize4_item1']/text()").extract_first(),
                'prize4_item2': joke.xpath(".//span[@id='mb_prize4_item2']/text()").extract_first(),
                'prize4_item3': joke.xpath(".//span[@id='mb_prize4_item3']/text()").extract_first(),
                'prize5_item0': joke.xpath(".//span[@id='mb_prize5_item0']/text()").extract_first(),
                'prize5_item1': joke.xpath(".//span[@id='mb_prize5_item1']/text()").extract_first(),
                'prize5_item2': joke.xpath(".//span[@id='mb_prize5_item2']/text()").extract_first(),
                'prize5_item3': joke.xpath(".//span[@id='mb_prize5_item3']/text()").extract_first(),
                'prize5_item4': joke.xpath(".//span[@id='mb_prize5_item4']/text()").extract_first(),
                'prize5_item5': joke.xpath(".//span[@id='mb_prize5_item5']/text()").extract_first(),
                'prize6_item0': joke.xpath(".//span[@id='mb_prize6_item0']/text()").extract_first(),
                'prize6_item1': joke.xpath(".//span[@id='mb_prize6_item1']/text()").extract_first(),
                'prize6_item2': joke.xpath(".//span[@id='mb_prize6_item2']/text()").extract_first(),
                'prize7_item0': joke.xpath(".//span[@id='mb_prize7_item0']/text()").extract_first(),
                'prize7_item1': joke.xpath(".//span[@id='mb_prize7_item1']/text()").extract_first(),
                'prize7_item2': joke.xpath(".//span[@id='mb_prize7_item2']/text()").extract_first(),
                'prize7_item3': joke.xpath(".//span[@id='mb_prize7_item3']/text()").extract_first()
            }
