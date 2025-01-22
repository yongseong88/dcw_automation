import random
import time

import pytest

from TestCase.base_test import BaseTest
from Pages.Canvas_Page import CanVasPage
from Pages.Login_page import LoginPage
from Pages.Main_Page import MainPage
from Utilities.File_util import multi_line
from Utilities.configreaderutil import readConfig
from Utilities.json_util import Drive_api


@pytest.mark.usefixtures("initialize_driver", "base_url")
class TestCanvasfileopen(BaseTest):

    def canvas_login(self, base_url):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)

        try:
            env = "dev" if "dev" in base_url else "prod"

            valid_id = readConfig("Account", f"{env}_id")
            valid_pwd = readConfig("Account", f"{env}_password")

            main_page.login_btn_click()
            login_page.set_id(valid_id)
            login_page.set_pwd(valid_pwd)
            login_page.login_submit()

        except AssertionError as e:
            print(f"AssertionError: {e}")

    def tesot_canvas_open_popup(self, base_url):
        # MainPage 인스턴스 생성
        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        try:
            self.canvas_login(base_url)
            main_page.canvas_btn_click()
            time.sleep(1)
            canvas_page.open_btn_click()
            time.sleep(9)

            http_status = drive_api.filebrowser_list_api(base_url, "ROOT")
            print(f"Status Code: {http_status.status_code}")
            assert http_status.status_code == 200, "FileOpen failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()

    def tesot_canvas_root_file_open(self, base_url):
        # MainPage, CanVasPage 인스턴스 생성
        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        try:
            self.canvas_login(base_url)
            main_page.canvas_btn_click()
            time.sleep(1)
            canvas_page.open_btn_click()
            time.sleep(5)

            root_file_open = canvas_page.file_open("file")
            time.sleep(8)

            root_file_key = drive_api.file_key_search(base_url, root_file_open)
            file_open_confirm_http_status = drive_api.file_open_api(base_url, root_file_key)
            print(f"\r\nStatus Code: {file_open_confirm_http_status.status_code}")
            assert file_open_confirm_http_status.status_code == 200, "FileOpen failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()

    def tesot_canvas_folder_file_open(self, base_url):
        # MainPage, CanVasPage 인스턴스 생성
        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        try:
            self.canvas_login(base_url)
            main_page.canvas_btn_click()
            time.sleep(1)
            canvas_page.open_btn_click()
            time.sleep(5)

            folder_name, folder_in_file_name = canvas_page.file_open("folder")
            time.sleep(8)

            folder_key, folder_in_file_key = drive_api.file_key_search(base_url, folder_name, folder_in_file_name)
            file_open_confirm_http_status = drive_api.file_open_api(base_url, folder_in_file_key)
            print(f"\r\nStatus Code: {file_open_confirm_http_status.status_code}")

            assert file_open_confirm_http_status.status_code == 200, "FileOpen failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()

    # def tesot_canvas_open_cancel(self):
    #     # MainPage, CanVasPage 인스턴스 생성
    #     main_page = MainPage(self.driver)
    #     canvas_page = CanVasPage(self.driver)
    #
    #     self.canvas_login()
    #     main_page.canvas_btn_click()
    #     time.sleep(1)
    #     canvas_page.open_btn_click()
    #     time.sleep(1)
    #     canvas_page.filebrowser_cancel_btn_click()
    #     time.sleep(2)
    #
    def tesot_canvas_edit_root_file_open(self, base_url):
        # MainPage, CanVasPage 인스턴스 생성
        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        try:
            input_multiline = multi_line()
            page_max = len(input_multiline)  # 페이지 최대 수

            # page_add_number = random.randrange(1, page_max + 1)  # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)

            start_x = 565  # 캔버스 첫 칸의 x 좌표
            start_y = 415  # 캔버스 첫 칸의 y 좌표


            self.canvas_login(base_url)
            main_page.canvas_btn_click()
            time.sleep(1)

            print("\r\n추가 할 페이지 수: {}".format(page_max-1))

            for pg in range(page_max):
                scroll_y_location = canvas_page.scroll_location()

                if pg > 0:
                    if scroll_y_location == 8:
                        start_y = (start_y - 20)

                    canvas_page.page_add_btn_click()

                    match len(input_multiline):
                        case length if length > pg:
                            canvas_page.drawing_tool(start_x, start_y)
                            print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
                            canvas_page.description_input(input_multiline[pg])
                            print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
                            print("페이지 정보: {} / {}".format(pg + 1, page_max))
                            time.sleep(2)

                        case length if length < pg:
                            canvas_page.drawing_tool(start_x, start_y)
                            print("입력 가능 한 멀티라인 텍스트가 없어요.")
                            print("페이지 정보: {} / {}".format(pg + 1, page_max))
                            time.sleep(2)

                else:
                    canvas_page.drawing_tool(start_x, start_y)
                    print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
                    canvas_page.description_input(input_multiline[pg])
                    print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
                    print("페이지 정보: {} / {}".format(pg + 1, page_max))
                    time.sleep(2)

            canvas_page.open_btn_click()
            canvas_page.edit_save_cancel()
            time.sleep(5)
            root_file_open = canvas_page.file_open("file")
            time.sleep(8)

            root_file_key = drive_api.file_key_search(base_url, root_file_open)
            file_open_confirm_http_status = drive_api.file_open_api(base_url, root_file_key)
            print(f"\r\nStatus Code: {file_open_confirm_http_status.status_code}")
            assert file_open_confirm_http_status.status_code == 200, "Fileadd failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()

    def tesot_canvas_edit_folder_file_open(self, base_url):
        # MainPage, CanVasPage 인스턴스 생성
        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        self.canvas_login(base_url)
        main_page.canvas_btn_click()
        time.sleep(1)

        try:
            input_multiline = multi_line()
            page_max = len(input_multiline)  # 페이지 최대 수

            start_x = 565  # 캔버스 첫 칸의 x 좌표
            start_y = 415  # 캔버스 첫 칸의 y 좌표

            print("\r\n추가 할 페이지 수: {}".format(page_max-1))

            for pg in range(page_max):
                scroll_y_location = canvas_page.scroll_location()

                if pg > 0:
                    if scroll_y_location == 8:
                        start_y = (start_y - 20)

                    canvas_page.page_add_btn_click()

                    match len(input_multiline):
                        case length if length > pg:
                            canvas_page.drawing_tool(start_x, start_y)
                            print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
                            canvas_page.description_input(input_multiline[pg])
                            print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
                            print("페이지 정보: {} / {}".format(pg + 1, page_max))
                            time.sleep(2)

                        case length if length < pg:
                            canvas_page.drawing_tool(start_x, start_y)
                            print("입력 가능 한 멀티라인 텍스트가 없어요.")
                            print("페이지 정보: {} / {}".format(pg + 1, page_max))
                            time.sleep(2)

                else:
                    canvas_page.drawing_tool(start_x, start_y)
                    print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
                    canvas_page.description_input(input_multiline[pg])
                    print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
                    print("페이지 정보: {} / {}".format(pg + 1, page_max))
                    time.sleep(2)

            canvas_page.open_btn_click()
            canvas_page.edit_save_cancel()
            time.sleep(5)
            folder_name, folder_in_file_name = canvas_page.file_open("folder")
            time.sleep(8)

            folder_key, folder_in_file_key = drive_api.file_key_search(base_url, folder_name, folder_in_file_name)
            file_open_confirm_http_status = drive_api.file_open_api(base_url, folder_in_file_key)
            print(f"\r\nStatus Code: {file_open_confirm_http_status.status_code}")
            assert file_open_confirm_http_status.status_code == 200, "Fileadd failed"

        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()
    #
    # def tesot_canvas_file_scroll(self):
    #     # MainPage, CanVasPage 인스턴스 생성
    #     main_page = MainPage(self.driver)
    #     canvas_page = CanVasPage(self.driver)
    #
    #     self.canvas_login()
    #     time.sleep(1)
    #     main_page.canvas_btn_click()
    #     time.sleep(1)
    #     canvas_page.add_btn_click()
    #     time.sleep(5)
    #     canvas_page.list_scroll()