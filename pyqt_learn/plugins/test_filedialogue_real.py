from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QWindow

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
    # 弹出提示框显示输入的文本
    filename, _= QFileDialog.getOpenFileName(None, "打开文件测试", ".", "txt files (*.txt)")
    print("dialog get filename", filename)

def getBtnText():
    return "打开文件"