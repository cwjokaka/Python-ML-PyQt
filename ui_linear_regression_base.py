# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_linear_regression_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LinearRegressionBase(object):
    def setupUi(self, LinearRegressionBase):
        LinearRegressionBase.setObjectName("LinearRegressionBase")
        LinearRegressionBase.resize(362, 317)
        self.horizontalLayout = QtWidgets.QHBoxLayout(LinearRegressionBase)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(LinearRegressionBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.checkBox_header = QtWidgets.QCheckBox(LinearRegressionBase)
        self.checkBox_header.setObjectName("checkBox_header")
        self.horizontalLayout_5.addWidget(self.checkBox_header)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(LinearRegressionBase)
        self.tableView.setEnabled(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableView, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(LinearRegressionBase)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.pushButton_create = QtWidgets.QPushButton(LinearRegressionBase)
        self.pushButton_create.setObjectName("pushButton_create")
        self.gridLayout.addWidget(self.pushButton_create, 4, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(LinearRegressionBase)
        QtCore.QMetaObject.connectSlotsByName(LinearRegressionBase)

    def retranslateUi(self, LinearRegressionBase):
        _translate = QtCore.QCoreApplication.translate
        LinearRegressionBase.setWindowTitle(_translate("LinearRegressionBase", "Form"))
        self.pushButton.setText(_translate("LinearRegressionBase", "Files..."))
        self.checkBox_header.setText(_translate("LinearRegressionBase", "has_header"))
        self.label.setText(_translate("LinearRegressionBase", "TableView:"))
        self.pushButton_create.setText(_translate("LinearRegressionBase", "Create"))
