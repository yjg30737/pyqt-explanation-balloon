from setuptools import setup, find_packages

setup(
    name='pyqt-explanation-balloon',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_explanation_balloon.ico': ['close.svg']},
    description='PyQt explanation balloon',
    url='https://github.com/yjg30737/pyqt-explanation-balloon.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-svg-button>=0.0.1'
    ]
)