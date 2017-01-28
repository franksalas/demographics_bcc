from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from ui import demo_ui


class Application(QDialog, demo_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.buttonLoad.clicked.connect(self.setOpenFileName)
        self.buttonConvert.clicked.connect(self.setExistingDirectory)
        self.buttonConvert.setEnabled(False)
        self.buttonExit.clicked.connect(quit)

    def setOpenFileName(self):
        options = QFileDialog.Options()
        fileName = QFileDialog.getOpenFileName(self,
                                               "Load File",
                                               self.messageLabel_2.text(),
                                               "All Files (*);;Text Files (*.txt)", options)
        if fileName:
            self.messageLabel.setText("File Loaded")
            self.messageLabel_2.setText(fileName)
            self.messageLabel.setText("File Loaded")
            self.buttonConvert.setEnabled(True)

    def load(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        self.file = open(name, 'r')
        # print(name)
        print("type of file: {}".format(self.file))

        if name == None:
            self.messageLabel.setText("Error")
        else:
            self.messageLabel.setText("File Loaded")
            self.buttonConvert.setEnabled(True)

    def convert(self):
        print("inside convert:{}".format(self.file))
        savelocation = QFileDialog.getSaveFileNameAndFilter(self, "save Location")

    def setExistingDirectory(self):
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self,
                                                     "Select Save Folder",
                                                     self.messageLabel.text(), options)
        if directory:
            self.messageLabel.setText(directory)

        print(directory)


app = QApplication(sys.argv)
dialog = Application()
dialog.show()
app.exec_()
