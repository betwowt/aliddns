

import json
import logging

from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from aliyunsdkcore.client import AcsClient

logger = logging.getLogger(__name__)

"""
    aliyun dns api 调度类
"""


class Consumer:

    # 读取配置文件
    def __init__(self, json_file):
        with open(json_file, 'r') as myfile:
            data = myfile.read()
        self.data = json.loads(data)
        self.client = AcsClient(self.get_data()['accessKeyId'], self.get_data()['accessSecret'], 'cn-hangzhou')

    # get method
    def get_data(self):
        return self.data

    # set method
    def set_data(self,data):
        self.data = data

    # 获取dns解析列表
    def get_dns_list(self):

        request = DescribeDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_DomainName(self.get_data()['domainName'])
        request.set_RRKeyWord(self.get_data()['tertiaryDomain'])
        response = self.client.do_action_with_exception(request)
        res_json = json.loads(str(response, encoding='utf-8'))
        return res_json['DomainRecords']['Record']

    def update_dns_resolve(self, ip, recordId, type):
        request = UpdateDomainRecordRequest()
        request.set_accept_format('json')
        request.set_Value(ip)
        request.set_Type(type)
        request.set_RR(self.get_data()['tertiaryDomain'])
        request.set_RecordId(recordId)
        response = self.client.do_action_with_exception(request)
        logger.info("域名解析修改成功:%s",ip)


