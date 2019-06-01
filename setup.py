from setuptools import setup

setup(
   name='aliddns',
   version='1.0',
   description='阿里云ddns更新脚本',
   author='betwowt',
   author_email='betwowt@gmail.com',
   packages=['aliddns'],
   install_requires=['aliyun-python-sdk-core-v3','aliyun-python-sdk-alidns','bs4','requests']
)