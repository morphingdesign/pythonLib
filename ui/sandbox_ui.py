# import utils.dataUtils as dataU

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtWidgets, QtGui
import numpy as np


class Root(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        # self.main = Widget()

        # Setup model and data.
        self.model = QtGui.QStandardItemModel()
        self.header_labels = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8']
        self.num_of_cols = len(self.header_labels)
        self.num_of_rows = 14

        self.model.setHorizontalHeaderLabels(self.header_labels)
        self.model.setColumnCount(self.num_of_cols)
        self.model.setRowCount(self.num_of_rows)


        self.data = Data(self.num_of_cols, self.num_of_rows)
        self._populate_data()

        self.main = Table(self.model)
        self.main.setMinimumSize(600, 500)
        # self.main.resize(500, 600)
        self.main.show()

    def _populate_data(self):
        """"""
        for row_num, row_data in enumerate(self.data.data_by_row):
            for col_num, col_data in enumerate(row_data):
                # cell_datum = QtWidgets.QTableWidgetItem(str(col_data))
                cell_datum = QtGui.QStandardItem(str(col_data))
                cell_datum.setTextAlignment(QtCore.Qt.AlignCenter)
                self.model.setItem(row_num, col_num, cell_datum)




# class Widget(QWidget):
#
#     def __init__(self):
#         super(Widget, self).__init__()
#         self.setGeometry(100, 100, 700, 500)
#         # self.setGeometry(50, 50, 500, 300)
#         self.setWindowTitle('Test Panel')
#
#         self.dt = DataTable()
#         self.dt.setParent(self)
#         self._home()
#         self._connect_cell()
#
#     def _home(self):
#         self.show()
#
#     def _out_data(self, row, col):
#         print('(Row, Col): (%d, %d)' % (row, col))
#         # print('Column: %d' % col)
#
#     def _connect_cell(self):
#         self.dt.cellClicked.connect(self._out_data)


# class DataTable(QtWidgets.QTableWidget):
#
#     def __init__(self):
#         super(DataTable, self).__init__()
#         self.num_of_cols = 5
#         self.num_of_rows = 7
#         self.setColumnCount(self.num_of_cols)
#         self.setRowCount(self.num_of_rows)
#         self.setMinimumSize(600, 500)
#         self.data = Data(self.num_of_cols, self.num_of_rows)
#         self._populate_data()
#
#     def _populate_data(self):
#         """"""
#         for row_num, row_data in enumerate(self.data.data_by_row):
#             for col_num, col_data in enumerate(row_data):
#                 cell_datum = QtWidgets.QTableWidgetItem(str(col_data))
#                 cell_datum.setTextAlignment(QtCore.Qt.AlignCenter)
#                 self.setItem(row_num, col_num, cell_datum)


class Data:
    def __init__(self, columns, rows):
        # Create matrix by columns.
        self.data = np.zeros((columns, rows))
        # Convert numpy array to nested list.
        self.data_list = self.data.tolist()
        # Transpose matrix from columns to rows.
        self.data_by_row = list(zip(*self.data_list))

    def transpose_by_numpy(self):
        data_nparray = self.data
        data_nparray_t = data_nparray.T
        data_nparray_str = np.array2string(data_nparray_t)


class Table(QtWidgets.QTableView):
    def __init__(self, model):
        super(Table, self).__init__()
        self.setModel(model)
        self.frozen_table = QtWidgets.QTableView(self)
        self.init_frozen_table()

    def init_frozen_table(self):
        # Assign model to be the same as the other table's model.
        self.frozen_table.setModel(self.model())
        # Hide frozen table's vertical labels.
        self.frozen_table.verticalHeader().hide()
        # Position main table under frozen table.
        self.viewport().stackUnder(self.frozen_table)
        # Style frozen table to appear unique from main table.
        self.frozen_table.setStyleSheet('''
                    QTableView { border: none;
                                 background-color: #8EDE21;
                                 selection-background-color: #999;
                    }''')
        # Setup columns and isolate first column only.
        for col in range(1, self.model().columnCount()):
            self.frozen_table.setColumnHidden(col, True)
        self.frozen_table.setColumnWidth(0, self.columnWidth(0))
        # Isolate table contents only.
        self.frozen_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.frozen_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.frozen_table.show()

        self.update_frozen_table_geometry()

        self.setHorizontalScrollMode(self.ScrollPerPixel)
        self.setVerticalScrollMode(self.ScrollPerPixel)
        self.frozen_table.setVerticalScrollMode(self.ScrollPerPixel)

    def update_frozen_table_geometry(self):
        self.frozen_table.setGeometry(
                self.verticalHeader().width() + self.frameWidth(),
                self.frameWidth(), self.columnWidth(0),
                self.viewport().height() + self.horizontalHeader().height())


def main():

    app = QApplication(sys.argv)
    # w = Widget()
    w = Root()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()