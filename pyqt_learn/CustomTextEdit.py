from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QDropEvent

class CustomTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.viewport().setAcceptDrops(True)

    def dragEnterEvent(self, event: QDropEvent):
        print("drop enter event")
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        print("drop event")
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            file_path = urls[0].toLocalFile()
            self.load_file(file_path)
            print("drop event", file_path)
            event.acceptProposedAction()

    def load_file(self, file_path):
        print(f"loading file {file_path}")
        with open(file_path, "r") as file:
            text = file.read()
            self.setPlainText(text)
