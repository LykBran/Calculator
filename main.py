from PySide6.QtWidgets import QApplication
from form import Form
import sys

app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec())
