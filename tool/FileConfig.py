import json
import os
import platform


config_json = '''
{
  "OSS_ACCESS_KEY_ID": "",
  "OSS_ACCESS_KEY_SECRET": "",
  "OSS_BUCKET": "",
  "OSS_ENDPOINT": "",
  "UPLOAD_PATH": "",
  "UPLOAD_DOMAIN": ""
}
'''


def set_config_path():
    # 创建Linux下配置文件目录
    if platform.system() == 'Linux':
        #
        config_path = os.path.expanduser('~') + '/.config/PyQtPicUpload/'
        if not os.path.exists(config_path):
            os.mkdir(config_path)
        # print(config_path)
        config_file = config_path + 'config.json'
        return config_file

# 检测配置文件
def checkConfig(config_file):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
            # print(str(config))
            access_key_id = config['OSS_ACCESS_KEY_ID']
            # print(access_key_id)
            access_key_secret = config['OSS_ACCESS_KEY_SECRET']
            # print(access_key_secret)
            bucket_name = config['OSS_BUCKET']
            endpoint = config['OSS_ENDPOINT']
            upload_path = config['UPLOAD_PATH']
            upload_domain = config['UPLOAD_DOMAIN']
            # print(upload_domain)
            for param in (access_key_id, access_key_secret, bucket_name, endpoint, upload_path, upload_domain):
                assert '' != param, '请配置上传参数！'
            return [access_key_id, access_key_secret, bucket_name, endpoint, upload_path, upload_domain]
    except Exception as e:
        print(e)
        return None


def saveConfig(access_key_id, access_key_secret, bucket_name, endpoint, upload_path, upload_domain):

    config_file = set_config_path()

    with open(config_file, 'w+') as file:
        json_config = {
            "OSS_ACCESS_KEY_ID": access_key_id,
            "OSS_ACCESS_KEY_SECRET": access_key_secret,
            "OSS_BUCKET": bucket_name,
            "OSS_ENDPOINT": endpoint,
            "UPLOAD_PATH": upload_path if upload_path[-1] == '/' else upload_path + '/',
            "UPLOAD_DOMAIN": upload_domain if upload_domain[-1] == '/' else upload_domain + '/'
        }
        file.write(json.dumps(json_config))