import io
import sys

from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>540</width>
    <height>627</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>540</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.pushButton.move(70, 150)
        self.do_paint = False
        self.holst = []
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
            qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            z = randint(0, 500)
            qp.drawEllipse(randint(0, 100),
                           randint(0, 100),
                           z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())