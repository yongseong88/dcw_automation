from Pages.Main_Page import MainPage
from Pages.Login_page import LoginPage
from TestCase.base_test import BaseTest
from Utilities.configreaderutil import readConfig
from Utilities.json_util import login_post


class TestLogin(BaseTest):

  def test_login_success(self):
    user_id = readConfig("Account", "id")
    user_pwd = readConfig("Account", "password")

    main_page = MainPage(self.driver)
    login_page = LoginPage(self.driver)

    main_page.login_btn_click()
    login_page.set_id(user_id)
    login_page.set_pwd(user_pwd)
    login_page.login_submit()

    http_status = login_post(user_id, user_pwd)
    print(f"\r\nStatus Code: {http_status}")
    print("login Success")
    assert http_status == 200, "Login Failed"

  def test_login_id_failure(self):
    user_id = readConfig("Account", "invalid_id")
    user_pwd = readConfig("Account", "password")

    main_page = MainPage(self.driver)
    login_page = LoginPage(self.driver)

    main_page.login_btn_click()
    login_page.set_id(user_id)
    login_page.set_pwd(user_pwd)
    login_page.login_submit()
    message = login_page.get_warning_message()

    http_status = login_post(user_id, user_pwd)
    print(f"\r\nStatus Code: {http_status}")
    print(message)
    assert http_status != 200, message

  def test_login_pwd_failure(self):
    user_id = readConfig("Account", "id")
    user_pwd = readConfig("Account", "invalid_pwd")

    main_page = MainPage(self.driver)
    login_page = LoginPage(self.driver)

    main_page.login_btn_click()
    login_page.set_id(user_id)
    login_page.set_pwd(user_pwd)
    login_page.login_submit()
    message = login_page.get_warning_message()

    http_status = login_post(user_id, user_pwd)
    print(f"\r\nStatus Code: {http_status}")
    print(message)
    assert http_status != 200, message