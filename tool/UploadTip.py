import json
import sys
import time
import os
import oss2
from PyQt5.QtCore import QSize, Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from tool import FileConfig
import notify2


class UploadAction(QThread):
    status = pyqtSignal(str)

    def __init__(self, filepath):
        super(UploadAction, self).__init__()
        try:
            with open(FileConfig.set_config_path(), 'r') as file:
                config = json.load(file)
        except Exception as e:
            print(e)
            self.status.emit(False)

        self.filepath = filepath
        # print(str(config))
        self.access_key_id = config['OSS_ACCESS_KEY_ID']
        # print(access_key_id)
        self.access_key_secret = config['OSS_ACCESS_KEY_SECRET']
        # print(access_key_secret)
        self.bucket_name = config['OSS_BUCKET']
        self.endpoint = config['OSS_ENDPOINT']
        self.upload_path = config['UPLOAD_PATH'] if config['UPLOAD_PATH'][-1] == '/' else config['UPLOAD_PATH'] + '/'
        # 在域名后面添加 /
        self.upload_domain = config['UPLOAD_DOMAIN'] if config['UPLOAD_DOMAIN'][-1] == '/' else config[
                                                                                                    'UPLOAD_DOMAIN'] + '/'

    def percentage(self, consumed_bytes, total_bytes):
        """进度条回调函数，计算当前完成的百分比
        :param consumed_bytes: 已经上传/下载的数据量
        :param total_bytes: 总数据量
        """
        if total_bytes:
            rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
            print('\r{0}% '.format(rate))
            sys.stdout.flush()

    def run(self):
        print('filepath:',self.filepath)
        # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
        bucket = oss2.Bucket(oss2.Auth(self.access_key_id, self.access_key_secret), self.endpoint, self.bucket_name)
        # 必须以二进制的方式打开文件。
        # 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        with open(self.filepath, 'rb') as fileobj:
            # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
            upload_name = self.upload_path + self.filepath.split('/')[-1]
            bucket.put_object(upload_name, fileobj, progress_callback=self.percentage)
            self.status.emit(self.upload_domain + upload_name)
            # print('result_url:',self.upload_domain + upload_name)
class UploadTip(QWidget):
    def __init__(self):
        super(UploadTip, self).__init__()
        self.pic_show = QLabel()
        # self.resize(300,500)
        # self.pic_show.setMaximumSize(300, 400)
        self.pic_show.setObjectName('pic_show')
        # self.pic_show.setStyleSheet('align:center')
        self.pic_show.setAlignment(Qt.AlignCenter)

        self.pic_show.setPixmap(
            QPixmap(os.getcwd() + '/images/upload.png'))

        self.pic_show.setStyleSheet('border:4px solid;')
        # self.pic_show.
        # .scaled(self.pic_show.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

        self.pic_tip = QLabel('Ctrl + V 粘贴图片')
        self.pic_tip.setAlignment(QtCore.Qt.AlignCenter)

        self.tip_layout = QVBoxLayout(self)
        self.tip_layout.addStretch()
        self.tip_layout.addWidget(self.pic_show)
        self.tip_layout.addStretch()

        self.tip_layout.addWidget(self.pic_tip)
        # self.tip_layout.addStretch()
        self.upload_btn = QPushButton('点击上传')
        self.upload_btn.setObjectName('upload_btn')

        # self.upload_btn.set(Qt.AlignCenter)

        self.tip_layout.addWidget(self.upload_btn, 0, Qt.AlignCenter)

        # layout.setSpacing(0)
        # 美化风格
        # self.setStyleSheet(qt_material.apply_stylesheet(self,''))
        self.createActions()

        self.upload_btn.clicked.connect(self.upload_action)

        self.restore_path = ''
        self.setLayout(self.tip_layout)
    def upload_action(self):
        if self.restore_path != '':
            self.upload_btn.setEnabled(False)
            self.upload_btn.setText('上传中...')
            self.upload_action.start()

    def upload_status(self, status):
        # print('upload_status:',status)
        # 判断上传结果
        if status:
            print(status)
            clipboard = QApplication.clipboard()
            clipboard.setText('![]('+status+')')
            notify2.init('OSS上传')
            notify2.Notification('OSS上传',status,self.restore_path).show()
            self.upload_btn.setText('点击上传')
            self.upload_btn.setEnabled(True)
        else:
            print('upload error ！')
        os.remove(self.restore_path)

    def createActions(self):
        pastAction = QAction(self)
        pastAction.setShortcut("Ctrl+V")
        pastAction.triggered.connect(self.pasteData)
        self.addAction((pastAction))  # Activate QAction

    def setImage(self, path):
        # print(path)
        image = QPixmap(path)
        # print(image.width(),image.height())
        if image.width() > image.height():
            scale = self.pic_show.width() / image.width()
            # print('比例:', scale)

            # width=scale*clipboard.pixmap().width()*scale
            height = image.height() * scale
            # print('转换后高度：', height)
            self.pic_show.setPixmap(image.scaled(QSize(self.pic_show.width(), int(height))))  # 用于粘贴图片
        else:
            scale = self.pic_show.height() / image.height()
            # print('比例:', scale)
            width = image.width() * scale
            # print('转换后宽度：', width)
            self.pic_show.setPixmap(image.scaled(QSize(int(width), self.pic_show.height())))
            self.pic_show.setAlignment(QtCore.Qt.AlignCenter)


    def pasteData(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()

        if mimeData.hasImage():

            # 根据时间设置图片文件名
            file_name = time.strftime('%Y-%m-%d-%H%M%S', time.localtime()) + '.png'
            # 将图片保存到指定位置
            self.restore_path = '/tmp/' + file_name
            clipboard.pixmap().save(self.restore_path, 'PNG')

            # print(restore_path)
            self.setImage(self.restore_path)
        elif mimeData.hasText():
            self.restore_path = clipboard.text()
            self.setImage(self.restore_path)
        print("pasted from clipboard")

        # 设置点击事件的信号传递
        self.upload_action = UploadAction(self.restore_path)
        self.upload_action.status.connect(self.upload_status)
