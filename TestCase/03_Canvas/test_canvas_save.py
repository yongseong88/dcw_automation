import random
import time
import datetime

import pytest

from Pages.Canvas_Page import CanVasPage
from Pages.Main_Page import MainPage
from TestCase.base_test import BaseTest
from Utilities.File_util import multi_line
from Utilities.configreaderutil import readConfig
from Utilities.json_util import Drive_api
from Pages.Login_page import LoginPage


@pytest.mark.usefixtures("initialize_driver", "base_url")
class TestCanvasfilesave(BaseTest):

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

    def tesot_canvas_root_save(self, base_url):

        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        try:
            today = datetime.datetime.now().strftime('%Y_%m_%d_')
            input_multiline = multi_line()
            page_max = len(input_multiline)  # 페이지 최대 수

            start_x = 585  # 캔버스 첫 칸의 x 좌표
            start_y = 425  # 캔버스 첫 칸의 y 좌표

            self.canvas_login(base_url)
            main_page.canvas_btn_click()
            time.sleep(1)

            print("\r\n추가 할 페이지 수: {}".format(page_max - 1))

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

            canvas_page.save_btn_click()
            time.sleep(5)
            canvas_page.save_set(today + "automation_file")
            time.sleep(1)
            canvas_page.save_confirm_btn_click()
            time.sleep(30)

            save_name = canvas_page.save_filename()
            time.sleep(8)
            print(f"save_name: {save_name}")

            # save_dtms_data = drive_api.dtms_data('ROOT', "pocket_kr")
            # create_http_status = dtms_create_api('ROOT', today + "_automation_test", save_dtms_data)
            # assert create_http_status.status_code <= 201, "DTMS created failed"
            # print(f"create_http_status Code: {create_http_status.status_code}")

            save_dtms_data = drive_api.dtms_data(base_url, save_name)
            # print(f"save_dtms_data: {save_dtms_data}")

            save_http_status = drive_api.dtms_save_api(base_url, save_name, save_dtms_data)
            print(f"save_http_status Code: {save_http_status.status_code}")

            assert save_http_status.status_code <= 200, "DTMS save failed"


        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()

    def tesot_canvas_folder_save(self, base_url):

        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        try:
            today = datetime.datetime.now().strftime('%Y_%m_%d_')
            input_multiline = multi_line()
            page_max = len(input_multiline)  # 페이지 최대 수

            start_x = 565  # 캔버스 첫 칸의 x 좌표
            start_y = 415  # 캔버스 첫 칸의 y 좌표

            self.canvas_login(base_url)
            time.sleep(1)
            main_page.canvas_btn_click()
            time.sleep(1)

            print("\r\n추가 할 페이지 수: {}".format(page_max - 1))

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

            canvas_page.save_btn_click()
            time.sleep(5)
            click_folder_name = canvas_page.folder_open()
            canvas_page.save_set(today + "automation_file")
            time.sleep(1)
            canvas_page.save_confirm_btn_click()
            time.sleep(30)

            save_name = canvas_page.save_filename()
            time.sleep(8)
            print(f"save_name: {save_name}")


            save_dtms_data = drive_api.dtms_data(base_url, click_folder_name, save_name)
            # print(f"save_dtms_data: {save_dtms_data}")

            save_http_status = drive_api.dtms_save_api(base_url, click_folder_name, save_dtms_data, save_name)
            print(f"save_http_status Code: {save_http_status.status_code}")

            assert save_http_status.status_code <= 200, "DTMS save failed"


        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()

            # dtms_info_path, dtms_info_filename = canvas_page.save_set('folder', dtms_info_file)
            # time.sleep(2)
            # dtms_data = canvas_page.dtms_info(dtms_info_path, dtms_info_filename)
            # time.sleep(2)


    def tesot_canvas_fileadd_root_save(self, base_url):

        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        try:
            today = datetime.datetime.now().strftime('%Y_%m_%d_')
            input_multiline = multi_line()
            page_max = len(input_multiline)  # 페이지 최대 수

            start_x = 585  # 캔버스 첫 칸의 x 좌표
            start_y = 425  # 캔버스 첫 칸의 y 좌표

            self.canvas_login(base_url)
            main_page.canvas_btn_click()
            time.sleep(1)

            print("\r\n추가 할 페이지 수: {}".format(page_max - 1))

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

            canvas_page.add_btn_click()
            time.sleep(5)
            canvas_page.file_open("file")
            time.sleep(7)
            canvas_page.save_btn_click()
            time.sleep(5)
            canvas_page.save_set(today + "automation_file")
            time.sleep(1)
            canvas_page.save_confirm_btn_click()
            time.sleep(30)

            save_name = canvas_page.save_filename()
            time.sleep(8)
            print(f"save_name: {save_name}")

            # save_dtms_data = drive_api.dtms_data('ROOT', "pocket_kr")
            # create_http_status = dtms_create_api('ROOT', today + "_automation_test", save_dtms_data)
            # assert create_http_status.status_code <= 201, "DTMS created failed"
            # print(f"create_http_status Code: {create_http_status.status_code}")

            save_dtms_data = drive_api.dtms_data(base_url, save_name)
            # print(f"save_dtms_data: {save_dtms_data}")

            # file_key_result = drive_api.file_key_searchi(base_url, save_name)
            # print(f"머가나올까: {file_key_result}")

            # drive_api.dtms_save_api(base_url, save_name, save_dtms_data)
            save_http_status = drive_api.dtms_save_api(base_url, save_name, save_dtms_data)
            print(f"save_http_status Code: {save_http_status.status_code}")
            assert save_http_status.status_code <= 200, "DTMS save failed"


        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()

    def tesot_canvas_fileadd_folder_save(self, base_url):

        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        drive_api = Drive_api(base_url)

        try:
            today = datetime.datetime.now().strftime('%Y_%m_%d_')
            input_multiline = multi_line()
            page_max = len(input_multiline)  # 페이지 최대 수

            start_x = 585  # 캔버스 첫 칸의 x 좌표
            start_y = 425  # 캔버스 첫 칸의 y 좌표

            self.canvas_login(base_url)
            main_page.canvas_btn_click()
            time.sleep(1)

            print("\r\n추가 할 페이지 수: {}".format(page_max - 1))

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

            canvas_page.add_btn_click()
            time.sleep(5)
            canvas_page.file_open("folder")
            time.sleep(7)

            canvas_page.save_btn_click()
            time.sleep(5)
            canvas_page.save_set(today + "automation_file")
            time.sleep(1)
            canvas_page.save_confirm_btn_click()
            time.sleep(30)

            save_name = canvas_page.save_filename()
            time.sleep(8)

            print(f"save_name: {save_name}")

            # save_dtms_data = drive_api.dtms_data('ROOT', "pocket_kr")
            # create_http_status = dtms_create_api('ROOT', today + "_automation_test", save_dtms_data)
            # assert create_http_status.status_code <= 201, "DTMS created failed"
            # print(f"create_http_status Code: {create_http_status.status_code}")

            save_dtms_data = drive_api.dtms_data(base_url, today + "automation_file")
            # print(f"save_dtms_data: {save_dtms_data}")

            save_http_status = drive_api.dtms_save_api(base_url, save_name, save_dtms_data)
            print(f"save_http_status Code: {save_http_status.status_code}")

            assert save_http_status.status_code <= 200, "DTMS save failed"


        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()

    def tesot_canvas_drawing(self, base_url):

        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)

        try:
            input_multiline = multi_line()
            page_max = len(input_multiline)  # 페이지 최대 수

            start_x = 585  # 캔버스 첫 칸의 x 좌표
            start_y = 425  # 캔버스 첫 칸의 y 좌표

            self.canvas_login(base_url)
            main_page.canvas_btn_click()
            time.sleep(1)

            print("\r\n추가 할 페이지 수: {}".format(page_max - 1))

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

        except AssertionError as e:
            print(f"AssertionError: {e}")
            canvas_page.screenshot_capture()