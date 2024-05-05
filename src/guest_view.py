from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout

class GuestView(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Guest View")
        
        label = QLabel("Welcome, Guest!")
        button = QPushButton("Continue as Guest")
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
    
        self.setLayout(layout)
