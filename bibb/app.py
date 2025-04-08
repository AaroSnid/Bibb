"""The starting point for the Bibb app."""

import sys

from PyQt6.QtWidgets import QApplication  # pylint: disable = no-name-in-module
from PyQt6.QtWidgets import QLabel  # pylint: disable = no-name-in-module
from PyQt6.QtWidgets import QWidget  # pylint: disable = no-name-in-module


def main():
    """Set up and run the app."""
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Bibb")
    window.setGeometry(100, 100, 280, 80)
    test_message = QLabel("<h1>Hello, welcome to Bibb!</h1>", parent=window)
    test_message.move(60, 15)
    window.show()
    sys.exit(app.exec())


if __name__ == main():
    main()
