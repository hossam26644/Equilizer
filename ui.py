# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1263, 957)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1281, 311))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(_fromUtf8("border-image: url(:/image/47383964-dj-image.jpg) 0 0 0 0 stretch stretch;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 320, 1259, 261))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        
        self.mplvl = QtGui.QVBoxLayout(self.widget_2)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))


        self.dockWidget = QtGui.QDockWidget(Form)
        self.dockWidget.setGeometry(QtCore.QRect(0, 630, 1261, 301))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(80, 250, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(190, 250, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(310, 250, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(430, 250, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(540, 250, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.dockWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(650, 250, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.dockWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(770, 250, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.dockWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(890, 250, 66, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.dockWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(1010, 250, 66, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.dockWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(1120, 250, 66, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.layoutWidget = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 1251, 241))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.two = QtGui.QSlider(self.layoutWidget)
        self.two.setOrientation(QtCore.Qt.Vertical)
        self.two.setObjectName(_fromUtf8("two"))
        self.horizontalLayout.addWidget(self.two)
        self.four = QtGui.QSlider(self.layoutWidget)
        self.four.setOrientation(QtCore.Qt.Vertical)
        self.four.setObjectName(_fromUtf8("four"))
        self.horizontalLayout.addWidget(self.four)
        self.six = QtGui.QSlider(self.layoutWidget)
        self.six.setOrientation(QtCore.Qt.Vertical)
        self.six.setObjectName(_fromUtf8("six"))
        self.horizontalLayout.addWidget(self.six)
        self.eight = QtGui.QSlider(self.layoutWidget)
        self.eight.setOrientation(QtCore.Qt.Vertical)
        self.eight.setObjectName(_fromUtf8("eight"))
        self.horizontalLayout.addWidget(self.eight)
        self.ten = QtGui.QSlider(self.layoutWidget)
        self.ten.setOrientation(QtCore.Qt.Vertical)
        self.ten.setObjectName(_fromUtf8("ten"))
        self.horizontalLayout.addWidget(self.ten)
        self.twelve = QtGui.QSlider(self.layoutWidget)
        self.twelve.setOrientation(QtCore.Qt.Vertical)
        self.twelve.setObjectName(_fromUtf8("twelve"))
        self.horizontalLayout.addWidget(self.twelve)
        self.fourteen = QtGui.QSlider(self.layoutWidget)
        self.fourteen.setOrientation(QtCore.Qt.Vertical)
        self.fourteen.setObjectName(_fromUtf8("fourteen"))
        self.horizontalLayout.addWidget(self.fourteen)
        self.sixteen = QtGui.QSlider(self.layoutWidget)
        self.sixteen.setOrientation(QtCore.Qt.Vertical)
        self.sixteen.setObjectName(_fromUtf8("sixteen"))
        self.horizontalLayout.addWidget(self.sixteen)
        self.eighteen = QtGui.QSlider(self.layoutWidget)
        self.eighteen.setOrientation(QtCore.Qt.Vertical)
        self.eighteen.setObjectName(_fromUtf8("eighteen"))
        self.horizontalLayout.addWidget(self.eighteen)
        self.twenty = QtGui.QSlider(self.layoutWidget)
        self.twenty.setOrientation(QtCore.Qt.Vertical)
        self.twenty.setObjectName(_fromUtf8("twenty"))
        self.horizontalLayout.addWidget(self.twenty)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 598, 1261, 51))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Import = QtGui.QPushButton(self.layoutWidget1)
        self.Import.setObjectName(_fromUtf8("Import"))
        self.horizontalLayout_2.addWidget(self.Import)
        self.ShowFrequencies = QtGui.QPushButton(self.layoutWidget1)
        self.ShowFrequencies.setObjectName(_fromUtf8("ShowFrequencies"))
        self.horizontalLayout_2.addWidget(self.ShowFrequencies)
        self.Save = QtGui.QPushButton(self.layoutWidget1)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.horizontalLayout_2.addWidget(self.Save)

        self.two.setMinimum (0)
        self.two.setMaximum (5)
        self.two.setValue(1)

        self.four.setMinimum (0)
        self.four.setMaximum (5)
        self.four.setValue(1)

        self.six.setMinimum (0)
        self.six.setMaximum (5)
        self.six.setValue(1)

        self.eight.setMinimum (0)
        self.eight.setMaximum (5)
        self.eight.setValue(1)

        self.ten.setMinimum (0)
        self.ten.setMaximum (5)
        self.ten.setValue(1)

        self.twelve.setMinimum (0)
        self.twelve.setMaximum (5)
        self.twelve.setValue(1)

        self.fourteen.setMinimum (0)
        self.fourteen.setMaximum (5)
        self.fourteen.setValue(1)

        self.sixteen.setMinimum (0)
        self.sixteen.setMaximum (5)
        self.sixteen.setValue(1)

        self.eighteen.setMinimum (0)
        self.eighteen.setMaximum (5)
        self.eighteen.setValue(1)

        self.twenty.setMinimum (0)
        self.twenty.setMaximum (5)
        self.twenty.setValue(1)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Harvard Equilizer", None))
        self.label.setText(_translate("Form", "0:2 KHZ", None))
        self.label_2.setText(_translate("Form", "2:4 KHZ", None))
        self.label_3.setText(_translate("Form", "4:6 KHZ", None))
        self.label_4.setText(_translate("Form", "6:8 KHZ", None))
        self.label_5.setText(_translate("Form", "8:10 KHZ", None))
        self.label_6.setText(_translate("Form", "10:12 KHZ", None))
        self.label_7.setText(_translate("Form", "12:14 KHZ", None))
        self.label_8.setText(_translate("Form", "14:16 KHZ", None))
        self.label_9.setText(_translate("Form", "16:18 KHZ", None))
        self.label_10.setText(_translate("Form", "18:20 KHZ", None))
        self.Import.setText(_translate("Form", "Import", None))
        self.ShowFrequencies.setText(_translate("Form", "Show frequencies", None))
        self.Save.setText(_translate("Form", "Save", None))

import resources_rc
