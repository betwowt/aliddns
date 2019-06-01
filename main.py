from alisdk.ali_sdk_consumer import consumer
from crawl.crawl_client import Client
import logging

# 日志配置
logging.basicConfig(filename='log.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

logger = logging.getLogger(__name__)


"""
    程序入口
"""

if __name__ == '__main__':
    logging.info("程序开始")
    ip = Client().getMyIp()
    consumer = consumer()
    list = consumer.getDnsList()
    for item in list:
        old_ip = item['Value'];
        if(old_ip != ip):
            logging.info("旧ip:%s,与新ip:%s存在差异,更新域名解析为新ip:%s",old_ip,ip,ip)
            consumer.updateDnsResolve(ip,item['RecordId'],item['Type'])
        else:
            logging.info("ip一致无需修改")
    logging.info("程序结束")

