from __future__ import division
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
# from PyQt5.QtWebKit import QWebView
from PyQt5.QtWebEngineWidgets  import QWebEngineView

from segyviewlib import resource_html


class HelpWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent, Qt.WindowStaysOnTopHint | Qt.Window)
        self.setVisible(False)

        self._view_help = QWebEngineView(self)
        self._view_help.load(resource_html("helppage.html"))
        self._view_help.show()

        f_layout = QHBoxLayout()
        f_layout.addWidget(self._view_help)

        self.setLayout(f_layout)
