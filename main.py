import PyQt5
import sys
from PyQt5 import QtWidgets
from sampel import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

USD = 36.5686
RUB = 0.42596
EUR = 39.83
PLN = 8.9425
JPY = 0.252
selected_format = 'USD$'


def calculate():
    try:
        if selected_format == 'USD$':
            x = int(ui.lineEdit.text())
            y = str(round(x * USD))
            ui.label.setText(y)
        if selected_format == 'RUB₽':
            x = int(ui.lineEdit.text())
            y = str(round(x * RUB))
            ui.label.setText(y)
        if selected_format == 'EUR€':
            x = int(ui.lineEdit.text())
            y = str(round(x * EUR))
            ui.label.setText(y)
        if selected_format == 'PLNzł':
            x = int(ui.lineEdit.text())
            y = str(round(x * PLN))
            ui.label.setText(y)
        if selected_format == 'JPY¥':
            x = int(ui.lineEdit.text())
            y = str(round(x * JPY))
            ui.label.setText(y)
    except ValueError:
        ui.label.setText('Error')


def set_selected_format(index):
    global selected_format
    format_mapping = {0: 'USD$', 1: 'RUB₽', 2: 'EUR€', 3: 'PLNzł', 4: 'JPY¥'}
    selected_format = format_mapping[index]


ui.pushButton.clicked.connect(calculate)
ui.comboBox.currentIndexChanged.connect(set_selected_format)
sys.exit(app.exec_())
