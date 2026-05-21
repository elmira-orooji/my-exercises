# imports and global variables
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys
from PyQt6.QtCore import QSize, Qt
app = QApplication(sys.argv)

# logic

# ui design 

window = QMainWindow()
window.setWindowTitle("GUI BMI CALCULATOR")
window.setFixedSize(QSize(400, 300))
widget = QWidget()
layot = QVBoxLayout()


height_label = QLabel("Height (m):")
height_entry = QLineEdit()

weight_label = QLabel("Weight (kg):")
weight_entry = QLineEdit()

result_label = QLabel("Result:")

calculate_button = QPushButton(text="Calculate BMI")


layot.addWidget(height_label)
layot.addWidget(height_entry)

layot.addWidget(weight_label)
layot.addWidget(weight_entry)

layot.addWidget(result_label)

layot.addWidget(calculate_button)

widget.setLayout(layot)
window.setCentralWidget(widget)
window.show()


# running the application
app.exec()