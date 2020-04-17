import requests, json, sys
from PyQt5 import QtWidgets
from UI.mainwindow import Ui_MainWindow  # the user interface object


def get(city, country):
    location = f'{city},{country}'  # the standard form for location in openweathermap
    url = r'http://api.openweathermap.org/data/2.5/weather?q=%s,uk&APPID=e93af7923aeaa74a1dbba5be6a154e49' % location
    response = requests.get(url)  # download JSON data
    response.raise_for_status()   # asserts we have no errors
    weather = json.loads(response.text)  # the python value for weather
    # the standard response from the site with kelvin unit --> to celsius
    description = weather['weather'][0]['main'], weather['weather'][0]['description']
    main_temp = str(weather['main']['temp'] - 273)
    feels = str(weather['main']['feels_like'] - 273)
    min_temp = str(weather['main']['temp_min'] - 273)
    max_temp = str(weather['main']['temp_max'] - 273)
    pressure = str(weather['main']['pressure']) + ' hpa'
    humidity = str(weather['main']['humidity']) + ' %'
    speed = str(weather['wind']['speed'])
    angle = str(weather['wind']['deg'])
    data = (description, main_temp, feels, min_temp, max_temp, pressure, humidity, speed, angle)
    return data


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.app = QtWidgets.QApplication(sys.argv)  # the main application
        super().__init__(parent)
        self.ui = Ui_MainWindow()  # the main window
        self.ui.setupUi(self)      # set up the GUI
        # connecect the menu actions with their functions
        self.ui.get.clicked.connect(self.get_weather) 
        self.ui.name.triggered.connect(self.name)   
        self.ui.phone.triggered.connect(self.phone)
        self.ui.help.triggered.connect(self.help)

    def show(self):
        super().show()      # freeze the code untill the user closes the application main window
        sys.exit(self.app.exec_())

    def get_weather(self):
        city = self.ui.city.text()  # city name
        country = self.ui.country.text()  # country name
        try:
            data = get(city, country)  # get the weather data
            description = f'{data[0][0]} -- {data[0][1]}'
            self.ui.description.setText(description)
            self.ui.maintemp.setText(data[1])
            self.ui.feelslike.setText(data[2])
            self.ui.min_temp.setText(data[3])
            self.ui.max_temp.setText(data[4])
            self.ui.pressure.setText(data[5])
            self.ui.humidity.setText(data[6])
            self.ui.speed.setText(data[7])
            self.ui.angle.setText(data[8])

        except :  # incase of any error erase the data and show invalid input message
            self.ui.description.setText('Invalid Location !!')
            self.ui.maintemp.setText('')
            self.ui.feelslike.setText('')
            self.ui.min_temp.setText('')
            self.ui.max_temp.setText('')
            self.ui.pressure.setText('')
            self.ui.humidity.setText('')
            self.ui.speed.setText('')
            self.ui.angle.setText('')

    def name(self):  # show name message box
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('My name')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText('Mohamed mostafa al-ghaly')
        show = msg.exec_()

    def phone(self): # show phone message box
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Phone')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText('01002929690')
        show = msg.exec_()

    def help(self):  # show help message box
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Help')
        msg.setText('weather data from : openweathermap')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        about = 'name : mohamed al-ghaly.\nphone : 01002929690\npython developer\n' \
                'twitter : https://twitter.com/mohamed32093140\n ' \
                'linkedin : https://www.linkedin.com/in/mohamed-alghaly-33ab201a3/'
        msg.setDetailedText(about)
        shoe = msg.exec_()


window = MainWindow()  # application object

window.show()          # show the main window

