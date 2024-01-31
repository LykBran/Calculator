# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_back = QPushButton(Form)
        self.pushButton_back.setObjectName(u"pushButton_back")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.pushButton_back.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_back)

        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_clear)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_add = QPushButton(Form)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy1)
        self.pushButton_add.setFont(font)

        self.gridLayout.addWidget(self.pushButton_add, 0, 0, 1, 1)

        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy1.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy1)
        self.pushButton_1.setFont(font)

        self.gridLayout.addWidget(self.pushButton_1, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setFont(font)

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font)

        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)

        self.pushButton_sub = QPushButton(Form)
        self.pushButton_sub.setObjectName(u"pushButton_sub")
        sizePolicy1.setHeightForWidth(self.pushButton_sub.sizePolicy().hasHeightForWidth())
        self.pushButton_sub.setSizePolicy(sizePolicy1)
        self.pushButton_sub.setFont(font)

        self.gridLayout.addWidget(self.pushButton_sub, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setFont(font)

        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setFont(font)

        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setFont(font)

        self.gridLayout.addWidget(self.pushButton_6, 1, 3, 1, 1)

        self.pushButton_mul = QPushButton(Form)
        self.pushButton_mul.setObjectName(u"pushButton_mul")
        sizePolicy1.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy1)
        self.pushButton_mul.setFont(font)

        self.gridLayout.addWidget(self.pushButton_mul, 2, 0, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setFont(font)

        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setFont(font)

        self.gridLayout.addWidget(self.pushButton_8, 2, 2, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setFont(font)

        self.gridLayout.addWidget(self.pushButton_9, 2, 3, 1, 1)

        self.pushButton_div = QPushButton(Form)
        self.pushButton_div.setObjectName(u"pushButton_div")
        sizePolicy1.setHeightForWidth(self.pushButton_div.sizePolicy().hasHeightForWidth())
        self.pushButton_div.setSizePolicy(sizePolicy1)
        self.pushButton_div.setFont(font)

        self.gridLayout.addWidget(self.pushButton_div, 3, 0, 1, 1)

        self.pushButton_calculate = QPushButton(Form)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        sizePolicy1.setHeightForWidth(self.pushButton_calculate.sizePolicy().hasHeightForWidth())
        self.pushButton_calculate.setSizePolicy(sizePolicy1)
        self.pushButton_calculate.setFont(font)

        self.gridLayout.addWidget(self.pushButton_calculate, 3, 1, 1, 1)

        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy1.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy1)
        self.pushButton_0.setFont(font)

        self.gridLayout.addWidget(self.pushButton_0, 3, 2, 1, 1)

        self.pushButton_point = QPushButton(Form)
        self.pushButton_point.setObjectName(u"pushButton_point")
        sizePolicy1.setHeightForWidth(self.pushButton_point.sizePolicy().hasHeightForWidth())
        self.pushButton_point.setSizePolicy(sizePolicy1)
        self.pushButton_point.setFont(font)

        self.gridLayout.addWidget(self.pushButton_point, 3, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"<-", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_mul.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_point.setText(QCoreApplication.translate("Form", u".", None))
    # retranslateUi

