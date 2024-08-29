# Developer: Navi Rosca - Ivan Christopher Rosca
# Email: nines.kyu.jp@gmail.com
# Github: Nines九 @Nines-kyu

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
