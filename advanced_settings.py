import sys
from PyQt4 import QtCore, QtGui, uic

move_up = 2
move_down = 2
move_left = 2
move_right = 2
joi1_up = 3
joi1_down = 3
joi2_up = 3
joi2_down = 3
joi3_up = 3
joi3_down = 3
base_clock = 3
base_anti_clock = 3

qtCreatorFile = "advanced_settings.ui"  # Enter file here.
Ui_MainWindow1, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)
        self.def_button.clicked.connect(self.old_values)
        self.set_button.clicked.connect(self.new_values)

    def old_values(self):
        move_up = 2
        move_down = 2
        move_left = 2
        move_right = 2
        joi1_up = 3
        joi1_down = 3
        joi2_up = 3
        joi2_down = 3
        joi3_up = 3
        joi3_down = 3
        base_clock = 3
        base_anti_clock = 3
        self.rover_up.setValue(move_up)
        self.rover_down.setValue(move_down)
        self.rover_left.setValue(move_left)
        self.rover_right.setValue(move_right)
        self.Joint1_up.setValue(joi1_up)
        self.Joint1_down.setValue(joi1_down)
        self.Joint2_up.setValue(joi2_up)
        self.Joint2_down.setValue(joi2_down)
        self.Joint3_up.setValue(joi3_up)
        self.Joint3_down.setValue(joi3_down)
        self.Base_clockwise.setValue(base_clock)
        self.Base_anti_clockwise.setValue(base_anti_clock)

    def new_values(self):
        move_up = self.rover_up.value()
        move_down = self.rover_down.value()
        move_left = self.rover_left.value()
        move_right = self.rover_right.value()
        joi1_up = self.Joint1_up.value()
        joi1_down = self.Joint1_down.value()
        joi2_up = self.Joint2_up.value()
        joi2_down = self.Joint2_down.value()
        joi3_up = self.Joint3_up.value()
        joi3_down = self.Joint3_down.value()
        base_clock = self.Base_clockwise.value()
        base_anti_clock = self.Base_anti_clockwise.value()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
