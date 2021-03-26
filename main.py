from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


Window.size = (414, 896)


class Register(MDScreen):
    pass


class Welcome(MDScreen):
    pass


class JoinMobile(MDScreen):
    pass

    def click_join(self, *args):
        if self.login.text and self.password.text:
            self.add_widget(Welcome())


class JoinMobileApp(MDApp):

    def build(self):
        return


if __name__ == '__main__':
    JoinMobileApp().run()

# ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue',
#  'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber',
#  'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']