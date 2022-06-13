import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen, QPainterPath
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QGridLayout
from pyqt_svg_button import SvgButton


class ExplanationBalloon(QWidget):
    def __init__(self, x: float, y: float, width: float, height: float, text: str):
        super().__init__()
        self.__initUi(x, y, width, height, text)

    def __initUi(self, x, y, width, height, text):
        self.setFixedSize(width + 2, height + 10)
        self.__initBalloon(x, y, width, height, text)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        eff = QGraphicsDropShadowEffect(self)
        eff.setOffset(0, 0)
        eff.setBlurRadius(5.0)
        self.setGraphicsEffect(eff)

        self.__btn = SvgButton(self)
        self.__btn.setIcon('close.svg')
        self.__btn.setFixedSize(14, 14)
        self.__btn.setAsCircle()
        self.__btn.clicked.connect(self.close)

        lay = QGridLayout()
        lay.addWidget(self.__btn, 0, 0, 1, 1, Qt.AlignTop | Qt.AlignRight)
        lay.setContentsMargins(5, 5, 5, 5)
        self.setLayout(lay)

    def __initBalloon(self, x, y, width, height, text):
        self.__border_width = 1
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__balloon = self.__getBalloonShape(self.__x, self.__y, self.__width, self.__height)

    def __setIsosceles(self, x: float, y: float, width: float, height: float, orientation=Qt.Horizontal) -> QPainterPath:
        isosceles = QPainterPath()
        # horizontal
        x1 = x
        y1 = y

        x2 = x1+width
        y2 = y1

        x3 = (x1+x2) / 2
        y3 = y1+height

        isosceles.moveTo(x1, y1)
        isosceles.lineTo(x2, y2)
        isosceles.lineTo(x3, y3)
        isosceles.lineTo(x1, y1)

        return isosceles

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush(QColor(50, 50, 50, 255))
        pen = QPen(QColor(Qt.darkGray), self.__border_width)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPath(self.__balloon)
        painter.drawText(self.__balloon.boundingRect(), Qt.AlignCenter, self.__text)

        return super().paintEvent(e)

    def __getBalloonShape(self, x: float, y: float, width: float, height: float):
        path1 = QPainterPath()
        path1.addRoundedRect(x, y, width, height, 10.0, 10.0)

        path2 = self.__setIsosceles(x + 20.0, y + height - 3, 30.0, 10.0)

        path3 = path2.united(path1)

        return path3


