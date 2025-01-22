import time
from Pages.Base_Page import BasePage
from Utilities.Locators import login_LocatorFields


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locate = login_LocatorFields

    def set_id(self, emaill_address):
        self.set(self.locate.id_field, emaill_address)

    def set_pwd(self, password):
      self.set(self.locate.pwd_field, password)

    def login_submit(self):
        self.click(self.locate.submit_button)
        time.sleep(3)

    def get_warning_message(self):
        msg = self.get_text(self.locate.warning_message)
        return msg