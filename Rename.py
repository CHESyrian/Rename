import sys
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
from os import getcwd

class Rename_App(QWidget):
    def __init__(self):
        super().__init__()
        self.dirs_list = []
        self.ent_style = """font : 24px #fff;
                            color : white;
                            border-bottom : 2px solid white;
                            border-radius : 5%;
                            background-color : transparent;
                            padding : 0px 8px -20px 8px;"""

        self.btn_style = """font : 22px #fff;
                            color : white;
                            border : 2px outset silver;
                            border-radius : 20%;
                            background-color : transparent;
                            padding : 8px;"""

        self.form_style = """background-color : black;"""
        self.pxm = QPixmap(getcwd() + '\\owner.png')
        self.Main_UI()

    def Main_UI(self):
        self.resize(420, 360)
        self.setGeometry(60, 60, 240+self.pxm.width(), 140+self.pxm.height())
        self.setMaximumSize(280+self.pxm.width(), 140+self.pxm.height())
        self.setMinimumSize(280+self.pxm.width(), 140+self.pxm.height())
        self.setWindowTitle("Rename")
        self.setStyleSheet(self.form_style)

        self.lbl_1 = QLabel(self)
        self.lbl_1.setPixmap(self.pxm)

        self.btn_1 = QPushButton(self)
        self.btn_1.setGeometry(self.pxm.width(), 40, 180, 40)
        self.btn_1.setText("Choose Folder")
        self.btn_1.clicked.connect(self.fdg_func)
        self.btn_1.setStyleSheet(self.btn_style)

        self.btn_2 = QPushButton(self)
        self.btn_2.setGeometry(self.pxm.width(), 180, 180, 40)
        self.btn_2.setText("Rename")
        self.btn_2.clicked.connect(self.Rename)
        self.btn_2.setStyleSheet(self.btn_style)

        self.ent_1 = QLineEdit(self)
        self.ent_1.setGeometry(40, self.pxm.height(), 320, 60)
        self.ent_1.setStyleSheet(self.ent_style)
        self.ent_1.setPlaceholderText('New Name')

        self.ent_2 = QLineEdit(self)
        self.ent_2.setGeometry(self.pxm.width()-80, self.pxm.height(), 320, 60)
        self.ent_2.setStyleSheet(self.ent_style)
        self.ent_2.setPlaceholderText('.Extension')
        self.show()


    def fdg_func(self):
        while True:
            self.fdg = QFileDialog.getExistingDirectory(self, "choose directories, or cancel to stop", '/')
            self.file_path = self.fdg.replace('\\', '/')
            if not self.file_path:
                break
            self.dirs_list.append(self.file_path)
        self.fdg_2 = QFileDialog.getExistingDirectory(self, 'choose folder to save outputs..', '/')
        self.save_path = self.fdg.replace('\\', '/')
        self.save_dir = self.fdg_2

    def Rename(self):
        import os
        self.num       = 1
        self.new_name  = self.ent_1.text()
        self.extension = self.ent_2.text()
        self.new_dir   =self.save_dir
        for path in self.dirs_list:
            for file in os.listdir(path):
                self.src = path + '/' + file
                self.dst = self.new_dir + '/' + self.new_name + str(self.num) + self.extension
                os.rename(src=self.src, dst=self.dst)
                self.num += 1
        self.ent_1.clear()
        self.ent_2.clear()

if __name__ == "__main__":
    APP = QApplication(sys.argv)
    obj = Rename_App()
    sys.exit(APP.exec_())
