import sys
# Libraries
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import *


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        # New WebView
        self.browser = QWebEngineView()
        # Set URL
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)

        self.showMaximized()
        # ToolBar
        navbar = QToolBar()
        self.addToolBar(navbar)
        # Back button
        prevBtn = QAction('Back', self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)
        # Forward Button
        nextBtn = QAction('Forward', self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)
        # Refresh Button
        refreshBtn = QAction('Refresh', self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)
        # Home Button
        homeBtn = QAction('Home', self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
        # Search Bar
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)

    def home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, url):
        self.searchBar.setText(url.toString())


MyApp = QApplication(sys.argv)


# App Name
QApplication.setApplicationName('Browser-py')

# New window
window = Window()

# Execute main app.
MyApp.exec_()
