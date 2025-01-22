import time
from random import random

import pytest

from TestCase.base_test import BaseTest
from Pages.Canvas_Page import CanVasPage
from Pages.Login_page import LoginPage
from Pages.Main_Page import MainPage
from Utilities.File_util import multi_line
from Utilities.configreaderutil import readConfig
import random

from Utilities.json_util import Braille_api


@pytest.mark.usefixtures("initialize_driver", "base_url")
class TestCanvasfileadministration(BaseTest):

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

    def tesot_canvas_pagemax(self, base_url):
        # MainPage 인스턴스 생성
        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)

        self.canvas_login(base_url)
        main_page.canvas_btn_click()
        time.sleep(1)

        page_max = 100 # 페이지 최대 수

        for pg in range(page_max+1):
            if pg == 0:
               #  print("\r\n 페이지 정보: {} / {}".format(1, page_max))
               # canvas_page.page_add_btn_click()
                print("페이지 정보: {} / {}".format(pg + 1, page_max))
                # time.sleep(2)

            elif pg < page_max:
                print("\r\n페이지 정보: {} / {}".format(pg + 1, page_max))
                canvas_page.page_add_btn_click()
                print("페이지 정보: {} / {}".format(pg + 1, page_max))
                time.sleep(1.5)
            else:
                # print("\r\n 페이지 정보: {} / {}".format(1, page_max))
                canvas_page.key_event('n')


        print("총 페이지 수는 {0} 입니다".format(page_max))
        print(f"최대 페이지 aria-label: {canvas_page.page_max_label()}")
        time.sleep(0.5)

        assert canvas_page.page_max_label() == "최대 100페이지까지 가능합니다.", "failed"

    def test_canvas_page_multiline(self, base_url):
        # MainPage, CanVasPage 인스턴스 생성
        main_page = MainPage(self.driver)
        canvas_page = CanVasPage(self.driver)
        braille_api = Braille_api(base_url)

        # page_add_number = random.randrange(1, page_max+1)  # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)
        input_multiline = multi_line()
        page_max = len(input_multiline)  # 페이지 최대 수

        self.canvas_login(base_url)
        time.sleep(1)
        main_page.canvas_btn_click()
        time.sleep(5)

        print("\r\n추가 할 페이지 수: {}".format(page_max))

        for pg in range(page_max):
          if 0 < pg: # 두번째 페이지 부터 페이지
                canvas_page.page_add_btn_click() # 페이지 추가
                if len(input_multiline) > pg: # 멀티라인 입력 가능 텍스트와 페이지수를 비교하는 로직
                    print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
                    canvas_page.description_input(input_multiline[pg])
                    multiline_input_http_status = braille_api.multiline_api(pg + 1, input_multiline[pg], base_url)
                    print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
                    print("페이지 정보: {} / {}".format(pg + 1, page_max))
                    print(f"Status Code: {multiline_input_http_status.status_code}\r\n")
                    assert multiline_input_http_status.status_code == 200, "multiline input Failed"

                    time.sleep(2)

                elif len(input_multiline) < pg:
                    print("입력 가능 한 멀티라인 텍스트가 없어요.")
                    print("페이지 정보: {} / {}".format(pg + 1, page_max))
                    time.sleep(2)

          else: # 첫 페이지
              print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
              canvas_page.description_input(input_multiline[pg])
              multiline_input_http_status = braille_api.multiline_api(pg + 1, input_multiline[pg], base_url)
              print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
              print("페이지 정보: {} / {}".format(1, page_max))
              print(f"Status Code: {multiline_input_http_status.status_code}")
              assert multiline_input_http_status.status_code == 200, "multiline input Failed"

        print("총 페이지 수는 {0} 입니다".format(page_max))

#
#     def tesot_canvas_multiline(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         input_text = "양지은"
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(5)
#
#         # canvas_page.page_add_btn_click()
#         canvas_page.description_input(input_text)
#
#         multiline_input_http_status = multiline_api(input_text)
#         print(f"\r\nStatus Code: {multiline_input_http_status.status_code}")
#         assert multiline_input_http_status.status_code == 200, "multiline input Failed"