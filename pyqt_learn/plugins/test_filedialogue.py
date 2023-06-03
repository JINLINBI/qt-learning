from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PySide6.QtGui import QWindow
from mainwindow import MainWindow

def initialize():
    # 初始化插件
    pass

def getMainWindow():
    top_level_windows = QApplication.topLevelWindows()
    for window in top_level_windows:
        # 判断窗口类型是否为 MainWindow
        print("window type", window, f"type{type(window)}")
        if isinstance(window, QWindow):
            print("is qmainWindow")
            return window
        else:
            print("not qmainwindow")

def handleClick():
    # 处理插件按钮被点击事件
    mainwindow = getMainWindow()
    # text = mainwindow.ui.lineEdit.text()
    text = "???22222"
    if text:
        # 弹出提示框显示输入的文本
        QMessageBox.information(None, 'Input Text', f'The input text is: {text}')
    else:
        # 弹出警告框提示输入不能为空
        QMessageBox.warning(None, 'Warning', 'The input cannot be empty!')

def getBtnText():
    return "插件1按钮"