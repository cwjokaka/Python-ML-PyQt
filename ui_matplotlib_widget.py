from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from ui_linear_regression_base import Ui_LinearRegressionBase
from ui_main import Ui_MainWindow
import pandas as pd

from ui_matplotlib_widget_base import Ui_matplotlib_widget_base


class Ui_MatplotlibWwidget(QWidget, Ui_matplotlib_widget_base):

    def __init__(self):
        super(Ui_MatplotlibWwidget, self).__init__()
        self.setupUi(self)
        self.widget.mpl.start_static_plot()
