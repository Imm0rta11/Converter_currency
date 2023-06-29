from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(361, 104)
        Form.setStyleSheet("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 60, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 51, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 40, 171, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 60, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Converter_currency"))
        self.comboBox.setItemText(0, _translate("Form", "USD$"))
        self.comboBox.setItemText(1, _translate("Form", "RUB₽"))
        self.comboBox.setItemText(2, _translate("Form", "EUR€"))
        self.comboBox.setItemText(3, _translate("Form", "PLNzł"))
        self.comboBox.setItemText(4, _translate("Form", "JPY¥"))
        self.pushButton.setText(_translate("Form", "Convert"))
        self.label_2.setText(_translate("Form", "   --->"))
        self.label.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "UAH₴"))
