import time

from Pages.Cloud_Page import CloudPage
from TestCase.base_test import BaseTest
from Utilities.configreaderutil import readConfig
from Pages.Login_page import LoginPage
from Pages.Main_Page import MainPage


class TestCloudfilopen(BaseTest):
    user_id = readConfig("Account", "id")
    user_pwd = readConfig("Account", "password")

    def canvas_login(self):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)

        main_page.login_btn_click()
        login_page.set_id(self.user_id)
        login_page.set_pwd(self.user_pwd)
        login_page.login_submit()

    def tesot_cloud_listinfo(self):
        main_page = MainPage(self.driver)
        cloud_page = CloudPage(self.driver)

        self.canvas_login()
        time.sleep(1)
        main_page.cloud_btn_click()
        time.sleep(8)
        cloud_page.file_info()
