from PySide6.QtCore import QObject, Signal, Slot, QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QApplication
import sys

# Pythonオブジェクト（ハンドラ）を作成
class Handler(QObject):
    linkClicked = Signal(str)

    @Slot(str)
    def handleLinkClick(self, url):
        print(f"Link clicked: {url}")
        self.linkClicked.emit(url)

# アプリケーションのセットアップ
app = QApplication(sys.argv)
view = QWebEngineView()

# QWebChannelのセットアップ
handler = Handler()
channel = QWebChannel()
channel.registerObject("handler", handler)
view.page().setWebChannel(channel)

# HTMLファイルをロード
view.setUrl(QUrl.fromLocalFile("three.html"))  # HTMLファイルへのパスを指定

view.show()
sys.exit(app.exec())
