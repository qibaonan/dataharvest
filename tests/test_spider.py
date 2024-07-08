import pytest

from dataharvest.spider.common_spider import CommonSpider
from dataharvest.spider.spider import AutoSpider


def test_common_spider():
    spider = CommonSpider()
    doc = spider.crawl(
        "https://baike.baidu.com/item/%E9%87%91%E7%BC%95%E7%8E%89%E8%A1%A3/617831?fr=ge_ala"
    )
    print(doc)


@pytest.mark.asyncio
async def test_async_common_spider():
    spider = CommonSpider()
    doc = await spider.a_crawl(
        "https://baike.baidu.com/item/%E9%87%91%E7%BC%95%E7%8E%89%E8%A1%A3/617831?fr=ge_ala"
    )
    print(doc)


def test_auto_spider():
    spider = AutoSpider()
    doc = spider.crawl("https://zhuanlan.zhihu.com/p/369984873")
    print(doc)


def test_mafengwo_spider():
    spider = AutoSpider()
    doc = spider.crawl("https://www.mafengwo.cn/i/2987983.html")
    print(doc)
    print(doc.page_content)


@pytest.mark.asyncio
async def test_async_common_spider():
    spider = AutoSpider()
    doc = await spider.a_crawl("https://www.mafengwo.cn/i/2987983.html")
    print(doc)
    print(doc.page_content)
