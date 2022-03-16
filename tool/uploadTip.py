import sys
import time
import os
import qt_material
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap


class UploadTip(QWidget):
    def __init__(self):
        super(UploadTip, self).__init__()
        self.pic_show = QLabel()
        # self.resize(300,500)
        self.pic_show.setMaximumSize(300, 400)
        self.pic_show.setPixmap(
            QPixmap('../images/icon.png'))
        # .scaled(self.pic_show.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

        self.pic_tip = QLabel('Ctrl + V 粘贴图片')
        self.pic_tip.setAlignment(QtCore.Qt.AlignCenter)

        self.tip_layout = QVBoxLayout()
        self.tip_layout.addStretch()
        self.tip_layout.addWidget(self.pic_show)
        self.tip_layout.addStretch()

        self.tip_layout.addWidget(self.pic_tip)
        self.tip_layout.addStretch()

        # layout.setSpacing(0)
        # 美化风格
        # self.setStyleSheet(qt_material.apply_stylesheet(self,''))
        self.createActions()
        self.setLayout(self.tip_layout)

    def createActions(self):
        pastAction = QAction(self)
        pastAction.setShortcut("Ctrl+V")
        pastAction.triggered.connect(self.pasteData)
        self.addAction((pastAction))  # Activate QAction

    def setImage(self, path):

        image = QPixmap(path)
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

        # self.pic_show.repaint()
        # pass

    def pasteData(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasImage():

            # 根据时间设置图片文件名
            file_name = time.strftime('%Y-%m-%d-%H%M%S', time.localtime()) + '.png'
            # 将图片保存到指定位置
            clipboard.pixmap().save(file_name, 'PNG')

            restore_path = '../'

            self.setImage(restore_path + file_name)
            os.remove(restore_path + file_name)

        elif mimeData.hasText():
            path = clipboard.text()
            self.setImage(path)
        print("pasted from clipboard")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     qt_material.apply_stylesheet(app, theme='light_teal.xml')
#     main = UploadTip()
#     app.setWindowIcon(QIcon('./images/icon.svg'))
#     main.show()
#     sys.exit(app.exec_())
