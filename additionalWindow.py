import io
import sys
import csv
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import json
from files.ui_config import template_for_choosing
from files.errors import LenError, SizeError
import mainWindow


class ChooseTheSubjects(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_for_choosing)
        uic.loadUi(f, self)
        self.LenErrorLabel.setHidden(True)
        self.SizeErrorLabel.setHidden(True)
        self.ReadyButton.clicked.connect(self.run)
        self.RemoveAll.clicked.connect(self.remove_all)
        self.SelectAll.clicked.connect(self.select_all)

        self.subjects = set()
        self.recollector()
        self.show()

    def recollector(self):
        """Открывает форму на том этапе, на котором она была сохранена ранее"""
        with open('files/temp.json', encoding='utf8') as f:
            data = json.load(f)
            for btn in self.SubjectButtons.buttons():
                btn.setChecked(data['status'][btn.objectName()])
            self.textEdit.setText(data['text'])

    def save_temp(self):
        """Сохраняет форму, чтобы в следующий раз она открылась с того же места"""
        status = {}
        for btn in self.SubjectButtons.buttons():
            status[btn.objectName()] = btn.isChecked()
        with open('files/temp.json', 'w', encoding='utf8') as f:
            text = self.textEdit.toPlainText()
            json.dump({'status': status, 'text': text}, f, indent=4, ensure_ascii=False)

    def select_all(self):
        """Ставит галочку на все предложенные предметы"""
        for btn in self.SubjectButtons.buttons():
            btn.setChecked(True)

    def remove_all(self):
        """Убирает галочку на всех предложенных предметах"""
        for btn in self.SubjectButtons.buttons():
            btn.setChecked(False)

    def update_data(self):
        """Сохраняет список выбранных предметов и создаёт новые записи в базе данных с домашкой"""
        self.subjects = sorted(self.subjects)
        # Записываем все предметы во внешнюю память
        with open('files/subjects.csv', 'w', encoding='utf8', newline='') as f:
            csv.writer(f).writerow(self.subjects)

        # Обновляем главный csv-файли с дз
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()

        cur.execute('''
        create table if not exists homework (
        subject text primary key,
        homework text)
        ''')
        if self.subjects:
            if len(self.subjects) == 1:
                request = f"delete from homework where subject != '{self.subjects[0]}'"
            else:
                request = f'delete from homework where subject not in {tuple(self.subjects)}'
            cur.execute(request)
        for el in self.subjects:
            if cur.execute('''SELECT * FROM homework WHERE subject = ?''', (el,)).fetchall():
                continue
            cur.execute('''INSERT INTO homework (subject, homework)
                        VALUES (?, ?)''', (el, 'ничего'))

        connection.commit()
        connection.close()

    def check_the_correctness(self):
        """Проверяет корректность данных, введённых пользователем"""
        self.SizeErrorLabel.setHidden(True)
        self.LenErrorLabel.setHidden(True)

        for btn in self.SubjectButtons.buttons():
            if btn.isChecked():
                self.subjects.add(btn.text())
        num_of_checked_boxes = len(self.subjects)
        cnt = 0
        try:
            text = self.textEdit.toPlainText()
            for line in text.split('\n'):
                if line:
                    cnt += 1
                    if cnt > 27 - num_of_checked_boxes:
                        raise SizeError
                    if len(line) > 17:
                        raise LenError
                    self.subjects.add(line)
        except SizeError:
            self.SizeErrorLabel.setHidden(False)
            self.subjects.clear()
            return 1
        except LenError:
            self.LenErrorLabel.setHidden(False)
            self.subjects.clear()
            return 1
        return 0

    def run(self):
        """Запускает ряд функций, нужных для сохранения настроек"""
        code = self.check_the_correctness()
        if code:
            return
        self.update_data()
        self.save_temp()
        self.open_main_window()

    def open_main_window(self):
        """Открывает главное окно дневника"""
        self.close()
        self.w = mainWindow.MainWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ChooseTheSubjects()
    sys.exit(app.exec())
