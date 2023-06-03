# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMessageBox, QTextEdit
from PySide6.QtCore import QFileInfo, QFile, QDir
from PySide6.QtGui import QTextCursor, QAction, QDropEvent
from PySide6.QtUiTools import QUiLoader
from form_ui import Ui_MainWindow



SIZE_1K = 1024  
WARN_FILESIZE = 20
FORB_FILESIZE = 200

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__buildModelView()

    def __buildModelView(self):
        self.model = QFileSystemModel(self)
        self.model.setRootPath(QDir.currentPath())
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.doubleClicked.connect(self.on_treeView_Doubleclicked)

        # 为textedit添加保存动作
        self.createSaveAction(self.ui.textEdit)
        # self.ui.textEdit.close()
        # self.ui.textEdit = CustomTextEdit()
        # self.ui.textEdit.setAcceptDrops(True)
        # self.ui.textEdit.show()
        

    # 双击treeview对象
    def on_treeView_Doubleclicked(self, index):
        filepath = self.model.filePath(index)

        # 加载文件到textedit
        file_info = QFileInfo(filepath)
        if file_info.exists() and file_info.isFile():
            if self.openfile(filepath):
                self.openfilesuc(index)

    # 打开文件成功，记录加载的文件信息
    def openfilesuc(self, index):
        self.ui.LabPath.setText(self.model.filePath(index))
        self.ui.LabType.setText(self.model.type(index))
        self.ui.LabFileName.setText(self.model.fileName(index))
        #目录名#节点类型#文件名
        fileSize = self.model.size(index) / SIZE_1K
        if (fileSize < SIZE_1K):
            self.ui.LabFilesize.setText("%d KB" % fileSize)
        else:
            self.ui.LabFilesize.setText("%.2f MB" % (fileSize / 1024.0))

    def openfile(self, filepath):
        file_info = QFileInfo(filepath)
        if file_info.size() > (FORB_FILESIZE * SIZE_1K * SIZE_1K):
            ret = QMessageBox.critical(self, "提示", f"文件大于 {FORB_FILESIZE}MB，禁止打开.")
            return
        elif file_info.size() > (WARN_FILESIZE * SIZE_1K * SIZE_1K):
            ret = QMessageBox.warning(self, "提示", f"文件大于 {WARN_FILESIZE}MB，确定打开吗？",
                           QMessageBox.StandardButton.Ok,
                           QMessageBox.StandardButton.Cancel)
            if ret == QMessageBox.StandardButton.Cancel:
                return

        # 读取文件内容
        file = QFile(filepath)
        try:
            if file.open(QFile.ReadOnly | QFile.Text):
                byte_array = file.readAll()
                text = bytes(byte_array).decode('utf-8')

                # 将内容显示在QTextEdit控件中
                self.ui.textEdit.setPlainText(text)
                self.ui.textEdit.moveCursor(QTextCursor.Start)  # 移动光标到开头
                return True
            else:
                raise Exception("打开文件失败，请检查权限是否合适!")
        except Exception as e:
            QMessageBox.warning(self, "提示", f"打开文件失败：{e}",QMessageBox.StandardButton.Ok)


    def createSaveAction(self, target):
        # 创建一个动作并设置快捷键
        action = QAction("保存文件", target)
        action.setShortcut("Ctrl+S")

        def on_action_triggered():
            print("ctrl + S")

        # 连接动作的触发信号到槽函数
        action.triggered.connect(on_action_triggered)

        # 添加动作到菜单或工具栏
        target.addAction(action)