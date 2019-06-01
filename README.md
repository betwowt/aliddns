# aliddns

### 快速开始

python 版本

请使用 python 3

```
pip install aliyun-python-sdk-core-v3 aliyun-python-sdk-alidns bs4 requests
```

> 使用前需要在域名解析增加一条符合配置文件的解析记录(重要)

修改配置文件

```
{
  "accessKeyId": "", // aliyun token
  "accessSecret": "",
  "domainName":"", 二级域名
  "tertiaryDomain":"" 三级域
}
```