# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QSizePolicy, QTabWidget, QTextEdit,
    QTreeView, QVBoxLayout, QWidget)
import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1027, 600)
        MainWindow.setBaseSize(QSize(600, 1027))
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/icon/images/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 1011, 571))
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(100, 100))
        self.tab.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 0, 961, 551))
        self.tabWidget_2.setElideMode(Qt.ElideRight)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.textEdit = QTextEdit(self.tab_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(350, 10, 591, 511))
        self.verticalLayoutWidget = QWidget(self.tab_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 390, 321, 91))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LabFileName = QLabel(self.verticalLayoutWidget)
        self.LabFileName.setObjectName(u"LabFileName")

        self.horizontalLayout_3.addWidget(self.LabFileName)

        self.LabFilesize = QLabel(self.verticalLayoutWidget)
        self.LabFilesize.setObjectName(u"LabFilesize")

        self.horizontalLayout_3.addWidget(self.LabFilesize)

        self.LabType = QLabel(self.verticalLayoutWidget)
        self.LabType.setObjectName(u"LabType")

        self.horizontalLayout_3.addWidget(self.LabType)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.LabPath = QLabel(self.verticalLayoutWidget)
        self.LabPath.setObjectName(u"LabPath")

        self.verticalLayout_2.addWidget(self.LabPath)

        self.horizontalLayoutWidget = QWidget(self.tab_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 10, 321, 371))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(self.horizontalLayoutWidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.header().setDefaultSectionSize(200)

        self.horizontalLayout.addWidget(self.treeView)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), u"\u8fdc\u7a0b")
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.tabWidget, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.treeView)
        QWidget.setTabOrder(self.treeView, self.tabWidget_2)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EAIO\u52a9\u624b", None))
        self.LabFileName.setText("")
        self.LabFilesize.setText("")
        self.LabType.setText("")
        self.LabPath.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u64cd\u4f5c", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u8d44\u6e90\u8def\u7531", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u672c\u5730", None))
    # retranslateUi

