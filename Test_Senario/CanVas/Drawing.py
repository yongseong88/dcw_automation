import random
import time
from Pages.Base_Page import BasePage
from Pages.Canvas_Page import CanVasPage
from Utilities.Locators import canvas_LocatorFields


class Drawing_Senario(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.locate = canvas_LocatorFields
    self.canvas_page = CanVasPage(self.driver)

  def drawing_tool(self):
    # 닷 캔버스에서 제공 되는 도구 선택하는 시나리오
    tool_list = self.canvas_page.tool_list(self.locate.tool_list)
    print("도구의 총 갯수는 {}개 입니다.".format(len(tool_list)))

    drawing_info = []

    for dr in tool_list:
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

    return drawing_info

  def drawing_drag(self, x, y):
    # 캔버스 내 300셀에 drawing 하는 시나리오

    # 드로잉 시작점 설정
    # start_x = 560  # 캔버스 첫 칸의 x 좌표
    # end_x = 1390 # 캔버스 마지막 칸의 x 좌표

    # start_y = 408  # 캔버스 첫 칸의 y 좌표
    # end_y = 964 # 캔버스 마지막 칸의 y 좌표

    coordinate_arr = []

    for i in range(2):
      coordinate_arr.append([])
      for coo_xy in range(1):
        x_ran_num = random.randrange(x, (x+(14.06*59)) + 1)
        y_ran_num = random.randrange(x, (x+(14.26*39)) + 1)

        coordinate_arr[i].append(x_ran_num)
        coordinate_arr[i].append(y_ran_num)

    for cnt in range(len(coordinate_arr)):
      coo_x, coo_y = coordinate_arr[cnt]
      if cnt == 0:
        self.mouse_click(coo_x, coo_y)
      else:
        self.mouse_drag(coo_x, coo_y)
      print(coo_x, coo_y)
      time.sleep(2)






