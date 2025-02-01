import time
import pytest
from Pages.Cloud_Page import CloudPage
from TestCase.base_test import BaseTest
from Utilities.configreaderutil import readConfig
from Pages.Login_page import LoginPage
from Pages.Main_Page import MainPage
from Utilities.json_util import File_group_api, Drive_api

@pytest.mark.usefixtures("initialize_driver", "base_url")
class TestCloudfilopen(BaseTest):

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

    def tesot_cloud_page_click(self, base_url):
        try:
            main_page = MainPage(self.driver)
            cloud_page = CloudPage(self.driver)

            file_api = File_group_api(base_url)

            self.canvas_login(base_url)
            time.sleep(1)
            main_page.cloud_btn_click()
            time.sleep(8)
            # cloud_page.file_info()
            # time.sleep(8)
            selected_page = cloud_page.page_click(base_url)
            print(f"selected_page: {selected_page}")
            time.sleep(5)

            cloud_list_http_Status = file_api.cloud_group_list_api(base_url, selected_page, 'ROOT')
            print(f"cloud_list_http_Status Code: {cloud_list_http_Status.status_code}")
            assert cloud_list_http_Status.status_code == 200, "page_click failed"

        except AssertionError as e:
            print(f"\n에러가 발생했습니다: {e}")
            cloud_page.screenshot_capture()


    def tesot_cloud_root_DTMS_contextclick(self, base_url):
        try:
            main_page = MainPage(self.driver)
            cloud_page = CloudPage(self.driver)
            drive_api = Drive_api(base_url)
            file_api = File_group_api(base_url)

            self.canvas_login(base_url)
            time.sleep(1)
            main_page.cloud_btn_click()
            time.sleep(3)

            click_file_name = None
            while click_file_name is None:
                try:
                    click_file_name = cloud_page.file_context_click(base_url, "file", "DTMS")
                    time.sleep(8)

                    if click_file_name is None:
                        print(f"click_file_name이 {click_file_name}입니다.")

                    elif len(click_file_name) == 3:
                        clickable_folder = click_file_name[0]
                        clickable_file = click_file_name[1]
                        page_info = click_file_name[2]

                        print(f"test_clickable_folder: {clickable_folder}")
                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    elif len(click_file_name) == 2:
                        clickable_file = click_file_name[0]
                        page_info = click_file_name[1]

                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    else:
                        print("흐규흐규 ㅜㅜ")

                except Exception as e:
                    print(f"파일 더블 클릭 중 에러 발생: {e}")
                    time.sleep(3)
                    print("다시 클라우드 페이지로 이동 합니다")
                    main_page.page_refresh()
                    time.sleep(5)

            file_key = drive_api.file_key_search(base_url, clickable_file)
            cloud_list_http = file_api.cloud_group_list_api(base_url, page_info, 'ROOT')
            file_open_confirm_http = drive_api.file_open_api(base_url, file_key)

            print(f"cloud_list_http_Status Code: {cloud_list_http.status_code}")
            print(f"\r\nfile_open_confirm_http_Status Code: {file_open_confirm_http.status_code}")

            assert cloud_list_http.status_code == 200, "page_click failed"
            assert file_open_confirm_http.status_code == 200, "FileOpen failed"

        except AssertionError as e:
            print(f"\n에러가 발생했습니다: {e}")
            cloud_page.screenshot_capture()










    def tesot_cloud_root_DTMS_doubleclick(self, base_url):
        try:
            main_page = MainPage(self.driver)
            cloud_page = CloudPage(self.driver)
            drive_api = Drive_api(base_url)
            file_api = File_group_api(base_url)

            self.canvas_login(base_url)
            time.sleep(1)
            main_page.cloud_btn_click()
            time.sleep(3)

            click_file_name = None
            while click_file_name is None:
                try:
                    click_file_name = cloud_page.file_double_click(base_url, "file", "DTMS")
                    time.sleep(8)

                    if click_file_name is None:
                        print(f"click_file_name이 {click_file_name}입니다.")

                    elif len(click_file_name) == 3:
                        clickable_folder = click_file_name[0]
                        clickable_file = click_file_name[1]
                        page_info = click_file_name[2]

                        print(f"test_clickable_folder: {clickable_folder}")
                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    elif len(click_file_name) == 2:
                        clickable_file = click_file_name[0]
                        page_info = click_file_name[1]

                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    else:
                        print("흐규흐규 ㅜㅜ")

                except Exception as e:
                    print(f"파일 더블 클릭 중 에러 발생: {e}")
                    time.sleep(3)
                    print("다시 클라우드 페이지로 이동 합니다")
                    main_page.page_refresh()
                    time.sleep(5)

            file_key = drive_api.file_key_search(base_url, clickable_file)
            cloud_list_http = file_api.cloud_group_list_api(base_url, page_info, 'ROOT')
            file_open_confirm_http = drive_api.file_open_api(base_url, file_key)

            print(f"cloud_list_http_Status Code: {cloud_list_http.status_code}")
            print(f"\r\nfile_open_confirm_http_Status Code: {file_open_confirm_http.status_code}")

            assert cloud_list_http.status_code == 200, "page_click failed"
            assert file_open_confirm_http.status_code == 200, "FileOpen failed"

        except AssertionError as e:
            print(f"\n에러가 발생했습니다: {e}")
            cloud_page.screenshot_capture()

    def tesot_cloud_root_DTMA_doubleclick(self, base_url):
        try:
            main_page = MainPage(self.driver)
            cloud_page = CloudPage(self.driver)
            drive_api = Drive_api(base_url)
            file_api = File_group_api(base_url)

            self.canvas_login(base_url)
            time.sleep(1)
            main_page.cloud_btn_click()
            time.sleep(3)

            click_file_name = None
            while click_file_name is None:
                try:
                    click_file_name = cloud_page.file_double_click(base_url, "file", "DTMA")
                    time.sleep(8)

                    if click_file_name is None:
                        print(f"click_file_name이 {click_file_name}입니다.")

                    elif len(click_file_name) == 3:
                        clickable_folder = click_file_name[0]
                        clickable_file = click_file_name[1]
                        page_info = click_file_name[2]

                        print(f"test_clickable_folder: {clickable_folder}")
                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    elif len(click_file_name) == 2:
                        clickable_file = click_file_name[0]
                        page_info = click_file_name[1]

                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    else:
                        print("흐규흐규 ㅜㅜ")

                except Exception as e:
                    print(f"파일 더블 클릭 중 에러 발생: {e}")
                    time.sleep(3)
                    print("다시 클라우드 페이지로 이동 합니다")
                    main_page.page_refresh()
                    time.sleep(5)

            file_key = drive_api.file_key_search(base_url, clickable_file)
            cloud_list_http = file_api.cloud_group_list_api(base_url, page_info, 'ROOT')
            file_open_confirm_http = drive_api.file_open_api(base_url, file_key)

            print(f"cloud_list_http_Status Code: {cloud_list_http.status_code}")
            print(f"\r\nfile_open_confirm_http_Status Code: {file_open_confirm_http.status_code}")

            assert cloud_list_http.status_code == 200, "page_click failed"
            assert file_open_confirm_http.status_code == 200, "FileOpen failed"

        except AssertionError as e:
            print(f"\n에러가 발생했습니다: {e}")
            cloud_page.screenshot_capture()

    def tesot_cloud_folder_DTMS_doubleclick(self, base_url):
        try:
            main_page = MainPage(self.driver)
            cloud_page = CloudPage(self.driver)
            drive_api = Drive_api(base_url)
            file_api = File_group_api(base_url)

            self.canvas_login(base_url)
            time.sleep(1)
            main_page.cloud_btn_click()
            time.sleep(3)

            click_file_name = None
            while click_file_name is None:
                try:
                    click_file_name = cloud_page.file_double_click(base_url, "folder", "DTMS")
                    time.sleep(8)

                    if click_file_name is None:
                        print(f"click_file_name이 {click_file_name}입니다.")

                    elif len(click_file_name) == 3:
                        clickable_folder = click_file_name[0]
                        clickable_file = click_file_name[1]
                        page_info = click_file_name[2]

                        print(f"test_clickable_folder: {clickable_folder}")
                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    elif len(click_file_name) == 2:
                        clickable_file = click_file_name[0]
                        page_info = click_file_name[1]

                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    else:
                        print("흐규흐규 ㅜㅜ")

                except Exception as e:
                    print(f"파일 더블 클릭 중 에러 발생: {e}")
                    time.sleep(3)
                    print("다시 클라우드 페이지로 이동 합니다")
                    main_page.page_refresh()
                    time.sleep(5)

            file_key = drive_api.file_key_search(base_url, clickable_folder, clickable_file)
            cloud_list_http = file_api.cloud_group_list_api(base_url, page_info, file_key[1])
            file_open_confirm_http = drive_api.file_open_api(base_url, file_key[1])

            print(f"cloud_list_http_Status Code: {cloud_list_http.status_code}")
            print(f"\r\nfile_open_confirm_http_Status Code: {file_open_confirm_http.status_code}")

            assert cloud_list_http.status_code == 200, "page_click failed"
            assert file_open_confirm_http.status_code == 200, "FileOpen failed"

        except AssertionError as e:
            print(f"\n에러가 발생했습니다: {e}")
            cloud_page.screenshot_capture()

    def tesot_cloud_folder_DTMA_doubleclick(self, base_url):
        try:
            main_page = MainPage(self.driver)
            cloud_page = CloudPage(self.driver)
            drive_api = Drive_api(base_url)
            file_api = File_group_api(base_url)

            self.canvas_login(base_url)
            time.sleep(1)
            main_page.cloud_btn_click()
            time.sleep(3)

            click_file_name = None
            while click_file_name is None:
                try:
                    click_file_name = cloud_page.file_double_click(base_url, "folder", "DTMA")
                    time.sleep(8)

                    if click_file_name is None:
                        print(f"click_file_name이 {click_file_name}입니다.")

                    elif len(click_file_name) == 3:
                        clickable_folder = click_file_name[0]
                        clickable_file = click_file_name[1]
                        page_info = click_file_name[2]

                        print(f"test_clickable_folder: {clickable_folder}")
                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    elif len(click_file_name) == 2:
                        clickable_file = click_file_name[0]
                        page_info = click_file_name[1]

                        print(f"test_clickable_file: {clickable_file}")
                        print(f"test_page_info: {page_info}")

                    else:
                        print("흐규흐규 ㅜㅜ")

                except Exception as e:
                    print(f"파일 더블 클릭 중 에러 발생: {e}")
                    time.sleep(3)
                    print("다시 클라우드 페이지로 이동 합니다")
                    main_page.page_refresh()
                    time.sleep(5)

            file_key = drive_api.file_key_search(base_url, clickable_folder, clickable_file)
            cloud_list_http = file_api.cloud_group_list_api(base_url, page_info, file_key[1])
            file_open_confirm_http = drive_api.file_open_api(base_url, file_key[1])

            print(f"cloud_list_http_Status Code: {cloud_list_http.status_code}")
            print(f"\r\nfile_open_confirm_http_Status Code: {file_open_confirm_http.status_code}")

            assert cloud_list_http.status_code == 200, "page_click failed"
            assert file_open_confirm_http.status_code == 200, "FileOpen failed"

        except AssertionError as e:
            print(f"\n에러가 발생했습니다: {e}")
            cloud_page.screenshot_capture()
