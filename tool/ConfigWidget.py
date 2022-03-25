from PyQt5.QtWidgets import *
from tool.FileConfig import *


class ConfigView(QWidget):
    def __init__(self):
        super(ConfigView, self).__init__()
        layout = QGridLayout()

        self.access_key_id_label = QLabel('access_key_id:')
        self.access_key_id_text = QLineEdit()
        self.access_key_secret_label = QLabel('access_key_secret:')
        self.access_key_secret_text = QLineEdit()
        self.access_key_secret_text.setEchoMode(QLineEdit.Password)
        self.bucket_name_label = QLabel('bucket_name')
        self.bucket_name_text = QLineEdit()
        self.bucket_name_text.setPlaceholderText('设置存储空间名')
        self.endpoint_label = QLabel('endpoint')
        self.endpoint_text = QLineEdit()
        self.endpoint_text.setPlaceholderText('地域节点(如：oss-cn-beijing.aliyuncs.com)')
        self.upload_path_label = QLabel('upload_path')
        self.upload_path_text = QLineEdit()
        self.upload_path_text.setPlaceholderText('上传路径(如：images/)')
        self.upload_domain_label = QLabel('upload_domain')
        self.upload_domain_text = QLineEdit()
        self.upload_domain_text.setPlaceholderText('绑定域名(需要带https://)')
        self.set_confirm = QPushButton('保存')
        self.set_confirm.setObjectName('set_confirm')
        self.set_default = QPushButton('设为默认图床')
        self.set_default.setCheckable(False)
        self.set_default.setObjectName('default_btn')
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.set_confirm)
        btn_layout.addWidget(self.set_default)

        # 填充配置文件
        config = checkConfig(set_config_path())

        if config != None:
            self.access_key_id_text.setText(config[0])
            self.access_key_secret_text.setText(config[1])
            self.bucket_name_text.setText(config[2])
            self.endpoint_text.setText(config[3])
            self.upload_path_text.setText(config[4])
            self.upload_domain_text.setText(config[5])

        self.set_confirm.clicked.connect(self.save_config)

        layout.addWidget(self.access_key_id_label, 0, 0)
        layout.addWidget(self.access_key_id_text, 0, 1)
        layout.addWidget(self.access_key_secret_label, 1, 0)
        layout.addWidget(self.access_key_secret_text, 1, 1)
        layout.addWidget(self.bucket_name_label, 2, 0)
        layout.addWidget(self.bucket_name_text, 2, 1)
        layout.addWidget(self.endpoint_label, 3, 0)
        layout.addWidget(self.endpoint_text, 3, 1)
        layout.addWidget(self.upload_path_label, 4, 0)
        layout.addWidget(self.upload_path_text, 4, 1)
        layout.addWidget(self.upload_domain_label, 5, 0)
        layout.addWidget(self.upload_domain_text, 5, 1)
        layout.addItem(btn_layout, 6, 1)

        self.setLayout(layout)

    def save_config(self):
        saveConfig(self.access_key_id_text.text(), self.access_key_secret_text.text(), self.bucket_name_text.text(),
                   self.endpoint_text.text(),
                   self.upload_path_text.text(), self.upload_domain_text.text())
