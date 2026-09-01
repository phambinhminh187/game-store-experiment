from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys, webbrowser, webview

def launcher(window_title, target):
    web_window = webview.create_window(window_title, target)
    webview.start()

account = {
    "username" : "",
    "password" : ""
}


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            "/Users/phambinhminh/MindxPython/PTA/game-store_login.ui", self)
        self.btn_login.clicked.connect(self.show_main)
        self.btn_register.clicked.connect(self.show_register)
        self.msg_box = QMessageBox()

    def show_main(self):
        username = self.txt_username.text()
        password = self.txt_password.text()
        if account["username"] == username and account["password"] == password:
            main.show()
            self.close()
        else:
            self.msg_box.setText("Retype information")
            self.msg_box.setIcon(QMessageBox.Icon.Warning)
            self.msg_box.exec()


    def show_register(self):
        register.show()
        self.close()


class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            "/Users/phambinhminh/MindxPython/PTA/game-store_register.ui", self)
        self.btn_login.clicked.connect(self.show_login)
        self.btn_register.clicked.connect(self.check_register)
        self.msg_box = QMessageBox()

    def show_login(self):
        login.show()
        self.close()

    def check_register(self):
        username = self.txt_username.text()
        password = self.txt_password.text()
        password_2 = self.txt_password_2.text()
        if username and password == password_2:
            account["username"] = username
            account["password"] = password

            self.msg_box.setText("Register operation successful")
            self.msg_box.setIcon(QMessageBox.Icon.Information)
            self.msg_box.exec()
            main.show()
            self.close()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/Users/phambinhminh/MindxPython/PTA/game_store.ui", self)
        self.btn_about.clicked.connect(self.show_info)
        self.btn_home.clicked.connect(lambda: self.show_pages(0))
        self.btn_purchase.clicked.connect(lambda: self.show_pages(1))
        self.btn_logout.clicked.connect(self.show_login)
        buttons = [
            (self.btn_play_roblox, 0),
            (self.btn_play_minecraft, 1),
            (self.btn_play_apex, 2),
            (self.btn_play_league, 3),
            (self.btn_play_fortnite, 4),
            (self.btn_play_counter, 5),
            (self.btn_play_geometry, 6),
            (self.btn_play_devil, 7)
        ]

        for btn, index in buttons:
            btn.clicked.connect(lambda _, i=index: self.show_detail(i))

        self.btn_buy_minecraft.clicked.connect(lambda: webbrowser.open("https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc"))
        self.btn_buy_roblox.clicked.connect(lambda: webbrowser.open("https://www.roblox.com/upgrades/robux"))
        self.btn_buy_apex.clicked.connect(lambda: webbrowser.open("https://store.ea.com/apex-legends/en"))
        self.btn_buy_league.clicked.connect(lambda: webbrowser.open("https://lolskinstore.com/store/"))

    def show_info(self):
        about.show()

    def show_login(self):
        login.show()
        self.close()

    def show_detail(self, tab_index):
        detail.show()
        detail.stackedWidget.setCurrentIndex(tab_index)
        self.close()

    def show_pages(self, pages):
        self.stackedWidget.setCurrentIndex(pages)


class Detail(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/Users/phambinhminh/MindxPython/PTA/game-store_detail.ui", self)
        self.btnback.clicked.connect(self.show_main)

        self.btn_install_roblox.clicked.connect(lambda: webbrowser.open("https://www.roblox.com/download"))
        self.btn_install_minecraft.clicked.connect(lambda: webbrowser.open("https://www.minecraft.net/en-us/download"))
        self.install(self.btn_install_apex, "https://www.ea.com/games/apex-legends/apex-legends",
                     "https://fa.getpedia.net/data?q=zEDMzITO4ATM2ETNxQjM5MjN8BzMzYzMxw3ZtRmLjFWbt8Gaj1yck5WZnVGbtgXZwF2L3AzLyAzL5EDMy8SZslmZvEGdhR2L")
        self.btn_install_league.clicked.connect(lambda: webbrowser.open("https://www.leagueoflegends.com/en-us/download/"))
        self.install(self.btn_install_fortnite, "https://fortnite.en.softonic.com/",
                     "https://fortnite.en.softonic.com/mac")
        self.install(self.btn_install_counter, "https://counter-strike-2.en.softonic.com/",
                     "https://counter-strike-2.en.softonic.com/mac")
        self.btn_run_geometry.clicked.connect(lambda: launcher("Geometry Dash", "https://geometrydash-pc.com/"))
        self.btn_run_devil.clicked.connect(lambda: launcher("Level Devil", "https://playleveldevil.com/play/"))

        self.learn(self.btn_learn_roblox, "https://roblox.vnggames.com/")
        self.learn(self.btn_learn_minecraft, "https://www.minecraft.net/en-us")
        self.learn(self.btn_learn_apex, "https://www.ea.com/games/apex-legends/apex-legends/")
        self.learn(self.btn_learn_league, "https://www.leagueoflegends.com/en-us/")
        self.learn(self.btn_learn_fortnite, "https://www.fortnite.com")
        self.learn(self.btn_learn_counter, "https://www.counter-strike.net/cs2")
        self.learn(self.btn_learn_geometry, "https://www.geometrydash.com/")
        self.learn(self.btn_learn_devil, "https://playleveldevil.com/")

        buttons = [
            (self.btn_tab_roblox, 0),
            (self.btn_tab_minecraft, 1),
            (self.btn_tab_apex, 2),
            (self.btn_tab_league, 3),
            (self.btn_tab_fortnite, 4),
            (self.btn_tab_counter, 5),
            (self.btn_tab_geometry, 6),
            (self.btn_tab_devil, 7)
        ]

        for btn, index in buttons:
            btn.clicked.connect(lambda _, i=index: main.show_detail(i))

    def show_main(self):
        main.show()
        self.close()

    def install(self, button_name, link1, link2):
        if sys.platform == 'win32':
            button_name.clicked.connect(lambda: webbrowser.open(link1))
        else:
            button_name.clicked.connect(lambda: webbrowser.open(link2))

    def learn(self, btn_name, url):
        btn_name.clicked.connect(lambda: webbrowser.open(url))


class About(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/Users/phambinhminh/MindxPython/PTA/game-store_about.ui", self)


if  __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    register = Register()
    main = Main()
    detail = Detail()
    about = About()
    login.show()
    sys.exit(app.exec())
