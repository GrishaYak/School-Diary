import sys
import csv
import sqlite3
import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QButtonGroup, QTextEdit, QMdiSubWindow, \
    QMdiArea
from PyQt6.QtGui import QIcon

import additionalWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(650, 250, 400, 640)
        self.setWindowTitle('Дневник')

        self.search_bar = QLineEdit(self)
        self.search_bar.setGeometry(50, 10, 337, 30)
        self.search_bar.textChanged.connect(self.search)

        self.settings_btn = QPushButton(self)
        self.settings_btn.setGeometry(5, 10, 30, 30)
        self.settings_btn.setIcon(QIcon('files/settings_icon.png'))
        self.settings_btn.clicked.connect(self.open_settings)

        self.btn_group = QButtonGroup(self)
        self.create_subject_buttons()
        self.btn_group.buttonClicked.connect(self.add_sub_window)

        self.mdi = QMdiArea()
        self.mdi.setGeometry(1055, 200, 400, 800)
        self.slots = []
        self.show()

    def add_sub_window(self, btn):
        """Добавляет окно с домашним заданием по выбранному предмету"""
        sub = QMdiSubWindow()
        sub.setGeometry(0, 0, 400, 200)
        sub.setWindowTitle(btn.text())
        txt = QTextEdit(sub)
        txt.setGeometry(1, 30, 398, 168)
        txt.textChanged.connect(self.save_homework)
        self.slots.append(sub)
        self.mdi.addSubWindow(sub)
        self.mdi.show()
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        text = cur.execute('''select homework from homework where subject == ?''',
                           (btn.text(),)).fetchone()
        txt.setText(text[0])
        con.close()
        sub.show()

    def save_homework(self):
        """Сохраняет домашнее задание в базу данных"""
        subject = self.sender().parent().windowTitle()
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('''update homework set homework = ? where subject = ?''',
                    (self.sender().toPlainText(), subject)).fetchall()
        con.commit()
        con.close()

    def create_subject_buttons(self):
        """Создаёт по кнопке для каждого предмета"""
        with open('files/subjects.csv', encoding='utf8') as f:
            r = csv.reader(f)
            for el in r:
                data = el
        #    выше я записал в пременную data все школьные предметы, т.к. они записаны в csv в одну строку
        col = 0
        indent = 50
        for subject in data:
            btn = QPushButton(self)
            btn.setText(subject)
            btn.setGeometry(8 + col * 128, indent, 123, 60)
            col += 1
            if col == 3:
                col = 0
                indent += 65
            self.btn_group.addButton(btn)

    def search(self):
        """Прячет все предметы, в названиях которых нет нужной подстроки"""
        expr = re.compile(f".*{self.search_bar.text().lower()}.*")
        for btn in self.btn_group.buttons():
            if expr.match(btn.text().lower()) is None:
                btn.setHidden(True)
            else:
                btn.setHidden(False)

    def open_settings(self):
        """Открывает окно с настройками"""
        self.close()
        self.smt = additionalWindow.ChooseTheSubjects()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())
