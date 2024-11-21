import sys
from PyQt6.QtWidgets import QApplication
import csv
from additionalWindow import ChooseTheSubjects
from mainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('files/subjects.csv', encoding='utf8') as f:
        r = csv.reader(f)
        a = []
        for el in r:
            a = el
    if a:
        w = MainWindow()
    else:
        w = ChooseTheSubjects()
    sys.exit(app.exec())
