# import time
# from random import random
# from TestCase.base_test import BaseTest
# from Pages.Canvas_Page import CanVasPage
# from Pages.Login_page import LoginPage
# from Pages.Main_Page import MainPage
# from Utilities.File_util import multi_line
# from Utilities.configreaderutil import readConfig
# from Utilities.json_util import user_api, filebrowser_list_api, file_open_api, dtms_create_api, dtms_save_api
# import random
#
#
# class TestCanvas(BaseTest):
#     user_id = readConfig("Account", "id")
#     user_pwd = readConfig("Account", "password")
#
#     def canvas_login(self):
#         login_page = LoginPage(self.driver)
#         main_page = MainPage(self.driver)
#
#         main_page.login_btn_click()
#         login_page.set_id(self.user_id)
#         login_page.set_pwd(self.user_pwd)
#         login_page.login_submit()
#
#     def tesot_canvas_click(self):
#         # MainPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#
#         self.canvas_login()
#         main_page.canvas_btn_click()
#
#         http_status = user_api()
#         print(f"\r\nStatus Code: {http_status.status_code}")
#         assert http_status.status_code == 200, "CanVas Click Failed"
#
#     def tesot_canvas_open_popup(self):
#         # MainPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         main_page.canvas_btn_click()
#         time.sleep(1)
#         canvas_page.open_btn_click()
#         time.sleep(7)
#
#         http_status = filebrowser_list_api('ROOT')
#         print(f"\r\nStatus Code: {http_status.status_code}")
#         assert http_status.status_code == 200, "failed"
#
#     def tesot_canvas_pagemax(self):
#         # MainPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         main_page.canvas_btn_click()
#         time.sleep(1)
#
#         page_max = 100  # 페이지 최대 수
#
#         for pg in range(page_max):
#             if pg > 0:
#                 canvas_page.page_add_btn_click()
#                 print("페이지 정보: {} / {}".format(pg + 1, page_max))
#                 time.sleep(2)
#
#             elif pg == page_max:
#                 print("페이지 정보: {} / {}".format(pg + 1, page_max))
#             else:
#                 print("페이지 정보: {} / {}".format(1, page_max))
#
#         print("총 페이지 수는 {0} 입니다".format(page_max))
#
#         time.sleep(7)
#
#         max_toast = canvas_page.page_add_max_text
#
#         assert max_toast == "최대 100페이지까지 가능합니다.", "failed"
#
#     def tesot_canvas_open_cancel(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         main_page.canvas_btn_click()
#         time.sleep(1)
#         canvas_page.open_btn_click()
#         time.sleep(1)
#         canvas_page.filebrowser_cancel_btn_click()
#         time.sleep(2)
#
#     def tesot_canvas_root_file_open(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         main_page.canvas_btn_click()
#         time.sleep(1)
#         canvas_page.open_btn_click()
#         time.sleep(7)
#
#         root_file_open = canvas_page.file_open("file")
#         time.sleep(3)
#
#         http_status = file_open_api(root_file_open)
#         print(f"\r\nStatus Code: {http_status.status_code}")
#         assert http_status.status_code == 200, "failed"
#
#     def tesot_canvas_folder_file_open(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         main_page.canvas_btn_click()
#         time.sleep(1)
#         canvas_page.open_btn_click()
#         time.sleep(7)
#
#         folder_file_open = canvas_page.file_open("folder")
#         time.sleep(3)
#
#         http_status = file_open_api(folder_file_open)
#         print(f"\r\nStatus Code: {http_status.status_code}")
#         assert http_status.status_code == 200, "failed"
#
#     def tesot_canvas_add_popup(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(1)
#         canvas_page.add_btn_click()
#         time.sleep(5)
#
#         http_status = filebrowser_list_api('ROOT')
#         print(f"\r\nStatus Code: {http_status.status_code}")
#         assert http_status.status_code == 200, "failed"
#
#     def tesot_canvas_add_cancel(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(1)
#         canvas_page.add_btn_click()
#         time.sleep(5)
#         canvas_page.filebrowser_cancel_btn_click()
#         time.sleep(2)
#
#     def tesot_canvas_root_file_add(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(1)
#         canvas_page.add_btn_click()
#         time.sleep(5)
#
#         root_file_open = canvas_page.file_open("file")
#         time.sleep(3)
#
#         http_status = file_open_api(root_file_open)
#         print(f"\r\nStatus Code: {http_status.status_code}")
#         assert http_status.status_code == 200, "failed"
#
#
#     def tesot_canvas_folder_file_add(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(1)
#         canvas_page.add_btn_click()
#         time.sleep(5)
#
#         folder_file_open = canvas_page.file_open("folder")
#         time.sleep(3)
#
#         http_status = file_open_api(folder_file_open)
#         print(f"\r\nStatus Code: {http_status.status_code}")
#         assert http_status.status_code == 200, "failed"
#
#     def tesot_canvas_page_add(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         page_max = 10  # 페이지 최대 수
#         page_add_number = random.randrange(1, page_max+1)  # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(5)
#
#         print("\r\n추가 할 페이지 수: {}".format(page_add_number))
#
#         for pg in range(page_add_number+1):
#           if 0 < pg:
#                 canvas_page.page_add_btn_click()
#                 print("페이지 정보: {} / {}".format(pg + 1, page_add_number + 1))
#                 time.sleep(2)
#
#           else:
#             print("페이지 정보: {} / {}".format(1, page_add_number + 1))
#
#         print("총 페이지 수는 {0} 입니다".format(page_add_number+1))
#         assert pg == page_add_number, "page add failed"
#
#     def tesot_canvas_page_add_max(self):
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         page_max = 100  # 페이지 최대 수
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(5)
#
#         print("\r\n추가 할 페이지 수: {}".format(page_max))
#
#         for pg in range(page_max + 1):
#             if pg > 0:
#                 canvas_page.page_add_btn_click()
#                 print("페이지 정보: {} / {}".format(pg + 1, page_max + 1))
#                 time.sleep(2)
#
#             else:
#                 print("페이지 정보: {} / {}".format(1, page_max + 1))
#
#         print("총 페이지 수는 {0} 입니다".format(page_max + 1))
#         assert pg == page_max, "page add failed"
#
#     def tesot_canvas_drawing(self):
#
#         # MainPage, CanVasPage 인스턴스 생성
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         start_x = 565  # 캔버스 첫 칸의 x 좌표
#         start_y = 415  # 캔버스 첫 칸의 y 좌표
#         page_max = 10  # 페이지 최대 수
#         page_add_number = random.randrange(1, page_max + 1)  # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(1)
#
#         # tool_list = canvas_page.drawing_tool()
#
#         # print("\r\ndrawing 가능 한 도구의 갯수: {}".format(len(tool_list)))
#         print("\r\n추가 할 페이지 수: {}".format(page_add_number))
#
#         for pg in range(page_add_number + 1):
#             scroll_y_location = canvas_page.scroll()
#
#             if scroll_y_location == 8:
#                 start_y = (start_y - 20)
#
#             canvas_page.drawing_tool(start_x, start_y)
#             canvas_page.page_add_btn_click()
#             print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number + 1))
#
#         assert pg == page_add_number, "drawing failed"
#
#     def tesot_canvas_save(self):
#
#         main_page = MainPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#
#         self.canvas_login()
#         time.sleep(1)
#         main_page.canvas_btn_click()
#         time.sleep(1)
#
#         page_max = 6  # 페이지 최대 수
#         page_add_number = random.randrange(1, page_max + 1)  # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)
#
#         start_x = 565  # 캔버스 첫 칸의 x 좌표
#         start_y = 415  # 캔버스 첫 칸의 y 좌표
#
#         input_multiline = multi_line()
#         save_file_name = "쿵쿵따리쿵쿵따"
#
#         tool_list = canvas_page.drawing_tool()
#
#         print("\r\ndrawing 가능 한 도구의 갯수: {}".format(len(tool_list)))
#         print("추가 할 페이지 수: {}".format(page_add_number))
#
#         for pg in range(page_add_number + 1):
#             for tl in tool_list:
#                 tool_value = tl.get_attribute("aria-label")
#
#                 if tool_value.find("(") != -1:
#                     tool_element = tool_value[0:(tool_value.find("(") - 1)]
#                 else:
#                     tool_element = tool_value
#
#             if pg > 0:
#                 canvas_page.page_add_btn_click()
#                 random.shuffle(tool_list)
#                 match len(input_multiline):
#                     case length if length > pg:
#                         match tool_element:
#                             case '채우기':
#                                 tl.click()  # // 전체 도구 중 임의의 도구 클릭
#                                 tooltip = tl.text  # // 클릭 한 도구 툴팁  추출
#                                 print(
#                                     "클릭한 도구: {}".format(
#                                         tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
#                                 print("도구 툴팁: {}".format(tooltip))
#                                 canvas_page.drawing_click(start_x, start_y)
#                                 print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
#                                 canvas_page.description_input(input_multiline[pg])
#                                 print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
#                                 print("페이지 정보: {} / {}".format(pg + 1, page_add_number + 1))
#                                 time.sleep(2)
#                                 # break
#
#                             case _:
#                                 tl.click()  # // 전체 도구 중 임의의 도구 클릭
#                                 tooltip = tl.text  # // 클릭 한 도구 툴팁  추출
#                                 print(
#                                     "클릭한 도구: {}".format(
#                                         tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
#                                 print("도구 툴팁: {}".format(tooltip))
#                                 canvas_page.drawing_drag(start_x, start_y)
#                                 print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
#                                 canvas_page.description_input(input_multiline[pg])
#                                 print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
#                                 print("페이지 정보: {} / {}".format(pg + 1, page_add_number + 1))
#                                 time.sleep(2)
#                                 # break
#
#                     case length if length < pg:
#                         match tool_element:
#                             case '채우기':
#                                 tl.click()  # // 전체 도구 중 임의의 도구 클릭
#                                 tooltip = tl.text  # // 클릭 한 도구 툴팁  추출
#                                 print(
#                                     "클릭한 도구: {}".format(
#                                         tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
#                                 print("도구 툴팁: {}".format(tooltip))
#                                 canvas_page.drawing_click(start_x, start_y)
#                                 print("입력 가능 한 멀티라인 텍스트가 없어요.")
#                                 print("페이지 정보: {} / {}".format(pg + 1, page_add_number + 1))
#                                 time.sleep(2)
#                                 # break
#
#                             case _:
#                                 tl.click()  # // 전체 도구 중 임의의 도구 클릭
#                                 tooltip = tl.text  # // 클릭 한 도구 툴팁  추출
#                                 print(
#                                     "클릭한 도구: {}".format(
#                                         tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
#                                 print("도구 툴팁: {}".format(tooltip))
#                                 canvas_page.drawing_drag(start_x, start_y)
#                                 print("입력 가능 한 멀티라인 텍스트가 없어요.")
#                                 print("페이지 정보: {} / {}".format(pg + 1, page_add_number + 1))
#                                 time.sleep(2)
#                                 # break
#
#             else:
#                 random.shuffle(tool_list)
#                 match tool_element:
#                     case '채우기':
#                         tl.click()  # // 전체 도구 중 임의의 도구 클릭
#                         tooltip = tl.text  # // 클릭 한 도구 툴팁  추출
#                         print(
#                             "클릭한 도구: {}".format(
#                                 tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
#                         print("도구 툴팁: {}".format(tooltip))
#                         canvas_page.drawing_click(start_x, start_y)
#                         print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
#                         canvas_page.description_input(input_multiline[pg])
#                         print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
#                         print("페이지 정보: {} / {}".format(pg + 1, page_add_number + 1))
#                         time.sleep(2)
#                         start_y = ((start_y) - 100)
#                         # break
#
#                     case _:
#                         tl.click()  # // 전체 도구 중 임의의 도구 클릭
#                         tooltip = tl.text  # // 클릭 한 도구 툴팁  추출
#                         print(
#                             "클릭한 도구: {}".format(
#                                 tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
#                         print("도구 툴팁: {}".format(tooltip))
#                         canvas_page.drawing_drag(start_x, start_y)
#                         print(f"멀티라인 입력 가능 길이: {len(input_multiline)}")
#                         canvas_page.description_input(input_multiline[pg])
#                         print(f"멀티라인 입력 텍스트: {input_multiline[pg]}")
#                         print("페이지 정보: {} / {}".format(pg + 1, page_add_number + 1))
#                         time.sleep(2)
#
#
#         canvas_page.save_btn_click()
#         time.sleep(7)
#         canvas_page.save_set(save_file_name)
#         time.sleep(3)
#         canvas_page.save_confirm_btn_click()
#         time.sleep(12)
#
#         create_http_status = dtms_create_api("ROOT", save_file_name)
#         save_http_status = dtms_save_api("ROOT", save_file_name)
#         print(f"\r\nStatus Code: {create_http_status.status_code}")
#         print(f"Status Code: {save_http_status.status_code}")
#         assert create_http_status.status_code <= 201, "DTMS created failed"
#         assert save_http_status.status_code <= 200, "DTMS save failed"
#
#     def tesot_canvas_saveAs(self):
#         user_id = readConfig("Account", "id")
#         user_pwd = readConfig("Account", "password")
#
#         login_page = LoginPage(self.driver)
#         canvas_page = CanVasPage(self.driver)
#         login_page.login_btn_click()
#         login_page.set_id(user_id)
#         login_page.set_pwd(user_pwd)
#         login_page.login_submit()
#         canvas_page.canvas_btn_click()
#         canvas_page.tool_btn_click()
#         canvas_page.drawing_drag()
#         canvas_page.description_btn_click("나는 행복 합니다.")
#         canvas_page.DTMS_Save("test1234")
#         canvas_page.page_add()
#         canvas_page.DTMS_SaveAs("dobbu")
#
#
#     def tesot_Dotpad_connect(self):
#         canvas_page = CanVasPage(self.driver)
#         canvas_page.add_dotpad()
