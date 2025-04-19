"""Entry point for the Bibb Application"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel


def main():
    """Demo application."""
    app = QApplication(sys.argv)
    label = QLabel("Welcome to Bibb!", alignment=Qt.Alignment.AlignCenter)
    label.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
