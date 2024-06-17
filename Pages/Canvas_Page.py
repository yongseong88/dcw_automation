import random
import time

from Pages.Base_Page import BasePage


class CanVasPage(BasePage):

  def __init__(self, driver):
    # super().__init__(driver)
    self.driver = driver

  def new_btn_click(self, locator):
    self.click(locator)

  def open_btn_click(self, locator):
    self.click(locator)

  def add_btn_click(self, locator):
    self.click(locator)

  def file_list(self, locator):
    file_lst = self.get_element(locator)
    return file_lst

  def folder_list(self, locator):
    folder_lst = self.get_element(locator)
    return folder_lst

  def confirm_btn_click(self, locator):
    self.click(locator)

  def cancel_btn_click(self, locator):
    self.click(locator)

  def export_btn_click(self, locator):
    self.click(locator)

  def save_btn_click(self, locator):
    self.click(locator)

  def saveAs_btn_click(self, locator):
    self.click(locator)

  def pt_btn_click(self, locator):
    self.click(locator)

  def undo_btn_click(self, locator):
    self.click(locator)

  def redo_btn_click(self, locator):
    self.click(locator)

  def tool_list(self, locator):
    tool_lst = self.get_element(locator)
    return tool_lst

  def drawing_click(self, x, y):
    self.mouse_click(x, y)

  def drawing_drag(self, x, y):
    # 캔버스 내 300셀에 drawing 하는 시나리오

    xran_step = random.randrange(1, 60)
    yran_step = random.randrange(1, 40)
    coordinate_arr = []

    for i in range(2):
      coordinate_arr.append([])
      for coo_xy in range(1):

        x_ran_num = random.randrange(x, int((x+(14.06*xran_step))) + 1, 15)
        y_ran_num = random.randrange(y, int((y+(14.26*yran_step))) + 1, 15)

        coordinate_arr[i].append(x_ran_num)
        coordinate_arr[i].append(y_ran_num)

    for cnt in range(len(coordinate_arr)):
      coo_x, coo_y = coordinate_arr[cnt]
      if cnt == 0:
        self.mouse_click(coo_x, coo_y)
        time.sleep(2)
      else:
        self.mouse_drag(coo_x, coo_y)
      print(coo_x, coo_y)
      time.sleep(2)

  def pen_size_list(self, locator):
    pen_size_lst = self.get_element(locator)
    return pen_size_lst

  def grid_btn_click(self, locator):
    self.click(locator)

  def page_add_btn_click(self, locator):
    self.click(locator)

  def page_description(self, locator, text):
    self.set(locator, text)

  # def root_file_open(self):
  #   # ROOT 경로 내 있는 파일 열기
  #   self.click(self.locate.open_btn)  # 열기 버튼 클릭
  #
  #   file_list = self.get_element(self.locate.file_list)  # ROOT 경로 내 파일 리스트 추출
  #   self.list_shuffle(file_list)  # 추출 한 파일 리스트 무작위 섞기
  #   ran_num = self.random_number(file_list)  # // ROOT 경로의 파일 총 갯수 중 임의 숫자 설정
  #
  #   print("\r\n" + f'{"출력 결과":=^78}')
  #   print("파일의 총 갯수는 {}개 입니다.".format(len(file_list)))
  #
  #   # // 파일 갯수 체크 하는 로직
  #   if len(file_list) > 1:  # ROOT 경로 내 파일 갯수가 1개 초과 일 경우
  #     file_list[ran_num].click()  # 폴더 내 임의의 파일 클릭
  #     file_name = file_list[ran_num].text
  #     print("클릭한 파일명 : {}".format(file_name))
  #
  #   else:  # ROOT 경로 내 파일 갯수가 1개 또는 1개 미만일 경우
  #     file_list[0].click()  # 폴더 내 첫번째 파일 클릭
  #     file_name = file_list[0].text
  #     print("클릭한 파일명 : {}".format(file_name))
  #
  #   self.click(self.locate.confirm_btn)  # // 팝업 내 열기 버튼 클릭
  #   time.sleep(3)
  #
  # def folder_file_open(self):
  #   # 파일 있는 폴더 진입 후 파일 열기
  #   self.click(self.locate.open_btn) # // 열기 버튼 클릭
  #
  #   folder_list = self.get_element(self.locate.folder_list) # // 폴더 리스트 추출
  #
  #   print("\r\n" + f'{"출력 결과":=^78}')
  #   print("폴더의 총 갯수는 {}개 입니다.".format(len(folder_list)))
  #
  #   random.shuffle(folder_list) # // 폴더 리스트 무작위 섞기
  #
  #   for fl in folder_list: # // 파일이 있는 폴더 클릭 후 파일 선택
  #     if fl.text.find("0 items") == -1: # 파일 갯수가 0개가 아니라면 해당 로직 진행
  #       fl.click() # 폴더 클릭
  #       folder_name = fl.find_element(By.CSS_SELECTOR, self.locate.folder_name).text # 클릭한 폴더명 추출
  #       folder_item = fl.find_element(By.CSS_SELECTOR, self.locate.folder_items).text # 클릭한 폴더 내 파일 갯수 추출
  #       print("호루다 네임: {}".format(folder_name))
  #       print("아이템 걋수: {}".format(folder_item))
  #
  #       file_list = self.get_element(self.locate.file_list) # 폴더 내 보유 한 파일 리스트 추출
  #
  #       random.shuffle(file_list) # 폴더 내 보유 한 파일 리스트 무작위 섞기
  #       ran_num = random.randrange(0, len(file_list))  # // 폴더 내 파일의 총 갯수 중 임의 숫자 설정
  #
  #       match len(file_list):
  #         case 0:
  #           print("파일이 없습니다.")
  #         case 1:
  #           file_list[0].click()  # 폴더 내 임의의 파일 클릭
  #           file_name = file_list[0].text
  #           print("클릭한 파일명 : {}".format(file_name))
  #         case _:
  #           file_list[ran_num].click()  # 폴더 내 임의의 파일 클릭
  #           file_name = file_list[ran_num].text
  #           print("클릭한 파일명 : {}".format(file_name))
  #       break
  #
  #     else:
  #       pass
  #
  #   self.click(self.locate.confirm_btn) # // 팝업 내 열기 버튼 클릭
  #   time.sleep(3)
  #
  #
  # def tool_btn(self):
  #   tool_list = self.get_element(self.locate.tool_list)  # 닷 캔버스 내 사용 가능한 도구 리스트 추출
  #   return tool_list

  # def drawing_tool_btn(self):
  #   # 닷 캔버스에서 제공 되는 도구 선택하는 시나리오
  #
  #   tool_list = self.get_element(self.locate.tool_list) # 닷 캔버스 내 사용 가능한 도구 리스트 추출
  #   print("도구의 총 갯수는 {}개 입니다.".format(len(tool_list)))
  #
  #   drawing_info = []
  #
  #   for dr in tool_list:
  #     # tool_value = tool_list[dr].get_attribute("aria-label")
  #     tool_value = dr.get_attribute("aria-label")
  #     shortcut_key_info = tool_value.find("(")  # // 도구명 뒤에 있는 단축키 안내 부분 체크
  #
  #     if shortcut_key_info != -1:
  #       tool_element = tool_value[0:(shortcut_key_info - 1)]
  #
  #     else:
  #       tool_element = tool_value
  #
  #     match tool_element:
  #       case '펜':
  #         drawing_info.append(dr)
  #       case '수직 미러 펜':
  #         drawing_info.append(dr)
  #       case '채우기':
  #         drawing_info.append(dr)
  #       case '선':
  #         drawing_info.append(dr)
  #       case '사각형':
  #         drawing_info.append(dr)
  #       case '원':
  #         drawing_info.append(dr)
  #       case '삼각형':
  #         drawing_info.append(dr)
  #       case _:
  #         pass
  #
  #   return drawing_info


    # for dl in drawing_info:
    #
    #   try:
    #     dl.click()
    #     dl.get_attribute()
    #
    #   except ElementClickInterceptedException:
    #     print("Element click was intercepted.")
    #
    #   print("클릭한 도구: ", dl.text)


      # tool_value = tool_list[dl].get_attribute("aria-label")
      # shortcut_key_info = tool_value.find("(")  # // 도구명 뒤에 있는 단축키 안내 부분 체크
      #
      # if shortcut_key_info != -1:
      #   tool_element = tool_value[0:(shortcut_key_info - 1)]
      #
      # else:
      #   tool_element = tool_value
      #
      # # print("드로잉 배열: ", dl)
      # # print("dl: ", len(drawing_info))
      # tool_list[dl].click()
      # tooltip = tool_list[dl].text  # // 클릭 한 도구 툴팁 추출
      # print("클릭한 도구: {}".format(tool_element))
      # print("도구 툴팁: {}".format(tooltip))

    # tool_list[0].click()  # // 전체 도구 중 임의의 도구 클릭
    # tooltip = tool_list[ran_num].text  # // 클릭 한 도구 툴팁 추출
    # print(
    #   "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
    # print("도구 툴팁: {}".format(tooltip))


  # case
  # '수직 미러 펜':
  # tool_list[ran_num].click()  # // 전체 도구 중 임의의 도구 클릭
  # tooltip = tool_list[ran_num].text  # // 클릭 한 도구 툴팁 추출
  # print(
  #   "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  # print("도구 툴팁: {}".format(tooltip))
  #
  # case
  # '채우기':
  # tool_list[ran_num].click()  # // 전체 도구 중 임의의 도구 클릭
  # tooltip = tool_list[ran_num].text  # // 클릭 한 도구 툴팁 추출
  # print(
  #   "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  # print("도구 툴팁: {}".format(tooltip))
  #
  # case
  # '선':
  # tool_list[ran_num].click()  # // 전체 도구 중 임의의 도구 클릭
  # tooltip = tool_list[ran_num].text  # // 클릭 한 도구 툴팁 추출
  # print(
  #   "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  # print("도구 툴팁: {}".format(tooltip))
  #
  # case
  # '사각형':
  # tool_list[ran_num].click()  # // 전체 도구 중 임의의 도구 클릭
  # tooltip = tool_list[ran_num].text  # // 클릭 한 도구 툴팁 추출
  # print(
  #   "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  # print("도구 툴팁: {}".format(tooltip))
  #
  # case
  # '원':
  # tool_list[ran_num].click()  # // 전체 도구 중 임의의 도구 클릭
  # tooltip = tool_list[ran_num].text  # // 클릭 한 도구 툴팁 추출
  # print(
  #   "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  # print("도구 툴팁: {}".format(tooltip))
  #
  # case
  # '삼각형':
  # tool_list[ran_num].click()  # // 전체 도구 중 임의의 도구 클릭
  # tooltip = tool_list[ran_num].text  # // 클릭 한 도구 툴팁 추출
  # print(
  #   "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  # print("도구 툴팁: {}".format(tooltip))
  #
  # case
  # _:
  # # tool_list[ran_num].click()
  # # tooltip = dr.text
  # print("선택된 도구: {}".format(tool_value))
  # pass
  #
  # time.sleep(3)

  # def drawing_drag(self):
  #   # 캔버스 내 300셀에 drawing 하는 시나리오
  #
  #   # 드로잉 시작점 설정
  #   start_x = 560  # 캔버스 첫 칸의 x 좌표
  #   end_x = 1390 # 캔버스 마지막 칸의 x 좌표
  #
  #   start_y = 408  # 캔버스 첫 칸의 y 좌표
  #   end_y = 964 # 캔버스 마지막 칸의 y 좌표
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
  #     time.sleep(2)
  #
  #
  # def page_add(self):
  #   self.click(self.locate.canvas_add_btn)
  #
  # def canvas_drawing_save(self):
  #   tool_btn = self.drawing_tool_btn()
  #   # print("\r\n그리기 도구의 총 갯수는 {}개 입니다.".format(len(tool_btn)))
  #
  #   # 페이지 추가 시나리오
  #   page_max = 100  # 페이지 최대 수 설정
  #   page_add_number = random.randrange(1, page_max + 1)  # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)
  #   page_info = []  # 추가한 페이지에 대한 정보를 담는 배열 선언
  #
  #   for pl in range(page_add_number):
  #     random.shuffle(tool_btn)
  #
  #     for tb in tool_btn:
  #       tool_value = tb.get_attribute("aria-label")
  #       shortcut_key_info = tool_value.find("(")  # // 도구명 뒤에 있는 단축키 안내 부분 체크
  #       if shortcut_key_info != -1:
  #         tool_element = tool_value[0:(shortcut_key_info - 1)]
  #
  #       else:
  #         tool_element = tool_value
  #
  #       match tool_element:
  #         case '펜':
  #           tb.click()  # // 전체 도구 중 임의의 도구 클릭
  #           tooltip = tb.text  # // 클릭 한 도구 툴팁 추출
  #           print(
  #             "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  #           print("도구 툴팁: {}".format(tooltip))
  #           self.drawing_drag()
  #           self.page_add()
  #           page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
  #           print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
  #           break
  #
  #         case '수직 미러 펜':
  #           tb.click()  # // 전체 도구 중 임의의 도구 클릭
  #           tooltip = tb.text  # // 클릭 한 도구 툴팁  추출
  #           print(
  #             "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  #           print("도구 툴팁: {}".format(tooltip))
  #           self.drawing_drag()
  #           self.page_add()
  #           page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
  #           print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
  #           break
  #
  #         case '채우기':
  #           tb.click()  # // 전체 도구 중 임의의 도구 클릭
  #           tooltip = tb.text  # // 클릭 한 도구 툴팁  추출
  #           print(
  #             "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  #           print("도구 툴팁: {}".format(tooltip))
  #           self.drawing_drag()  # 해당 위치 까지 drag
  #           self.page_add()
  #           page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
  #           print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
  #           break
  #
  #         case '선':
  #           tb.click()  # // 전체 도구 중 임의의 도구 클릭
  #           tooltip = tb.text  # // 클릭 한 도구 툴팁  추출
  #           print(
  #             "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  #           print("도구 툴팁: {}".format(tooltip))
  #           self.drawing_drag()
  #           self.page_add()
  #           page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
  #           print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
  #           break
  #
  #         case '사각형':
  #           tb.click()  # // 전체 도구 중 임의의 도구 클릭
  #           tooltip = tb.text  # // 클릭 한 도구 툴팁  추출
  #           print(
  #             "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  #           print("도구 툴팁: {}".format(tooltip))
  #           self.drawing_drag()
  #           self.page_add()
  #           page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
  #           print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
  #           break
  #
  #         case '원':
  #           tb.click()  # // 전체 도구 중 임의의 도구 클릭
  #           tooltip = tb.text  # // 클릭 한 도구 툴팁  추출
  #           print(
  #             "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  #           print("도구 툴팁: {}".format(tooltip))
  #           self.drawing_drag()
  #           self.page_add()
  #           page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
  #           print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
  #           break
  #
  #         case '삼각형':
  #           tb.click()  # // 전체 도구 중 임의의 도구 클릭
  #           tooltip = tb.text  # // 클릭 한 도구 툴팁  추출
  #           print(
  #             "클릭한 도구: {}".format(tool_element))  # // 도구명 뒤에 단축키 안내 '(' 가 있으면 도구명 부터 '(' 앞까지만 노출 되도록 설정
  #           print("도구 툴팁: {}".format(tooltip))
  #           self.drawing_drag()
  #           self.page_add()
  #           page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
  #           print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
  #           break
  #
  #         case _:
  #           # tooltip = dr.text
  #           print("선택된 도구가 없어요!")
  #           pass
  #           # self.page_add()
  #           # page_info.append(pl)  # 배열에 추가한 페이지 수 카운트 추가
  #           # print("추가된 페이지 정보: {} / {}".format(pl + 1, page_add_number + 1))
  #           break
  #
  #   print("추가된 페이지 수는 {0} 입니다".format(page_add_number+1))
  #   time.sleep(5)

  #       Canvas_Tool.tool_btn_click(dr)
  #       self.page_add()
  #       page_info.append(pl)
  #       break
  #
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
  #
  # print("추가된 페이지 수는 {0} 입니다".format(page_add_number+1))
  # time.sleep(5)
  # self.DTMS_Save("testo")
  # time.sleep(3)





  #   # pyautogui.mouseInfo()
  #   time.sleep(5)  # // 3초 대기
  #
  #
  # def drawing_drag(self):
  #   # 캔버스 내 300셀에 drawing 하는 시나리오
  #
  #   # 드로잉 시작점 설정
  #   start_x = 560  # 캔버스 첫 칸의 x 좌표
  #   end_x = 1390 # 캔버스 마지막 칸의 x 좌표
  #
  #   start_y = 408  # 캔버스 첫 칸의 y 좌표
  #   end_y = 964 # 캔버스 마지막 칸의 y 좌표
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



  #   # 캔버스 내 페이지 추가 시나리오
  #   page_list = self.get_element(self.page_list)  # 페이지 갯수 추출
  #   page_max = 100 # 페이지 최대 수
  #   page_add_number = random.randrange(1,page_max+1) # 추가 할 페이지 수 랜덤으로 설정 (1 ~ 100)
  #   page_info = [] # 추가한 페이지에 대한 정보를 담는 배열 선언
  #
  #   print("추가 할 페이지 수: {}".format(page_add_number))
  #
  #   for pg in range(page_add_number):
  #     self.click(self.canvas_add_button)
  #     page_info.append(pg) # 배열에 추가한 페이지 수 카운트 추가
  #     print("추가된 페이지 정보: {} / {}".format(pg+1, page_add_number))
  #
  #   print("추가된 페이지 수는 {} 입니다".format(len(page_info)))
  #
  # def description_btn_click(self, description):
  #   # 캔버스 내 페이지 설명 작성 시나리오
  #   self.set(self.canvas_description_button, description) # // 페이지 설명 선택 후 텍스트 작성
  #
  # def DTMS_Save(self, file_name):
  #   # 파일 최초 저장 및 재 저장 하는 시나리오
  #   self.click(self.save_btn) # 저장 버튼 클릭
  #   self.set(self.save_textfield, file_name) # // 팝업 내 텍스트 박스 선택 후 저장 할 파일명 입력
  #   self.click(self.save_confirm_btn) # // 팝업 내 저장 버튼 클릭
  #   time.sleep(3)
  #
  # def DTMS_SaveAs(self, file_name):
  #   # 파일 다른 이름 저장 하는 시나리오
  #   self.click(self.saveAs_btn) # // 다른 이름 저장 버튼 클릭
  #   self.set(self.save_textfield, file_name) # // 팝업 내 텍스트 박스 선택 후 저장 할 파일명 입력
  #   self.click(self.save_confirm_btn) # // 팝업 내 저장 버튼 클릭
  #   time.sleep(3)
  #
  # # def folder_open(self):
  # #   self.click(self.open_button) # // 열기 버튼 클릭
  # #   folder_list = self.get_element(self.folder_list) # // 열기 버튼 클릭
  # #
  # #   print("\r\n" + f'{"출력 결과":=^78}')
  # #   print("폴더의 총 갯수는 {}개 입니다.".format(len(folder_list)))
  # #
  # #   # 폴더 리스트 무작위로 섞기
  # #   self.list_shuffle(folder_list)
  # #
  # #   for fl in folder_list:
  # #     if fl.text.find("0 items") == -1:
  # #       fl.click()
  # #       folder_name = fl.find_element(By.CSS_SELECTOR, self.folder_name).text
  # #       folder_item = fl.find_element(By.CSS_SELECTOR, self.folder_items).text
  # #       print("호루다 네임: {}".format(folder_name))
  # #       print("아이템 걋수: {}".format(folder_item))
  # #       break
  # #
  # #     else:
  # #       pass
  #
  #
  #
  # def root_file_add(self):
  #   # ROOT 경로 내 있는 파일 추가
  #
  #   self.click(self.file_add_button) # 추가하기 버튼 클릭
  #   self.click(self.file_add_dotcloud)  # 닷 클라우드 버튼 클릭
  #
  #   file_list = self.get_element(self.file_list)  # ROOT 경로 내 파일 리스트 추출
  #
  #   print("\r\n" + f'{"출력 결과":=^78}')
  #   print("파일의 총 갯수는 {}개 입니다.".format(len(file_list)))
  #
  #   # random.shuffle(file_list)
  #   # self.list_shuffle(file_list)  # 추출 한 파일 리스트 무작위 섞기
  #   ran_num = self.random_number(file_list)  # // ROOT 경로의 파일 총 갯수 중 임의 숫자 설정
  #   # ran_num = random.randrange(0, len(file_list))
  #
  #   # // 파일 갯수 체크 하는 로직
  #   if len(file_list) > 1:  # ROOT 경로 내 파일 갯수가 1개 초과 일 경우
  #     self.list_shuffle(file_list)
  #     file_list[ran_num].click()  # 폴더 내 임의의 파일 클릭
  #     file_name = file_list[ran_num].text
  #     print("클릭한 파일명 : {}".format(file_name))
  #
  #   else:  # ROOT 경로 내 파일 갯수가 1개 또는 1개 미만일 경우
  #     file_list[0].click()  # 폴더 내 첫번째 파일 클릭
  #     file_name = file_list[0].text
  #     print("클릭한 파일명 : {}".format(file_name))
  #
  #   self.click(self.file_add_confirm)  # // 팝업 내 가져오기 버튼 클릭
  #   self.Export()
  # 
  #   time.sleep(3)


  # def folder_file_add(self):
  #   # 파일 있는 폴더 진입 후 파일 추가
  #   self.click(self.file_add_button)  # 추가하기 버튼 클릭
  #   self.click(self.file_add_dotcloud)  # 닷 클라우드 버튼 클릭
  #
  #   folder_list = self.get_element(self.folder_list) # // 폴더 리스트 추출
  #
  #   print("\r\n" + f'{"출력 결과":=^78}')
  #   print("폴더의 총 갯수는 {}개 입니다.".format(len(folder_list)))
  #
  #   random.shuffle(folder_list) # // 폴더 리스트 무작위 섞기
  #
  #   for fl in folder_list: # // 파일이 있는 폴더 클릭 후 파일 선택
  #     if fl.text.find("0 items") == -1: # 파일 갯수가 0개가 아니라면 해당 로직 진행
  #       fl.click() # 폴더 클릭
  #       folder_name = fl.find_element(By.CSS_SELECTOR, self.folder_name).text # 클릭한 폴더명 추출
  #       folder_item = fl.find_element(By.CSS_SELECTOR, self.folder_items).text # 클릭한 폴더 내 파일 갯수 추출
  #       print("호루다 네임: {}".format(folder_name))
  #       print("아이템 걋수: {}".format(folder_item))
  #
  #       file_list = self.get_element(self.file_list) # 폴더 내 보유 한 파일 리스트 추출
  #
  #       random.shuffle(file_list) # 폴더 내 보유 한 파일 리스트 무작위 섞기
  #       ran_num = random.randrange(0, len(file_list))  # // 폴더 내 파일의 총 갯수 중 임의 숫자 설정
  #
  #       match len(file_list):
  #         case 0:
  #           print("파일이 없습니다.")
  #         case 1:
  #           file_list[0].click()  # 폴더 내 임의의 파일 클릭
  #           file_name = file_list[0].text
  #           print("클릭한 파일명 : {}".format(file_name))
  #         case _:
  #           file_list[ran_num].click()  # 폴더 내 임의의 파일 클릭
  #           file_name = file_list[ran_num].text
  #           print("클릭한 파일명 : {}".format(file_name))
  #
  #       break
  #
  #     else:
  #       pass
  #
  #   self.click(self.file_add_confirm)  # // 팝업 내 가져오기 버튼 클릭
  #   self.Export()
  #
  #   time.sleep(3)
  #
  # def Export(self):
  #   # DTMS 파일 내보내기
  #   self.click(self.file_export_button)  # 추가하기 버튼 클릭
  #   time.sleep(2)
  #
  # def add_dotpad(self):
  #   # DotPad 연결 시나리오
  #   # #list_x, list_y = 182, 182
  #   # Pairing_x, Pairing_y = 511, 513
  #   # add_dotpad = 2
  #
  #   self.click(self.Dotpad_button)
  #   print("여긴 어디? ", self.get_text(self.Dotpad_list))
  #   # print("tidre: ", self.get_tidre())
  #   # print(dotpad_len.text)
  #   time.sleep(3)
  #   # self.click(self.BLEsearch_button)
  #   # self.mouse_click(list_x, list_y)
  #   # self.mouse_click(Pairing_x, Pairing_y)
  #
  #
  #   # while add_dotpad < 2:
  #   #   if ad == 0:
  #   #     self.click(self.Dotpad_button)
  #   #     self.click(self.BLEsearch_button)
  #   #     self.mouse_click(list_x, list_y)
  #   #     self.mouse_click(Pairing_x, Pairing_y)
  #   #
  #   #   else:
  #   #     self.click(self.Dotpad_button)
  #   #     self.click(self.BLEsearch_button)
  #   #     self.mouse_click(list_x, list_y+40)
  #   #     self.mouse_click(Pairing_x, Pairing_y)
  #
  #   # pyautogui.moveTo(180, 182, duration=0.5)
  #   # pyautogui.mouseInfo()



