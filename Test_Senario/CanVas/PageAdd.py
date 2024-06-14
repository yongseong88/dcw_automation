import random
import time

from selenium.common import ElementClickInterceptedException
from Pages.Base_Page import BasePage
from Pages.Canvas_Page import CanVasPage
from Utilities.Locators import canvas_LocatorFields

class PageAdd_Senario(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locate = canvas_LocatorFields
        self.canvas_page = CanVasPage(self.driver)

    def DTMS_create(self):
        drawing_tool = self.canvas_page.tool_list(self.locate.tool_list)
        page_max = 100  # 페이지 최대 수
        page_add_number = random.randrange(1, page_max + 1)  # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)
        start_x = 565  # 캔버스 첫 칸의 x 좌표
        start_y = 413  # 캔버스 첫 칸의 y 좌표
        page_info = []  # 추가한 페이지에 대한 정보를 담는 배열 선언
        drawing_info = []

        for dr in drawing_tool:
            tool_value = dr.get_attribute("aria-label")
            shortcut_key_info = tool_value.find("(")  # // 도구명 뒤에 있는 단축키 안내 부분 체크
    
            if shortcut_key_info != -1:
              tool_element = tool_value[0:(shortcut_key_info - 1)]

            else:
              tool_element = tool_value

            match tool_element:
              case '펜':
                drawing_info.append(dr)
              case '수직 미러 펜':
                drawing_info.append(dr)
              case '채우기':
                drawing_info.append(dr)
              case '선':
                drawing_info.append(dr)
              case '사각형':
                drawing_info.append(dr)
              case '원':
                drawing_info.append(dr)
              case '삼각형':
                drawing_info.append(dr)
              case _:
                pass

        print("추가 할 페이지 수: {}".format(page_add_number))

        for pg in range(page_add_number):
            random.shuffle(drawing_info)

            for dl in drawing_info:
                tool_value = dl.get_attribute("aria-label")
                shortcut_key_info = tool_value.find("(")  # // 도구명 뒤에 있는 단축키 안내 부분 체크

                if shortcut_key_info != -1:
                    tool_element = tool_value[0:(shortcut_key_info - 1)]
                else:
                    tool_element = tool_value

                match pg:
                    case 0:
                        match tool_element:
                            case '펜':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁 추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '수직 미러 펜':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '채우기':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '선':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '사각형':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '원':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '삼각형':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case _:
                                pass
                                break

                    case _:
                        start_y = 430  # 캔버스 첫 칸의 y 좌표
                        match tool_element:
                            case '펜':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁 추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '수직 미러 펜':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '채우기':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '선':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '사각형':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '원':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case '삼각형':
                                dl.click()  # // 전체 도구 중 임의의 도구 클릭
                                tooltip = dl.text  # // 클릭 한 도구 툴팁  추출
                                print(
                                    "클릭한 도구: {}".format(
                                        tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
                                print("도구 툴팁: {}".format(tooltip))
                                self.canvas_page.drawing_drag(start_x, start_y)
                                self.canvas_page.page_add_btn_click(self.locate.canvas_add_btn)
                                page_info.append(pg)  # 배열에 추가한 페이지 수 카운트 추가
                                print("추가된 페이지 정보: {} / {}".format(pg + 1, page_add_number+1))
                                break

                            case _:
                                pass
                                break
        time.sleep(5)
        print("추가된 페이지 수는 {0} 입니다".format(page_add_number+1))

    def description_input(self, description):
        # 캔버스 내 페이지 설명 작성 시나리오
        self.set(self.locate.canvas_description_btn, description) # // 페이지 설명 선택 후 텍스트 작성