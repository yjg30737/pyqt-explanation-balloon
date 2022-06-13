# pyqt-explanation-balloon
PyQt explanation balloon

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-explanation-balloon`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a>

## Preview

Explanation balloon can be used to explain certain widget. You can close this balloon with X button at the top right. 

![image](https://user-images.githubusercontent.com/55078043/173282320-6fe4a07b-27dc-47b9-af1b-3d531f9c408b.png)

You can set the widget which you want to describe with balloon. 

You can also set the size and content of balloon with constructor. Check the class overview below.

This explanation balloon is perfectly responsive to window's resize/move/activate/deactivate event.

## Class Overview
* `ExplanationBalloon(widget, width: float, height: float, text: str)` - Constructor. `widget` is the widget which is supposed to be explained by explanation balloon.

## Example
```python
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

        self.__eb = ExplanationBalloon(btn, 200.0, 100.0, 'This is explanation balloon\nmade out of PyQt')
        btn.clicked.connect(self.__eb.show)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/173282320-6fe4a07b-27dc-47b9-af1b-3d531f9c408b.png)
