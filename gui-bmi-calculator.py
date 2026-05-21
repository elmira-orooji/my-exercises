# imports and global variables
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys
from PyQt6.QtCore import QSize, Qt
app = QApplication(sys.argv)

# logic
def calculate_bmi_and_result():
    result = None

    weight = float(weight_entry.text())
    height = float(height_entry.text())

    bmi = weight // (height * 2)

    if( 18.5 <= bmi < 25):
        result = "Normal"
    
    elif( 25 <=  bmi < 30):
       result = "Over weight"
    
    elif( 30 <= bmi < 35):
       result  = "Obese"
    
    elif(bmi < 18.5):
        result = "Underweight"

    else:
        result = "Extremely obese"

    result_label.setText(f"Result : {result}")

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
calculate_button = QPushButton(text="Calculate BMI")
calculate_button.clicked.connect(calculate_bmi_and_result)
result_label = QLabel("Result:")
layot.addWidget(height_label)
layot.addWidget(height_entry)
layot.addWidget(weight_label)
layot.addWidget(weight_entry)
layot.addWidget(calculate_button)
layot.addWidget(result_label)

widget.setLayout(layot)
window.setCentralWidget(widget)
window.show()


# running the application
app.exec()