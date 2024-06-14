import random
import time
from selenium.webdriver.common.by import By
from Pages.Base_Page import BasePage
# from Pages.canvas_tool import Canvas_Tool
from Utilities.Locators import canvas_LocatorFields
from Utilities.configreaderutil import readConfig


class SavePage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    # super().__init__(driver)
    # self.locate = canvas_LocatorFields

  def DTMS_Save(self, locator):
    self.click(locator)
    time.sleep(3)

  # def canvas_click(self):
  #   # 캔버스 진입 시나리오
  #   self.get_element(self.locate.canvas_button)
  #   self.click(self.locate.canvas_button)
  #   # print("뭐라고 뜨지? ", canvas_btn)
  #   # print(self.get_text(self.canvas_btn))



  # def tool_btn(self):
  #   # 닷 캔버스에서 제공 되는 도구 선택하는 시나리오
  #   tool_list = self.get_element(self.tool_list) # 닷 캔버스 내 사용 가능한 도구 리스트 추출
  #   return tool_list

  # def drawing_drag(self):
  #   # 캔버스 내 300셀에 drawing 하는 시나리오
  #
  #   # 드로잉 시작점 설정
  #   start_x = int(readConfig("Canvas_locator", "start_x")) # 캔버스 첫 칸의 x 좌표
  #   end_x = int(readConfig("Canvas_locator", "end_x"))  # 캔버스 마지막 칸의 x 좌표
  #
  #   start_y = int(readConfig("Canvas_locator", "start_y"))   # 캔버스 첫 칸의 y 좌표
  #   end_y = int(readConfig("Canvas_locator", "end_y"))  # 캔버스 마지막 칸의 y 좌표
  #
  #   coordinate_arr = []
  #
  #   for i in range(2):
  #     coordinate_arr.append([])
  #     for coo_xy in range(1):
  #       x_ran_num = random.randrange(start_x, end_x + 1)
  #       y_ran_num = random.randrange(start_y, end_y + 1)
  #
  #       coordinate_arr[i].append(x_ran_num)
  #       coordinate_arr[i].append(y_ran_num)
  #
  #   for cnt in range(len(coordinate_arr)):
  #     x, y = coordinate_arr[cnt]
  #     if cnt == 0:
  #       self.mouse_click(x, y)
  #     else:
  #       self.mouse_drag(x, y)
  #     print(x, y)

  # def page_add(self):
  #     self.click(self.canvas_add_button)
  #
  # def DTMS_Save(self, file_name):
  #   # 파일 최초 저장 및 재 저장 하는 시나리오
  #   self.click(self.save_btn) # 저장 버튼 클릭
  #   self.set(self.save_textfield, file_name) # // 팝업 내 텍스트 박스 선택 후 저장 할 파일명 입력
  #   self.click(self.save_confirm_btn) # // 팝업 내 저장 버튼 클릭
  #
  # def canvas_drawing_save(self):
  #
  #   tool_list = Canvas_Tool.tool_btn()
  #   print("도구의 총 갯수는 {}개 입니다.".format(len(tool_list)))
  #
  #   # 페이지 추가 시나리오
  #   page_max = 100  # 페이지 최대 수 설정
  #   page_add_number = random.randrange(1, page_max + 1)  # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)
  #   page_info = []  # 추가한 페이지에 대한 정보를 담는 배열 선언
  #
  #   for pl in range(page_add_number):
  #     # print("추가 할 페이지수: ", page_add_number)
  #     random.shuffle(tool_list)
  #
  #     for dr in tool_list:
  #       Canvas_Tool.tool_btn_click(dr)
  #       self.page_add()
  #       page_info.append(pl)
  #       break


        # tool_value = dr.get_attribute("aria-label")  # // 클릭 한 도구 attribute 값 추출
        # shortcut_key_info = tool_value.find("(")  # // 도구명 뒤에 있는 단축키 안내 부분 체크
        #
        # if shortcut_key_info != -1:
        #   tool_element = tool_value[0:(shortcut_key_info - 1)]
        #
        # else:
        #   tool_element = tool_value
        #
        # match tool_element:
        #   case '펜':
        #     dr.click()  # // 전체 도구 중 임의의 도구 클릭
        #     tooltip = dr.text  # // 클릭 한 도구 툴팁 추출
        #     print(
        #       "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
        #     print("도구 툴팁: {}".format(tooltip))
        #     self.drawing_drag()
        #     self.page_add()
        #     page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
        #     print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
        #     break
        #
        #   case '수직 미러 펜':
        #     dr.click()  # // 전체 도구 중 임의의 도구 클릭
        #     tooltip = dr.text  # // 클릭 한 도구 툴팁  추출
        #     print(
        #       "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
        #     print("도구 툴팁: {}".format(tooltip))
        #     self.drawing_drag()
        #     self.page_add()
        #     page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
        #     print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
        #     break
        #
        #   case '채우기':
        #     dr.click()  # // 전체 도구 중 임의의 도구 클릭
        #     tooltip = dr.text  # // 클릭 한 도구 툴팁  추출
        #     print(
        #       "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
        #     print("도구 툴팁: {}".format(tooltip))
        #     self.drawing_drag()  # 해당 위치 까지 drag
        #     self.page_add()
        #     page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
        #     print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
        #     break
        #
        #   case '선':
        #     dr.click()  # // 전체 도구 중 임의의 도구 클릭
        #     tooltip = dr.text  # // 클릭 한 도구 툴팁  추출
        #     print(
        #       "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
        #     print("도구 툴팁: {}".format(tooltip))
        #     self.drawing_drag()
        #     self.page_add()
        #     page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
        #     print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
        #     break
        #
        #   case '사각형':
        #     dr.click()  # // 전체 도구 중 임의의 도구 클릭
        #     tooltip = dr.text  # // 클릭 한 도구 툴팁  추출
        #     print(
        #       "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
        #     print("도구 툴팁: {}".format(tooltip))
        #     self.drawing_drag()
        #     self.page_add()
        #     page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
        #     print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
        #     break
        #
        #   case '원':
        #     dr.click()  # // 전체 도구 중 임의의 도구 클릭
        #     tooltip = dr.text  # // 클릭 한 도구 툴팁  추출
        #     print(
        #       "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
        #     print("도구 툴팁: {}".format(tooltip))
        #     self.drawing_drag()
        #     self.page_add()
        #     page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
        #     print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
        #     break
        #
        #   case '삼각형':
        #     dr.click()  # // 전체 도구 중 임의의 도구 클릭
        #     tooltip = dr.text  # // 클릭 한 도구 툴팁  추출
        #     print(
        #       "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
        #     print("도구 툴팁: {}".format(tooltip))
        #     self.drawing_drag()
        #     self.page_add()
        #     page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
        #     print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
        #     break
        #
        #   case _:
        #     # tooltip = dr.text
        #     print("선택된 도구가 없어요!")
        #     pass
        #     # self.page_add()
        #     # page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
        #     # print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
        #     break

    # print("추가된 페이지 수는 {0} 입니다".format(page_add_number+1))
    # time.sleep(5)
    # self.DTMS_Save("testo")
    # time.sleep(3)


    # tool_value = tool_list[dr].get_attribute("aria-label")  # // 클릭 한 도구 attribute 값 추출
    # shortcut_key_info = tool_value.find("(")  # // 도구명 뒤에 있는 단축키 안내 부분 체크
    #
    # if shortcut_key_info != -1:
    #   tool_element = tool_value[0:(shortcut_key_info - 1)]
    #
    # else:
    #   tool_element = tool_value


    # self.list_shuffle(tool_list)

    # if len(tool_list) > page_add_number:

    # elif len(tool_list) < page_add_number:

    # elif len(tool_list) == page_add_number:

  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #
  # def page_add_save(self):
  #   pass
  # def file_open_save(self):
  #   pass