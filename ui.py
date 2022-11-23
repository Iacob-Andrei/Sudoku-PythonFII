import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class UiSudokuClass(object):
    def setup_ui(self, SudokuClass):
        SudokuClass.setObjectName("SudokuClass")
        SudokuClass.resize(550, 650)
        SudokuClass.setLayoutDirection(QtCore.Qt.RightToLeft)
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

        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # item.setBackground(brush)
        # self.Table.setItem(2, 2, item)

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

        self.predefined_options(SudokuClass)
        QtCore.QMetaObject.connectSlotsByName(SudokuClass)

    def predefined_options(self, SudokuClass):
        _translate = QtCore.QCoreApplication.translate
        SudokuClass.setWindowTitle(_translate("SudokuClass", "Sudoku"))
        __sortingEnabled = self.Table.isSortingEnabled()
        self.Table.setSortingEnabled(False)
        self.Table.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.Table_2.isSortingEnabled()
        self.Table_2.setSortingEnabled(False)

        for index in range(0, 9):
            item = self.Table_2.item(0, index)
            item.setText(_translate("SudokuClass", f"{index + 1}"))
        item = self.Table_2.item(0, 9)
        item.setText(_translate("SudokuClass", "-"))

        self.Table_2.setSortingEnabled(__sortingEnabled)

    def predefined_values(self, SudokuClass):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sudoku_ui = QtWidgets.QMainWindow()
    ui = UiSudokuClass()
    ui.setup_ui(sudoku_ui)
    sudoku_ui.show()
    sys.exit(app.exec_())
