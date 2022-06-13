# pyqt-explanation-balloon
PyQt explanation balloon

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-explanation-balloon`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a>

## Usage
Constructor - `ExplanationBalloon(x: float, y: float, width: float, height: float, text: str)`

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

        self.__eb = ExplanationBalloon(0, 0, 200.0, 100.0, 'This is explanation balloon\nmade out of PyQt')
        btn.clicked.connect(self.__eb.show)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/173264369-c7023c03-18d0-44a9-aabb-a4fad215f742.png)
