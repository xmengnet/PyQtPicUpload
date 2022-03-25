import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize

from tool.UploadTip import UploadTip
from tool.ConfigWidget import ConfigView
from tool import QSSLoader

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QHBoxLayout(self, spacing=0)
        self.listWidget = QListWidget()
        self.resize(800, 600)

        layout.addWidget(self.listWidget)

        # 右侧层叠窗口
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.iniUI()

    def iniUI(self):
        # 初始化界面
        # 通过QListWidget的当前item变化来切换QStackedWidget中的序号
        self.listWidget.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex)
        # 去掉边框
        # self.listWidget.setFrameShape(QListWidget.NoFrame)
        # # 隐藏滚动条
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # print(os.getcwd())
        self.upload_item = QListWidgetItem(
            QIcon(QPixmap(os.getcwd()+'/images/upload.png')), '上传区', self.listWidget)
        self.set_item = QListWidgetItem(
            QIcon(QPixmap(os.getcwd()+'/images/setting_icon.png')), '配置区域')
        self.upload_item.setSizeHint(QSize(16777215, 60))
        # 文字居中
        self.upload_item.setTextAlignment(Qt.AlignCenter)

        self.set_item.setSizeHint(QSize(16777215, 60))
        # 文字居中
        self.set_item.setTextAlignment(Qt.AlignCenter)

        self.listWidget.addItem(self.upload_item)
        self.listWidget.addItem(self.set_item)
        upload_widget = UploadTip()
        config_widget = ConfigView()

        self.stackedWidget.addWidget(upload_widget)
        self.stackedWidget.addWidget(config_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    style_file = 'resource/current.qss'
    style_sheet = QSSLoader.QSSLoader.read_qss_file(style_file)
    # apply_stylesheet(app, theme='light_blue.xml')
    app.setWindowIcon(QIcon('./images/icon.svg'))
    main.setStyleSheet(style_sheet)

    main.show()
    sys.exit(app.exec_())
