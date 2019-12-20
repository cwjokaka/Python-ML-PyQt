# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_matplotlib_widget_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_matplotlib_widget_base(object):
    def setupUi(self, matplotlib_widget_base):
        matplotlib_widget_base.setObjectName("matplotlib_widget_base")
        matplotlib_widget_base.resize(401, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(matplotlib_widget_base)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = MatplotlibWidget(matplotlib_widget_base)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(matplotlib_widget_base)
        QtCore.QMetaObject.connectSlotsByName(matplotlib_widget_base)

    def retranslateUi(self, matplotlib_widget_base):
        _translate = QtCore.QCoreApplication.translate
        matplotlib_widget_base.setWindowTitle(_translate("matplotlib_widget_base", "Form"))
from matplotlib_widget import MatplotlibWidget
