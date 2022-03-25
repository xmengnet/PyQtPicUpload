import os
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from ListWidgetItem import ListWidgetItem

class ConfigView(QLabel):
    def __init__(self):
        super(ConfigView, self).__init__()
        self.config_view=QLabel()

    def configAction(self):
        dialog = QDialog()
        # dialog.resize(300,200)
        dialog.setMaximumSize(500 ,400)
        dialog.setWindowTitle("配置oss信息")
        access_key_id_label = QLabel('access_key_id:')
        access_key_id_text = QLineEdit()
        access_key_secret_label = QLabel('access_key_secret:')
        access_key_secret_text = QLineEdit()
        access_key_secret_text.setEchoMode(QLineEdit.Password)
        bucket_name_label = QLabel('bucket_name')
        bucket_name_text = QLineEdit()
        bucket_name_text.setPlaceholderText('设置存储空间名')
        endpoint_label = QLabel('endpoint')
        endpoint_text = QLineEdit()
        endpoint_text.setPlaceholderText('地域节点(如：oss-cn-beijing.aliyuncs.com)')
        upload_path_label = QLabel('upload_path')
        upload_path_text = QLineEdit()
        upload_path_text.setPlaceholderText('上传路径(如：images/)')
        upload_domain_label = QLabel('upload_domain')
        upload_domain_text = QLineEdit()
        upload_domain_text.setPlaceholderText('绑定域名(需要带https://)')
        dialog_layout = QGridLayout()
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        dialog.setFont(font)
        dialog_layout.addWidget(access_key_id_label, 0, 0)
        dialog_layout.addWidget(access_key_id_text, 0, 1)
        dialog_layout.addWidget(access_key_secret_label, 1, 0)
        dialog_layout.addWidget(access_key_secret_text, 1, 1)
        dialog_layout.addWidget(bucket_name_label, 2, 0)
        dialog_layout.addWidget(bucket_name_text, 2, 1)
        dialog_layout.addWidget(endpoint_label, 3, 0)
        dialog_layout.addWidget(endpoint_text, 3, 1)
        dialog_layout.addWidget(upload_path_label, 4, 0)
        dialog_layout.addWidget(upload_path_text, 4, 1)
        dialog_layout.addWidget(upload_domain_label, 5, 0)
        dialog_layout.addWidget(upload_domain_text, 5, 1)
        save_btn = QPushButton('保存配置')
        content = [access_key_id_text.text(), access_key_secret_text.text(), bucket_name_text.text(),
                   endpoint_text.text(), upload_path_text.text(), upload_domain_text.text()]

        save_btn.clicked.connect(lambda: self.save_oss_config(content))
        dialog_layout.addWidget(save_btn, 6, 1)
        dialog.setLayout(dialog_layout)
        # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.exec_()