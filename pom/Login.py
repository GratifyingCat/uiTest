from base.seleniumbase import SeleniumBase


class Login(SeleniumBase):
    def __init__(self, driver, login, password, login_field_path, password_field_path, login_btn_path):
        super(Login, self).__init__(driver)
        self.login = login
        self.password = password
        self.__login_field_path = login_field_path
        self.__password_field_path = password_field_path
        self.__login_btn_path = login_btn_path

    def get_element(self, field_path):
        return self.is_visible('XPATH', field_path)

    def input_login(self):
        self.get_element(self.__login_field_path).send_keys(self.login)

    def input_password(self):
        self.get_element(self.__password_field_path).send_keys(self.password)

    def auth(self):
        self.get_element(self.__login_btn_path).click()
