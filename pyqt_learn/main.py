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

    pm = PluginManager()
    pm.searchPlugins("./pyqt_learn/plugins")
    for module in pm.getPlugins():
        if hasattr(module, "handleClick"):
            pb = QPushButton()
            pb.setObjectName(module.module_name)
            text = module.getBtnText() if hasattr(module, "getBtnText") else module.module_name
            pb.setText(text)
            pb.clicked.connect(module.handleClick)
            pb.show()
            widget.ui.gridLayout.addWidget(pb)

    print("plugins", pm.getPluginNames())
    widget.ui.pushButton.clicked.connect(lambda: pm.handlePluginClick("test_filedialogue"))

    sys.exit(app.exec_())
