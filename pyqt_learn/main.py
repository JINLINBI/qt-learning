import sys

from PySide6.QtWidgets import QApplication, QPushButton
from mainwindow import MainWindow
from qt_material import apply_stylesheet

from plugin_manager import PluginManager


if __name__ == "__main__":
    app = QApplication()
    apply_stylesheet(app, theme="default_dark.xml")
    widget = MainWindow()
    widget.show()

    import os

    current_path = os.path.dirname(os.path.abspath(__file__))
    print("Current file path:", current_path)

    pm = PluginManager()
    pm.searchPlugins(os.path.join(current_path, "plugins"))
    # for module in pm.getPlugins():
    #     print("name", module.module_name)
    #     if hasattr(module, "handleClick"):
    #         pb = QPushButton()
    #         pb.setObjectName(module.module_name)
    #         text = module.getBtnText() if hasattr(module, "getBtnText") else module.module_name
    #         pb.setText(text)
    #         pb.clicked.connect(module.handleClick)
    #         pb.show()
    #         widget.ui.gridLayout.addWidget(pb)
    # print("plugins", pm.getPluginNames())

    # 排列插件按钮
    pm.layoutButtons(widget.ui.gridLayout, colnum = 3)

    widget.ui.pushButton.clicked.connect(lambda: pm.handlePluginClick("test_filedialogue"))

    sys.exit(app.exec_())
