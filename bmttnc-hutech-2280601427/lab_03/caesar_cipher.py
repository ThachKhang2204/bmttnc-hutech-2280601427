import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối các nút với hàm xử lý
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):  # Đổi từ "ecnrypt" -> "encrypt"
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plainTextEdit.toPlainText(),
            "key": self.ui.textEdit.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_2.setPlainText(data['encrypted_message'])
                QMessageBox.information(self, "Success", "Encryption Successful")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"API Error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_2.toPlainText(),
            "key": self.ui.textEdit.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data['decrypted_message'])
                QMessageBox.information(self, "Success", "Decryption Successful")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"API Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
