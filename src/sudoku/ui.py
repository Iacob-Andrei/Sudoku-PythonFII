import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

import table


def cancel_popup():
    sys.exit()


class UiSudokuClass(object):
    def __init__(self, SudokuClass, max_time, difficulty):
        """
        constructor
        :param max_time: of the game
        :param difficulty: of the game
        """
        self.instance = table.generate_instance(difficulty)
        self.to_place = None
        self.count = max_time
        self.start = True

        self.generate_ui(SudokuClass)
        self.predefined_options()
        self.default_instance()

        QtCore.QMetaObject.connectSlotsByName(SudokuClass)

    def generate_ui(self, SudokuClass):
        """
        generating the UI components
        created using QTDesigner
        """
        SudokuClass.setObjectName("SudokuClass")
        SudokuClass.setFixedSize(550, 650)
        SudokuClass.setLayoutDirection(QtCore.Qt.RightToLeft)
        SudokuClass.setWindowTitle("Sudoku")
        SudokuClass.setWindowIcon(QtGui.QIcon('../../resources/logo.png'))
        self.centralWidget = QtWidgets.QWidget(SudokuClass)
        self.centralWidget.setObjectName("centralWidget")

        self.Table = QtWidgets.QTableWidget(self.centralWidget)
        self.Table.setGeometry(QtCore.QRect(50, 30, 450, 450))

        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Table.setFont(font)
        self.Table.setMouseTracking(False)
        self.Table.setAcceptDrops(False)
        self.Table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Table.setAutoScrollMargin(16)
        self.Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Table.setTextElideMode(QtCore.Qt.ElideNone)
        self.Table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.Table.setGridStyle(QtCore.Qt.DashDotLine)
        self.Table.setWordWrap(True)
        self.Table.setRowCount(9)
        self.Table.setColumnCount(9)
        self.Table.setObjectName("Table")

        for line in range(0, 9):
            for column in range(0, 9):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Table.setItem(line, column, item)

        self.Table.horizontalHeader().setVisible(False)
        self.Table.horizontalHeader().setDefaultSectionSize(50)
        self.Table.horizontalHeader().setHighlightSections(False)
        self.Table.horizontalHeader().setMinimumSectionSize(10)
        self.Table.verticalHeader().setVisible(False)
        self.Table.verticalHeader().setDefaultSectionSize(50)
        self.Table.verticalHeader().setHighlightSections(False)
        self.Table.verticalHeader().setMinimumSectionSize(10)
        self.Table.selectionModel().selectionChanged.connect(self.handle_select_matrix)

        lines_coordonates = [(50, 170, 451, 21), (50, 320, 451, 21), (180, 30, 41, 451), (330, 30, 41, 451)]
        for index in range(0, 4):
            self.line = QtWidgets.QFrame(self.centralWidget)
            self.line.setGeometry(QtCore.QRect(lines_coordonates[index][0], lines_coordonates[index][1],
                                               lines_coordonates[index][2], lines_coordonates[index][3]))
            self.line.setFrameShadow(QtWidgets.QFrame.Plain)
            self.line.setLineWidth(3)
            if index > 1:
                self.line.setFrameShape(QtWidgets.QFrame.VLine)
            else:
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setObjectName(f"line_{index}")

        self.Table_2 = QtWidgets.QTableWidget(self.centralWidget)
        self.Table_2.setGeometry(QtCore.QRect(20, 510, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Table_2.setFont(font)
        self.Table_2.setMouseTracking(False)
        self.Table_2.setAcceptDrops(False)
        self.Table_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Table_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Table_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Table_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Table_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.Table_2.setGridStyle(QtCore.Qt.DashDotLine)
        self.Table_2.setWordWrap(True)
        self.Table_2.setRowCount(1)
        self.Table_2.setColumnCount(10)
        self.Table_2.setObjectName("Table_2")

        for index in range(0, 10):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.Table_2.setItem(0, index, item)

        self.Table_2.horizontalHeader().setVisible(False)
        self.Table_2.horizontalHeader().setDefaultSectionSize(50)
        self.Table_2.horizontalHeader().setHighlightSections(False)
        self.Table_2.horizontalHeader().setMinimumSectionSize(10)
        self.Table_2.verticalHeader().setVisible(False)
        self.Table_2.verticalHeader().setDefaultSectionSize(50)
        self.Table_2.verticalHeader().setHighlightSections(False)
        self.Table_2.verticalHeader().setMinimumSectionSize(10)
        SudokuClass.setCentralWidget(self.centralWidget)
        self.Table_2.selectionModel().selectionChanged.connect(self.handle_select_numbers)

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(220, 580, 100, 35)
        self.label.setStyleSheet("border : 3px solid black")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        timer = QtCore.QTimer(self.centralWidget)
        timer.timeout.connect(self.show_time)
        timer.start(100)

    def show_time(self):
        """
        updating the timer every 1 second
        calls the popup to show when timer is up
        :return: None
        """
        if self.start:
            self.count -= 1

            if self.count == 0:
                self.start = False
                self.show_popup('Time is up')

        if self.start:
            text = str(self.count / 10) + " s"
            self.label.setText(text)

    def default_instance(self):
        """
        instantiate the initial matrix
        :return: None
        """
        for line in range(0, 9):
            for column in range(0, 9):
                nr = self.instance[line * 9 + column]
                if nr != '0':
                    item = self.Table.item(line, column)
                    item.setText(nr)
                    brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    item.setBackground(brush)

    def predefined_options(self):
        """
        prefill the possible options
        :return: None
        """
        for column in range(0, 9):
            item = self.Table_2.item(0, column)
            item.setText(f"{column + 1}")

        item = self.Table_2.item(0, 9)
        item.setText('-')

    def handle_select_matrix(self, selected):
        """
        handles the selection of a box
        changes the value of the box with the selected pre-option
        if matrix becomes full, it checks if it is valid solution
        :param selected: the selected box from the matrix
        :return: None
        """
        if self.to_place is None:
            return

        row = column = 0
        for ix in selected.indexes():
            row = ix.row()
            column = ix.column()

        if self.instance[row * 9 + column] != '0':
            return

        item = self.Table.item(row, column)
        item.setText(self.to_place)

        self.get_matrix_state()
        if table.verify_final_instance(self.matrix):
            self.show_popup("Congrats")
        self.Table.clearSelection()

    def handle_select_numbers(self, selected):
        """
        handles the selection of a number
        :param selected: selected box number
        :return:
        """
        index = 0
        for ix in selected.indexes():
            index = ix.column()

        if index == 9:
            self.to_place = ''
        else:
            item = self.Table_2.item(0, index)
            self.to_place = item.text()

    def get_matrix_state(self):
        """
        convert the data from UI table into matrix
        :return: None
        """
        self.matrix = []
        for line in range(0, 9):
            for column in range(0, 9):
                item = self.Table.item(line, column)
                self.matrix.append(item.text())
        self.matrix = np.array(self.matrix).reshape((9, 9))

    def show_popup(self, text):
        """
        create and show the popup with a specified message
        :param text: that will be shown in the popup
        :return: None
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(text)
        msg.setWindowIcon(QtGui.QIcon('../../resources/logo.png'))
        if text == "Congrats":
            msg.setText("Congrats, you finished the game!")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        else:
            msg.setText("Unfortunately, the time is up!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.Cancel)

        msg.buttonClicked.connect(cancel_popup)
        msg.exec_()
