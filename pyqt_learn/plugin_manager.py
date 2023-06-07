import os
import importlib
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QObject, Signal
from eaio_helper.plugin import PluginBase

class PluginManager(QObject):
    # 定义一个信号，当插件被选中时触发
    pluginSelected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.plugins = []

    def searchPlugins(self, path):
        # 搜索指定路径下的所有 python 文件
        print(os.getcwd())
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.py'):
                    module_name = os.path.splitext(file)[0]
                    module_path = os.path.join(root, file)
                    try:
                        # 加载 Python 模块并初始化
                        spec = importlib.util.spec_from_file_location(module_name, module_path)
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        module.module_name = module_name
                        if hasattr(module, 'initialize'):
                            module.initialize()
                        # 将模块加入插件列表
                        self.plugins.append((module_name, module))
                    except Exception as e:
                        print(f'Failed to load plugin: {module_name}', str(e))

    def getButtons(self):
        return PluginBase.add_button.buttons
    
    def getPlugins(self):
        return [module for _, module in self.plugins]

    def handlePluginClick(self, name):
        print("handlePluginClick")

        # 处理点击插件按钮事件
        for plugin_name, plugin_module in self.plugins:
            if name == plugin_name:
                # 发送插件被选中的信号
                self.pluginSelected.emit(name)
                if hasattr(plugin_module, 'handleClick'):
                    # 调用插件的 handleClick 方法
                    plugin_module.handleClick()
                break

    def layoutButtons(self, parentWidget, colnum=1):
        count = 0
        for name, info in self.getButtons().items():
            print(f"name: {name}, handle_func: ${info}")
            pb = QPushButton()
            pb.setText(name)
            def closure():
                params = (info["func"], info["load_ui"], info["param"])
                def onClicked():
                    params[0](params[1], *(params[2][0]), **(params[2][1]))
                return onClicked
            pb.clicked.connect(closure())
            pb.show()

            # 排列组合
            count = count + 1
            parentWidget.addWidget(pb, (count - 1) // colnum, (count - 1) % colnum)