from sys import argv, exit
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
from os import getcwd

class Rename_App(object):
    def __init__(self):
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

    def Main_UI(self, Form):
        Form.resize(420, 360)
        Form.setGeometry(60, 60, 240+self.pxm.width(), 140+self.pxm.height())
        Form.setMaximumSize(280+self.pxm.width(), 140+self.pxm.height())
        Form.setMinimumSize(280+self.pxm.width(), 140+self.pxm.height())
        Form.setWindowTitle("Rename")
        Form.setStyleSheet(self.form_style)

        self.lbl_1 = QLabel(Form)
        self.lbl_1.setPixmap(self.pxm)

        self.btn_1 = QPushButton(Form)
        self.btn_1.setGeometry(self.pxm.width(), 40, 180, 40)
        self.btn_1.setText("Choose Folder")
        self.btn_1.clicked.connect(self.fdg_func)
        self.btn_1.setStyleSheet(self.btn_style)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setGeometry(self.pxm.width(), 180, 180, 40)
        self.btn_2.setText("Rename")
        self.btn_2.clicked.connect(self.Rename)
        self.btn_2.setStyleSheet(self.btn_style)

        self.ent_1 = QLineEdit(Form)
        self.ent_1.setGeometry(40, self.pxm.height(), 320, 60)
        self.ent_1.setStyleSheet(self.ent_style)
        self.ent_1.setPlaceholderText('New Name')

        self.ent_2 = QLineEdit(Form)
        self.ent_2.setGeometry(self.pxm.width()-80, self.pxm.height(), 320, 60)
        self.ent_2.setStyleSheet(self.ent_style)
        self.ent_2.setPlaceholderText('.Extension')


    def fdg_func(self):
        w = QWidget()
        while True:
            self.fdg = QFileDialog.getExistingDirectory(w, "choose directories-cancel to stop", '/')
            self.file_path = self.fdg.replace('\\', '/')
            if not self.file_path:
                break
            self.dirs_list.append(self.file_path)
        self.fdg_2 = QFileDialog.getExistingDirectory(w, 'choose folder to save outputs..', '/')
        self.save_path = self.fdg.replace('\\', '/')
        self.save_dir = self.fdg_2

    def Rename(self):
        import os
        self.num = 1
        self.new_name = self.ent_1.text()
        self.extension = self.ent_2.text()
        self.new_dir =self.save_dir
        for path in self.dirs_list:
            for file in os.listdir(path):
                self.src = path + '/' + file
                self.dst = self.new_dir + '/' + self.new_name + str(self.num) + self.extension
                os.rename(src=self.src, dst=self.dst)
                self.num += 1
        self.ent_1.clear()
        self.ent_2.clear()

if __name__ == "__main__":
    APP = QApplication(argv)
    Form = QWidget()
    obj = Rename_App()
    obj.Main_UI(Form)
    Form.show()
    exit(APP.exec_())
