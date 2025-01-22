import pytest
from Pages.Main_Page import MainPage
from Pages.Login_page import LoginPage
from TestCase.base_test import BaseTest
from Utilities.configreaderutil import readConfig
from Utilities.json_util import User_api

@pytest.mark.usefixtures("initialize_driver", "base_url")
class TestLogin(BaseTest):

  # user_info
  # dev_id = readConfig("Account", "dev_id")
  # dev_pwd = readConfig("Account", "dev_password")
  # prod_id = readConfig("Account", "prod_id")
  # prod_pwd = readConfig("Account", "prod_password")
  # invalid_id = readConfig("Account", "invalid_id")
  # invalid_pwd = readConfig("Account", "invalid_pwd")

  def account_config(self, base_url):

    try:
      env = "dev" if "dev" in base_url else "prod"

      return {
        "valid_id": readConfig("Account", f"{env}_id"),
        "valid_pwd": readConfig("Account", f"{env}_password"),
        "invalid_id": readConfig("Account", "invalid_id"),
        "invalid_pwd": readConfig("Account", "invalid_pwd")

      }

    except AssertionError as e:
      print(f"AssertionError: {e}")


  @pytest.mark.order(1)
  def tesot_login_success(self, base_url):

    main_page = MainPage(self.driver)
    login_page = LoginPage(self.driver)
    user_info = self.account_config(base_url)
    user_api = User_api(base_url)

    try:
      main_page.login_btn_click()
      login_page.set_id(user_info['valid_id'])
      login_page.set_pwd(user_info['valid_pwd'])
      login_page.login_submit()
      login_success_http_status = user_api.login_check_api(user_info['valid_id'], user_info['valid_pwd'])
      menu_http_status = user_api.menus_api(base_url)

      print(f"\r\nlogin_success_http_Status Code: {login_success_http_status.status_code}")
      print(f"menu_http_Status Code: {menu_http_status.status_code}")

      assert login_success_http_status.status_code == 200, "Login Failed"
      assert menu_http_status.status_code == 200, "Menu Failed"

    except AssertionError as e:
      print(f"AssertionError: {e}")
      login_page.screenshot_capture()

  @pytest.mark.order(2)
  def tesot_login_id_failure(self, base_url):

    main_page = MainPage(self.driver)
    login_page = LoginPage(self.driver)
    user_info = self.account_config(base_url)
    user_api = User_api(base_url)

    try:
      main_page.login_btn_click()
      login_page.set_id(user_info['invalid_id'])
      login_page.set_pwd(user_info['valid_pwd'])
      login_page.login_submit()

      message = login_page.get_warning_message()
      http_status = user_api.login_check_api(user_info['invalid_id'], user_info['valid_pwd'])

      print(f"\r\nStatus Code: {http_status.status_code}")
      print(message)

      assert http_status.status_code != 200, message

    except AssertionError as e:
      print(f"AssertionError: {e}")
      login_page.screenshot_capture()

  @pytest.mark.order(3)
  def tesot_login_pwd_failure(self, base_url):

    main_page = MainPage(self.driver)
    login_page = LoginPage(self.driver)
    user_info = self.account_config(base_url)
    user_api = User_api(base_url)

    try:
        main_page.login_btn_click()
        login_page.set_id(user_info['valid_id'])
        login_page.set_pwd(user_info['invalid_pwd'])
        login_page.login_submit()
        message = login_page.get_warning_message()

        http_status = user_api.login_check_api(user_info['valid_id'], user_info['invalid_pwd'])
        print(f"\r\nStatus Code: {http_status.status_code}")
        print(message)

        assert http_status.status_code != 200, message

    except AssertionError as e:
      print(f"AssertionError: {e}")
      login_page.screenshot_capture()