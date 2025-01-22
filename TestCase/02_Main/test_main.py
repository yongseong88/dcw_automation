import time

import pytest
from Pages.Canvas_Page import CanVasPage
from TestCase.base_test import BaseTest
from Pages.Login_page import LoginPage
from Pages.Main_Page import MainPage
from Utilities.configreaderutil import readConfig, read_file
from Utilities.json_util import User_api, file_group_api

@pytest.mark.usefixtures("initialize_driver", "base_url")
class TestMain(BaseTest):

    def canvas_login(self, base_url):
        login_page = LoginPage(self.driver)

        try:
            env = "dev" if "dev" in base_url else "prod"

            valid_id = readConfig("Account", f"{env}_id")
            valid_pwd = readConfig("Account", f"{env}_password")

            login_page.set_id(valid_id)
            login_page.set_pwd(valid_pwd)
            login_page.login_submit()

        except AssertionError as e:
            print(f"AssertionError: {e}")

    @pytest.mark.order(5)
    def tesot_canvas_click(self, base_url):
        # MainPage 인스턴스 생성
        main_page = MainPage(self.driver)
        user_api = User_api(base_url)

        try:
            main_page.login_btn_click()
            self.canvas_login(base_url)
            main_page.canvas_btn_click()

            user_info_http_status = user_api.user_status_api(base_url)
            print(f"\r\nuser_info_http_Status Code: {user_info_http_status.status_code}")

            assert user_info_http_status.status_code == 200, "CanVas Click Failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            main_page.screenshot_capture()

    def tesot_canvas_login(self, base_url):
        # MainPage 인스턴스 생성
        main_page = MainPage(self.driver)
        user_api = User_api(base_url)

        try:
            main_page.canvas_btn_click()
            self.canvas_login(base_url)

            user_info_http_status = user_api.user_status_api(base_url)
            menu_http_status = user_api.menus_api(base_url)

            print(f"\r\nuser_info_http_Status Code: {user_info_http_status.status_code}")
            print(f"menu_http_Status Code: {menu_http_status.status_code}")

            assert user_info_http_status.status_code == 200, "CanVas Click Login Failed"
            assert menu_http_status.status_code == 200, "CanVas Click Login Failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            main_page.screenshot_capture()

    def tesot_cloud_click(self, base_url):
        main_page = MainPage(self.driver)
        user_api = User_api(base_url)
        file_api = file_group_api()

        try:
            main_page.login_btn_click()
            self.canvas_login(base_url)
            main_page.cloud_btn_click()

            user_http_status = user_api.user_status_api(base_url)
            path_http_status = file_api.cloud_group_path_api(base_url)
            list_http_status = file_api.cloud_group_list_api(base_url)

            print(f"\r\nuser_http_Status Code: {user_http_status.status_code}")
            print(f"path_http_Status Code: {path_http_status.status_code}")
            print(f"list_http_Status Code: {list_http_status.status_code}")

            assert user_http_status.status_code == 200, "user_info Failed"
            assert path_http_status.status_code == 200, "group_path Failed"
            assert list_http_status.status_code == 200, "group_list Failed"
            time.sleep(7)

        except AssertionError as e:
            print(f"AssertionError: {e}")
            main_page.screenshot_capture()

    def tesot_cloud_login(self, base_url):
        # MainPage 인스턴스 생성
        main_page = MainPage(self.driver)
        user_api = User_api(base_url)
        file_api = file_group_api()

        try:
            main_page.cloud_btn_click()
            self.canvas_login(base_url)

            user_http_status = user_api.user_status_api(base_url)
            path_http_status = file_api.cloud_group_path_api(base_url)
            list_http_status = file_api.cloud_group_list_api(base_url)

            print(f"\r\nuser_http_Status Code: {user_http_status.status_code}")
            print(f"path_http_Status Code: {path_http_status.status_code}")
            print(f"list_http_Status Code: {list_http_status.status_code}")


            assert user_http_status.status_code == 200, "user_info Failed"
            assert path_http_status.status_code == 200, "group_path Failed"
            assert list_http_status.status_code == 200, "group_list Failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            main_page.screenshot_capture()

    def tesot_braille_setting(self, base_url):
        main_page = MainPage(self.driver)
        file_path = "/Users/park-yongseong/Documents/DCW_Automation/Config/braille_data.JSON"
        json_read = read_file(file_path)
        user_api = User_api(base_url)

        try:
            main_page.login_btn_click()
            self.canvas_login(base_url)
            main_page.braille_language_dropdown()
            time.sleep(2)

            braille_list = main_page.braille_language_list()

            for bl in range(len(braille_list)):
                braille_list[bl].click()  # 현재 순서의 항목 선택
                time.sleep(2)
                main_page.braille_language_dropdown()
                time.sleep(2)
                braille_info = braille_list[bl].text

                braille_text = braille_info[0:(braille_info.find("-") - 1)]
                braille_grade = braille_info[(braille_info.find("-")) + 1:]
                print(f"\r\n점역 언어: {braille_text}")
                print(f"점역 언어 Grade: {braille_grade.strip()}")

                for key in json_read:
                    if type(json_read[key]) is list:
                        for item in json_read[key]:
                            if braille_text in item and "language_option" in item[braille_text]:
                                print(f"Found braille_language: {item[braille_text]['language']}")
                                print(f"Found {braille_grade.strip()}: {item[braille_text]['language_option'][braille_grade.strip()]}")

                                braille_info_http_status = user_api.BrailleLanguage_change_api(base_url, item[braille_text]['language'], item[braille_text]['language_option'][braille_grade.strip()])
                                print(f"\r\n{braille_text} - {braille_grade.strip()} http_status Code: {braille_info_http_status.status_code}")
                                assert braille_info_http_status.status_code == 200, "braille put failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            main_page.screenshot_capture()