# import utils.dataUtils as dataU

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtWidgets, QtGui
import numpy as np


class Root(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self._main_defaults()

        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setTabShape(QtWidgets.QTabWidget.Triangular)

        self.dashboard = QtWidgets.QFrame()
        self.tabs.addTab(self.dashboard, "Dashboard")
        self.tabs.setTabToolTip(0, "This is a dashboard.")

        self.main = QtWidgets.QWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.addTab(self.main, "Data Table")
        self._h_layout = QtWidgets.QHBoxLayout()
        self._v_layout = QtWidgets.QVBoxLayout()
        self.main.setLayout(self._v_layout)
        self._v_layout.addLayout(self._h_layout)
        self._v_layout.setAlignment(QtCore.Qt.AlignTop)
        self.btn = QtWidgets.QPushButton('test')
        self._h_layout.addWidget(self.btn)

        # Setup model and data.
        # self.model = QtGui.QStandardItemModel()
        # self.header_labels = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8']
        self.num_of_cols = 10
        self.num_of_rows = 35
        # Generate header labels via list comprehension.
        self.header_labels = [('Column %d' % (i + 1)) for i in range(self.num_of_cols)]

        self.table = DataTable()
        self.table.setMinimumSize(600, 500)
        self.table.setColumnCount(self.num_of_cols)
        self.table.setHorizontalHeaderLabels(self.header_labels)
        self.table.setRowCount(self.num_of_rows)

        self.data = Data(self.num_of_cols, self.num_of_rows)
        self._populate_data()

        self._v_layout.addWidget(self.table)

        self.show()

    def _main_defaults(self):
        """"""
        self.setWindowTitle('Sandbox')
        menu = self.menuBar()
        file_menu = menu.addMenu('File')

        status = self.statusBar()
        status.showMessage('Status Bar')

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMaximumHeight(500)

    def _populate_data(self):
        """"""
        for row_num, row_data in enumerate(self.data.data_by_row):
            for col_num, col_data in enumerate(row_data):
                cell_datum = QtWidgets.QTableWidgetItem(str(col_data))
                cell_datum.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row_num, col_num, cell_datum)


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
        # self.data = np.zeros((columns, rows))
        self.data = np.random.randint(100, size=(columns, rows))
        # Convert numpy array to nested list.
        self.data_list = self.data.tolist()
        # Transpose matrix from columns to rows.
        self.data_by_row = list(zip(*self.data_list))

    def transpose_by_numpy(self):
        data_nparray = self.data
        data_nparray_t = data_nparray.T
        data_nparray_str = np.array2string(data_nparray_t)


class DataTable(QtWidgets.QTableWidget):
    def __init__(self):
        super(DataTable, self).__init__()
        self.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)


class Table(QtWidgets.QTableView):
    def __init__(self, model):
        super(Table, self).__init__()
        self.setModel(model)
        self.frozen_table = QtWidgets.QTableView(self)
        self.init_frozen_table()
        #
        self.horizontalHeader().sectionResized.connect(self.updateSectionWidth)
        self.verticalHeader().sectionResized.connect(self.updateSectionHeight)
        self.frozen_table.verticalScrollBar().valueChanged.connect(
            self.verticalScrollBar().setValue)
        self.verticalScrollBar().valueChanged.connect(
            self.frozen_table.verticalScrollBar().setValue)

    def init_frozen_table(self):
        # Assign model to be the same as the other table's model.
        self.frozen_table.setModel(self.model())
        # Hide frozen table's vertical labels.
        self.frozen_table.verticalHeader().hide()
        #
        self.frozen_table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Fixed)
        # Position main table under frozen table.
        self.viewport().stackUnder(self.frozen_table)
        # Style frozen table to appear unique from main table.
        self.frozen_table.setStyleSheet('''
                    QTableView { border: none;
                                 background-color: #8EDE21;
                                 selection-background-color: #999;
                    }''')
        #
        self.frozen_table.setFocusPolicy(QtCore.Qt.NoFocus)
        #
        self.frozen_table.setSelectionModel(self.selectionModel())
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

    def updateSectionWidth(self, logicalIndex, oldSize, newSize):
        if self.logicalIndex == 0:
            self.frozen_table.setColumnWidth(0, newSize)
            self.update_frozen_table_geometry()

    def updateSectionHeight(self, logicalIndex, oldSize, newSize):
        self.frozen_table.setRowHeight(logicalIndex, newSize)

    def resizeEvent(self, event):
        """Resize frozen table alongside main window/table resize."""
        super(Table, self).resizeEvent(event)
        self.update_frozen_table_geometry()

    def moveCursor(self, cursorAction, modifiers):
        current = super(Table, self).moveCursor(cursorAction, modifiers)
        if (cursorAction == self.MoveLeft and
                self.current.column() > 0 and
                self.visualRect(current).topLeft().x() <
                    self.frozen_table.columnWidth(0)):
            newValue = (self.horizontalScrollBar().value() +
                        self.visualRect(current).topLeft().x() -
                        self.frozen_table.columnWidth(0))
            self.horizontalScrollBar().setValue(newValue)
        return current

    def scrollTo(self, index, hint):
        if index.column() > 0:
            super(Table, self).scrollTo(index, hint)

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