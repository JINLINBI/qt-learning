from eaio_helper.utils import getMainWindow


class PluginBase:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)

    # 装饰器-添加按钮
    class add_button:
        buttons = {}
    
        # load_ui: True的话说明，需要ui辅助输入，点击按钮不会直接触发装饰器的函数，而是生成二级页面
        def __init__(self, button_name, load_ui=False, *args, **kwargs):
            print(f"button_name: {button_name}")
            self.param = (args, kwargs)
            self.button_name = button_name
            self.load_ui = load_ui

        def __call__(self, func):
            def wrapper(load_ui, *args, **kwargs):
                mainWidget = getMainWindow()
                print(args, kwargs)
                desc = kwargs.get("description", "")
                mainWidget.ui.labelPlugin.setText(f"model: \ndescription: {desc}")

                print(f"load_ui? {load_ui}")
                if load_ui:
                    mainWidget.ui.pushButton.clicked.connect(lambda: func(*args, **kwargs))
                    return
                # else:
                #     mainWidget.ui.pushButton.show()

                # 执行被装饰的函数
                return func(*args, **kwargs)

            self.buttons[self.button_name] = {
                "param": self.param,
                "load_ui": self.load_ui,
                "func": wrapper,
            }
            return wrapper
            


    # def add_button(func):
    #     def wrapper(self, *args, **kwargs):
    #         if not isinstance(self, PluginBase):
    #             raise TypeError("self is not a PluginBase derive class!")
    #         # 执行被装饰的函数
    #         return func(*args, **kwargs)
    #     return wrapper

    def stop():
        return

    def reload():
        return


class Plugin1(PluginBase):
    pass


class Plugin2(PluginBase):
    pass

print(PluginBase.plugins)  # 输出 [Plugin1, Plugin2]
