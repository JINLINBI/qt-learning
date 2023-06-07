from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PySide6.QtGui import QWindow
from mainwindow import MainWindow

from eaio_helper.plugin import PluginBase
from eaio_helper.utils import getMainWindow


class testPlugin(PluginBase):
    def __init__(self):
        pass

    @staticmethod
    def initialize(self):
        # 初始化插件
        pass

    @PluginBase.add_button(button_name="插件2按钮", load_ui=True, cls=PluginBase, description="这是一个描述\n怎么描述好呢?\n不太清楚呢")
    def handleClick(cls, *args, **kw):
        # 处理插件按钮被点击事件
        mainwindow = getMainWindow()
        # text = mainwindow.ui.lineEdit.text()
        text = "???11111"
        if text:
            # 弹出提示框显示输入的文本
            QMessageBox.information(None, 'Input Text', f'The input text is: {text}')
        else:
            # 弹出警告框提示输入不能为空
            QMessageBox.warning(None, 'Warning', 'The input cannot be empty!')

    def description(self):
        return """
        简介：测试插件
        可以获取使用方法：
        1. 输入xxx
        2. 点击ad发扥
        """