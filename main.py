import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

from func import get_remote_branches, set_branch


class MyWindow(QWidget):
    def __init__(self, buttons):
        super().__init__()
        self.initUI(buttons)

    def button_clicked(self, button_text, button_id):
        print(f"Нажата {button_text} с ID {button_id}")
        set_branch(dirname, button_id)
        sys.exit(app.exec())

    def initUI(self, buttons):
        self.setWindowTitle("Окно с тремя кнопками")
        self.setGeometry(1000, 30, 300, 200)

        layout = QVBoxLayout()

        for button in buttons:
            button_widget = QPushButton(button["text"])
            # button_widget.setStyleSheet(f"background-color: {button.get('color', '#ffffff')};")
            button_widget.clicked.connect(
                lambda checked, text=button["text"], btn_id=button["id"]: self.button_clicked(text, btn_id))
            layout.addWidget(button_widget)

        self.setLayout(layout)


if __name__ == "__main__":
    global dirname
    dirname = r"C:\PyProjects\Python_Basic"
    x = get_remote_branches(dirname).stdout
    print(x)
    print('---------')
    # print(type(x))
    app = QApplication(sys.argv)
    buttons = []
    for i in x.split('\n'):
        if i.find('->') == -1 and i.find('/') != -1:
            buttons.append({"text": i, "id": i.split('/')[1].strip()})
    print(buttons)
    window = MyWindow(buttons)
    window.show()
    sys.exit(app.exec())
