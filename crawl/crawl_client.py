import requests

from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh,zh-CN;q=0.9,en;q=0.8,en-US;q=0.7,en-AU;q=0.6,en-CA;q=0.5,en-ZA;q=0.4,en-NZ;q=0.3,en-IN;q=0.2,en-GB;q=0.1",
    'Cache-Control': "max-age=0",
    'Connection': "keep-alive",
    'Cookie': "__jsluid=3a2553f43ec63bdb88db9b9e7c3dddda; _ga=GA1.2.1541727517.1559280874; _gid=GA1.2.56373316.1559280874; LOVEAPP_SESSID=ef58898357573a65ec06143bbc3729682c38c581; Hm_lvt_123ba42b8d6d2f680c91cb43c1e2be64=1559280874,1559304784; Hm_lpvt_123ba42b8d6d2f680c91cb43c1e2be64=1559304790; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1559305319; Hm_lpvt_d7682ab43891c68a00de46e9ce5b76aa=1559305319",
    'Host': "www.ipip.net",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'Postman-Token': "5660d3c3-9bb5-47f2-b7d6-b8f7d910ccdb,f84f003b-e62a-4959-805f-8727c0346846",
    'cache-control': "no-cache"
}


class Client:

    """
        获取公网ip
    """

    def getMyIp(self):
        logger.info('开始查询ip')
        r = requests.get("https://www.ipip.net/ip.html", headers=headers);
        htmlEncoded = r.text.encode('utf-8')
        html = BeautifulSoup(htmlEncoded, 'html.parser')
        form = html.find('form')
        ip = form.contents[1]['value']
        logger.info("当前公网ip为:%s",ip)
        return ip

