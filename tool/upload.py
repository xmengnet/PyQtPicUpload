# -*- coding: utf-8 -*-
import json
import oss2

# 以下代码展示了文件上传的高级用法，如断点续传、分片上传等。

# 首先初始化AccessKeyId、AccessKeySecret、Endpoint等信息。
# 通过环境变量获取，或者把诸如“<你的AccessKeyId>”替换成真实的AccessKeyId等。
#
# 以杭州区域为例，Endpoint可以是：
#   http://oss-cn-hangzhou.aliyuncs.com
#   https://oss-cn-hangzhou.aliyuncs.com
# 分别以HTTP、HTTPS协议访问。

config = {}
with open('../QtPicUpload/config.json', 'r') as file:
    config = json.load(file)
    # print(str(config))
access_key_id = config['OSS_ACCESS_KEY_ID']
# print(access_key_id)
access_key_secret = config['OSS_ACCESS_KEY_SECRET']
# print(access_key_secret)
bucket_name = config['OSS_BUCKET']
endpoint = config['OSS_ENDPOINT']
upload_path = config['UPLOAD_PATH'] if config['UPLOAD_PATH'][-1] == '/' else config['UPLOAD_PATH'] + '/'
# 在域名后面添加 /
upload_domain = config['UPLOAD_DOMAIN'] if config['UPLOAD_DOMAIN'][-1] == '/' else config['UPLOAD_DOMAIN'] + '/'
# print(upload_domain)


# 确认上面的参数都填写正确了
try:
    for param in (access_key_id, access_key_secret, bucket_name, endpoint, upload_path, upload_domain):
        assert '' != param, '请配置上传参数！'
except Exception as e:
    print(e)


def upload(filepath):
    print(filepath)
    # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    # 必须以二进制的方式打开文件。
    # 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
    with open(filepath, 'rb') as fileobj:
        # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
        upload_name = upload_path + filepath.split('/')[-1]
        bucket.put_object(upload_name, fileobj)

        return upload_domain + upload_name

# print(upload('/home/liyp/Pictures/壁纸/web-illust_71411811_20181116_203823.png'))