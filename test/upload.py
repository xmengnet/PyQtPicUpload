# -*- coding: utf-8 -*-
import json
import os

import oss2
import sys

# 以下代码展示了文件上传的高级用法，如断点续传、分片上传等。

# 首先初始化AccessKeyId、AccessKeySecret、Endpoint等信息。
# 通过环境变量获取，或者把诸如“<你的AccessKeyId>”替换成真实的AccessKeyId等。
#
# 以杭州区域为例，Endpoint可以是：
#   http://oss-cn-hangzhou.aliyuncs.com
#   https://oss-cn-hangzhou.aliyuncs.com
# 分别以HTTP、HTTPS协议访问。

# print(os.getcwd())
class Upload():
    def __init__(self,path) :
        config={}
        try:
            with open(path, 'r') as file:
                config = json.load(file)
        except Exception as e:
            print(e)
            return False
        # print(str(config))
        self.access_key_id = config['OSS_ACCESS_KEY_ID']
        # print(access_key_id)
        self.access_key_secret = config['OSS_ACCESS_KEY_SECRET']
        # print(access_key_secret)
        self.bucket_name = config['OSS_BUCKET']
        self.endpoint = config['OSS_ENDPOINT']
        self.upload_path = config['UPLOAD_PATH'] if config['UPLOAD_PATH'][-1] == '/' else config['UPLOAD_PATH'] + '/'
        # 在域名后面添加 /
        self.upload_domain = config['UPLOAD_DOMAIN'] if config['UPLOAD_DOMAIN'][-1] == '/' else config['UPLOAD_DOMAIN'] + '/'
# print(upload_domain)


    def percentage(self,consumed_bytes, total_bytes):
        """进度条回调函数，计算当前完成的百分比
        
        :param consumed_bytes: 已经上传/下载的数据量
        :param total_bytes: 总数据量
        """
        if total_bytes:
            rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
            print('\r{0}% '.format(rate))
            # sys.stdout.flush()

    def upload(self,filepath):
        print(filepath)
        # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
        bucket = oss2.Bucket(oss2.Auth(self.access_key_id, self.access_key_secret), self.endpoint, self.bucket_name)
        # 必须以二进制的方式打开文件。
        # 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        with open(filepath, 'rb') as fileobj:
            # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
            upload_name = self.upload_path + filepath.split('/')[-1]
            bucket.put_object(upload_name, fileobj, progress_callback= self.percentage)

            return self.upload_domain + upload_name



# 确认上面的参数都填写正确了
# try:
#     for param in (access_key_id, access_key_secret, bucket_name, endpoint, upload_path, upload_domain):
#         assert '' != param, '请配置上传参数！'
# except Exception as e:
#     print(e)

# print(upload('/home/liyp/Pictures/壁纸/web-illust_71411811_20181116_203823.png'))
