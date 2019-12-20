import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from ui_linear_regression import Ui_LinearRegression
from ui_linear_regression_base import Ui_LinearRegressionBase
from ui_main import Ui_MainWindow


class MainWin(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('ML😔')
        # self.tab_welcome.
        # newPage = QWidget(self.tabWidget)
        # self.tabWidget.addTab(newPage, 'newPage')
        self.treeWidget.clicked.connect(self.on_tree_clicked)
        self.tabWidget.tabCloseRequested.connect(self.on_close_tab)

    def on_tree_clicked(self, qmodelindex):
        item = self.treeWidget.currentItem()
        if item.childCount() > 0:
            return

        for i in range(self.tabWidget.count()):
            item_text = item.text(0)
            if self.tabWidget.tabText(i) == item_text:
                return

        title = item.text(0)
        if title == 'LinearRegression':
            self.tabWidget.addTab(Ui_LinearRegression(), item.text(0))
        self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)
        print(f"key={item.text(0)} ,value={item.text(1)}, index:{qmodelindex}")

    def on_close_tab(self, tab_index):
        self.tabWidget.removeTab(tab_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
