from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QFont
import webbrowser
import sys
import time

def abrir_youtube():
    email = en_email.text()
    password = en_senha.text()

    if email == "teste@gmail.com" and password == "123456":
        webbrowser.open("https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0")
        window.close()
        time.sleep(0.3)
    else:
        QMessageBox.critical(window, "Error", "Invalid email or password")

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Portal de alunos")
window.setGeometry(610, 153, 490, 560)

img_fundo = QPixmap("imagens\\fundo.png")
Lab_fundo = QLabel(window)
Lab_fundo.setPixmap(img_fundo)
Lab_fundo.setGeometry(0, 0, 490, 560)

en_email = QLineEdit(window)
en_email.setGeometry(32, 155, 425, 85)
en_email.setAlignment(Qt.AlignCenter)
en_email.setFont(QFont("Calibri", 15))

en_senha = QLineEdit(window)
en_senha.setGeometry(32, 320, 425, 85)
en_senha.setEchoMode(QLineEdit.Password)
en_senha.setAlignment(Qt.AlignCenter)
en_senha.setFont(QFont("Calibri", 15))

bt_entrar = QPushButton(window)
bt_entrar.setGeometry(186, 489, 118, 64)
bt_entrar.setIcon(QPixmap("imagens\\LOGIN.png"))
bt_entrar.clicked.connect(abrir_youtube)

window.show()
sys.exit(app.exec_())