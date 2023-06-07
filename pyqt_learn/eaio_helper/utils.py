from PySide6.QtWidgets import QApplication, QMainWindow
import platform

def get_home_path():
    if platform.system() == "Windows":
        return "C:\\Program Files\\sangfor\\EAIO"
    elif platform.system() == "Linux":
        return "/usr/share/sangfor/EAIO"
    else:
        return "/Library/sangfor/EAIO"


def getMainWindow():
    top_level_windows = QApplication.topLevelWidgets()
    for window in top_level_windows:
        # 判断窗口类型是否为 MainWindow
        if isinstance(window, QMainWindow):
            return window
