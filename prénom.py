import sys
import random
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget


class AnimatedRandomNameApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nom Aléatoire avec Animation")
        self.layout = QVBoxLayout()
        self.names = {
            1: "Zishaan",
            2: "Mattis",
            3: "Baqer",
            4: "Romain",
            5: "Marco",
            6: "Joshua",
        }
        self.label = QLabel("Cliquez pour commencer !", alignment=Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 32, QFont.Weight.Bold))
        self.layout.addWidget(self.label)
        self.button = QPushButton("Tirer un prénom")
        self.button.setFont(QFont("Arial", 16))
        self.button.clicked.connect(self.start_animation)
        self.layout.addWidget(self.button)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.animation_steps = 30
        self.current_step = 0
        self.setLayout(self.layout)

    def start_animation(self):
        self.current_step = 0
        self.button.setEnabled(False) 
        self.timer.start(50)  

    def update_animation(self):
        if self.current_step < self.animation_steps:
            number = random.randint(1, 6)
            name = self.names[number]
            self.label.setText(f"{number} : {name}")
            self.current_step += 1
        else:
            self.timer.stop()
            self.button.setEnabled(True)
            self.final_result()

    def final_result(self):
        number = random.randint(1, 6)
        name = self.names[number]
        self.label.setText(f"🎉 {number} : {name} 🎉")
        self.label.setFont(QFont("Arial", 40, QFont.Weight.Bold))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimatedRandomNameApp()
    window.resize(400, 300) 
    window.show()
    sys.exit(app.exec())
