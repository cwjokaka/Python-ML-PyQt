import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from ui_linear_regression_base import Ui_LinearRegressionBase
from ui_main import Ui_MainWindow
import pandas as pd

from ui_matplotlib_widget import Ui_MatplotlibWwidget


class Ui_LinearRegression(QWidget, Ui_LinearRegressionBase):

    def __init__(self):
        super(Ui_LinearRegression, self).__init__()
        self.setupUi(self)
        self.df = None
        self.pushButton.clicked.connect(self.on_open_file)
        self.model = QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(['数据...'])
        self.tableView.setModel(self.model)
        self.pushButton_create.clicked.connect(self.on_create_draw)

    def on_open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', './src/algorithm',
                                                   "csv files (*.txt *.csv)")
        if file_path == '':
            return
        # 取第一行为列名
        if self.checkBox_header.isChecked():
            self.df = pd.read_csv(file_path, header=0)
        else:
            self.df = pd.read_csv(file_path, header=None)

        self.model.clear()
        cols = [f'{value} 'for value in self.df.columns.values]
        self.model.setHorizontalHeaderLabels(cols)
        for row_num, row in self.df.iterrows():
            for col_num, it in enumerate(row):
                item = QStandardItem(f'{it}')
                self.model.setItem(row_num, col_num, item)

    def on_create_draw(self):
        if self.df is None:
            return
        self.mpl = Ui_MatplotlibWwidget()
        self.mpl.show()
