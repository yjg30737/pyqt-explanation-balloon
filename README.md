# pyqt-explanation-balloon
PyQt explanation balloon

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-explanation-balloon`

## Preview

Explanation balloon can be used to explain certain widget. You can close this balloon with X button at the top right. 

![image](https://user-images.githubusercontent.com/55078043/189249105-9ce31fd1-164b-4b35-af6d-af623ff2f56a.png)

You can set the widget which you want to describe with balloon. 

You can also set the size and content of balloon with constructor. Check the class overview below.

This explanation balloon is perfectly responsive to window's resize/move/activate/deactivate event.

Text alignment is set to the center, word is wrapped at word boundaries.

## Class/Method Overview
* `ExplanationBalloon(widget, width: float, height: float, text: str)` - Constructor. `widget` is the widget which is supposed to be explained by explanation balloon.
* `setBackgroundColor(color: QColor)` - Set the background color. Text color will be also changed automatically based on background color. 
* `setFont(font: QFont)` - Default function of Qt. You can set the font of text.

## Example
```python
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QVBoxLayout, QWidget

from pyqt_explanation_balloon.explanationBalloon import ExplanationBalloon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('Show explanation balloon')

        lay = QVBoxLayout()
        lay.addWidget(btn)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

        self.__eb = ExplanationBalloon(btn, 300.0, 200.0, 'This is explanation balloon made out of PyQt')
        self.__eb.setFont(QFont('Arial', 14))
        self.__eb.setBackgroundColor(QColor(50, 50, 50, 255))
        btn.clicked.connect(self.__eb.show)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/189249567-076f8141-1fc7-4e46-b6ba-29f87ab645a6.png)
