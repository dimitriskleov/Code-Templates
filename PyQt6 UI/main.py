from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtCore import QObject, pyqtSlot, QUrl
import sys
import os

# Backend logic for handling JS calls
class Backend(QObject):
    @pyqtSlot()
    def buttonClicked(self):
        print("Button clicked! Executing Python function.")

# Main application window
class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTML-Python Integration")

        # Create WebEngineView (embedded browser)
        self.browser = QWebEngineView()

        # Set up communication channel
        self.channel = QWebChannel()
        self.backend = Backend()
        self.channel.registerObject("backend", self.backend)

        # Load external HTML file
        html_file_path = os.path.abspath("loading.html")  # Ensure absolute path
        self.browser.setUrl(QUrl.fromLocalFile(html_file_path))
        self.browser.page().setWebChannel(self.channel)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebWindow()
    window.show()
    sys.exit(app.exec())
