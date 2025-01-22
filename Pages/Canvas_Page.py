from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import random
import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from Pages.Base_Page import BasePage
from Utilities.Locators import canvas_LocatorFields
from Utilities.json_util import Drive_api


class CanVasPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.locate = canvas_LocatorFields

  def save_filename(self):
    actual_filename = self.get_text(self.locate.filename_catch)
    return actual_filename

  #새로 만들기 버튼 클릭
  def new_btn_click(self):
    self.click(self.locate.New_btn)

  #열기 버튼 클릭
  def open_btn_click(self):
    self.click(self.locate.open_btn)

  # 추가하기 버튼 클릭
  def add_btn_click(self):
    self.click(self.locate.file_add_btn)
    self.click(self.locate.file_add_dotcloud)

  # 파일 브라우저 내 열기/추가 버튼 선택
  def filebrowser_confirm_btn_click(self):
    self.click(self.locate.confirm_btn)

  # 파일 브라우저 내 취소 버튼 선택
  def filebrowser_cancel_btn_click(self):
    self.click(self.locate.cancel_btn)

  # 파일 브라우저 내 열기/추가 파일 가져오기
    # file_type에 따라 ROOT 또는 폴더 내 파일 가져오기
  def file_open(self, file_type):

    file_name = None
    folder_name = None
    folder_in_file_name = None

    match file_type:
      case "file":
        file_list = self.get_elements(self.locate.file_list)
        random_file = random.choice(file_list)

        print("\r\n" + f'{"출력 결과":=^78}')
        print("파일의 총 갯수는 {}개 입니다.".format(len(file_list)))

        match len(file_list):
          case 0:
            print("파일이 없습니다.")
            pass

          case 1:
            file_list[0].click()  # 폴더 내 임의의 파일 클릭
            file_name = file_list[0].text
            print("클릭한 파일명 : {}".format(file_name))

          case _:
            random_file.click()  # 폴더 내 임의의 파일 클릭
            file_name = random_file.text
            print("클릭한 파일명 : {}".format(file_name))

        time.sleep(5)
        self.filebrowser_confirm_btn_click()
        return file_name

      case "folder":
        folder_list = self.get_elements(self.locate.folder_list)

        print("\r\n" + f'{"출력 결과":=^78}')
        print("폴더의 총 갯수는 {}개 입니다.".format(len(folder_list)))

        # random_folder = random.choice(folder_list)
        random.shuffle(folder_list)  # // 폴더 리스트 무작위 섞기

        try:
          for fl in folder_list:  # // 파일이 있는 폴더 클릭 후 파일 선택
            if fl.text.find("0 items") == -1:  # 파일 갯수가 0개가 아니라면 해당 로직 진행
              random.shuffle(folder_list)
              # random_folder = random.choice(folder_list)
              # random_folder.click()  # 폴더 클릭
              fl.click()
              folder_name = fl.find_element(By.CSS_SELECTOR, self.locate.click_folder_name).text  # 클릭한 폴더명 추출
              folder_item = fl.find_element(By.CSS_SELECTOR, self.locate.click_folder_items).text  # 클릭한 폴더 내 파일 갯수 추출
              print("폴더 네임: {}".format(folder_name))
              print("아이템 갯수: {}".format(folder_item))
              time.sleep(7)

              folder_in_file_list = self.get_elements(self.locate.file_list)  # 폴더 내 보유 한 파일 리스트 추출

              random_foder_in_file = random.choice(folder_in_file_list)
              # random.shuffle(folder_in_file_list)  # 폴더 내 보유 한 파일 리스트 무작위 섞기
              # ran_num = random.randrange(0, len(folder_in_file_list))  # // 폴더 내 파일의 총 갯수 중 임의 숫자 설정

              match len(folder_in_file_list):
                case 0:
                  print("파일이 없습니다.")
                case 1:
                  folder_in_file_list[0].click()  # 폴더 내 임의의 파일 클릭
                  folder_in_file_name = folder_in_file_list[0].text
                  print("클릭한 파일명 : {}".format(folder_in_file_name))
                case _:
                  random_foder_in_file.click()  # 폴더 내 임의의 파일 클릭
                  folder_in_file_name = random_foder_in_file.text
                  print("클릭한 파일명 : {}".format(folder_in_file_name))
              break

            else:
              print("클릭 할 폴더가 없습니다.")

        except StaleElementReferenceException:
          pass

        time.sleep(5)
        self.filebrowser_confirm_btn_click()
        return folder_name, folder_in_file_name

      case _:
        print("실행 불가능 합니다")
        pass

  def folder_open(self):

    folder_name = None

    try:
      folder_list = self.get_elements(self.locate.folder_list)

      print("\r\n" + f'{"출력 결과":=^78}')
      print("폴더의 총 갯수는 {}개 입니다.".format(len(folder_list)))

      random_folder = random.choice(folder_list)
      # random.shuffle(folder_list)  # // 폴더 리스트 무작위 섞기

      match len(folder_list):
        case 0:
          print("클릭 할 폴더가 없습니다.")
          pass

        case 1:
          folder_list[0].click()  # 폴더 내 임의의 파일 클릭
          # folder_name = folder_list[0].text
          folder_name = folder_list[0].find_element(By.CSS_SELECTOR, self.locate.click_folder_name).text  # 클릭한 폴더명 추출
          # folder_item = folder_list[0].find_element(By.CSS_SELECTOR, self.locate.click_folder_items).text  # 클릭한 폴더 내 파일 갯수 추출
          print("클릭한 폴더명 : {}".format(folder_name))

        case _:
          random_folder.click()  # 폴더 내 임의의 파일 클릭
          # folder_name = random_folder.text
          folder_name = random_folder.find_element(By.CSS_SELECTOR, self.locate.click_folder_name).text  # 클릭한 폴더명 추출
          print("클릭한 폴더명 : {}".format(folder_name))

      time.sleep(5)
      return folder_name

    except StaleElementReferenceException:
      pass


  # drawing 도구 리스트 추출
  def drawing_tool(self, x, y):
    # 닷 캔버스에서 제공 되는 도구 선택하는 시나리오
    tool_list = self.get_elements(self.locate.tool_list)

    drawing_info = []
    # drawing_tl = None  # 선택된 도구를 저장할 변수

    for tl in tool_list:
      tool_value = tl.get_attribute("aria-label")

      if tool_value.find("(") != -1:
        tool_element = tool_value[0:(tool_value.find("(") - 1)]
      else:
        tool_element = tool_value

      match tool_element:
        case '펜':
          drawing_info.append(tl)
        case '수직 미러 펜':
          drawing_info.append(tl)
        case '채우기':
          drawing_info.append(tl)
        case '선':
          drawing_info.append(tl)
        case '사각형':
          drawing_info.append(tl)
        case '원':
          drawing_info.append(tl)
        case '삼각형':
          drawing_info.append(tl)
        case _:
          pass

    random_tool = random.choice(drawing_info)

    tool_element = random_tool.get_attribute("aria-label")

    if "채우기" in tool_element:
      random_tool.click()
      tooltip = random_tool.text
      print("클릭한 도구: {}".format(tooltip[0:(tooltip.find("(") - 1)]))
      print("도구 툴팁: {}".format(tooltip))
      self.drawing_click(x, y)
      time.sleep(2)

    else:
      random_tool.click()
      tooltip = random_tool.text
      print("클릭한 도구: {}".format(tooltip[0:(tooltip.find("(") - 1)]))
      print("도구 툴팁: {}".format(tooltip))
      self.drawing_drag(x, y)
      time.sleep(2)


  # 300셀 클릭
  def drawing_click(self, x, y):
    self.mouse_click(x, y)

  # 300셀 드래그 동작
  def drawing_drag(self, x, y):
    # 캔버스 내 300셀에 drawing 하는 시나리오

    DTMS_X = random.randrange(1, 61)
    DTMS_Y = random.randrange(1, 41)
    coordinate_arr = []

    for i in range(2):
      coordinate_arr.append([])
      for coo_xy in range(1):
          x_ran_num = random.randrange(x, int((x + (13.78 * DTMS_X))) + 1, 15)
          y_ran_num = random.randrange(y, int((y + (13.75 * DTMS_Y))) + 1, 15)

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

  # undo 버튼 클릭
  def undo_btn_click(self):
    self.click(self.locate.undo_btn)

  # redo 버튼 클릭
  def redo_btn_click(self):
    self.click(self.locate.redo_btn)

  def description_input(self, description):
    # 캔버스 내 페이지 설명 작성 시나리오
    self.set(self.locate.canvas_description_btn, description)  # // 페이지 설명 선택 후 텍스트 작성

  def page_add_btn_click(self):
    self.click(self.locate.canvas_add_btn)

  def edit_save_cancel(self):
    self.click(self.locate.edit_save_cancel)

  def list_scroll(self):
    file_list = self.get_element(self.locate.file_list)
    random_file = random.choice(file_list)
    selected_index = file_list.index(random_file)

    print("\r\n" + f'{"출력 결과":=^78}')
    print("파일의 총 갯수는 {}개 입니다.".format(len(file_list)))

    for fl in range(len(file_list)):
      if selected_index >= 8:
        print(f"selected_index: {selected_index}")
        print(file_list[selected_index].text)
        self.element_scroll(file_list[selected_index])
        time.sleep(5)
        break
      else:
        random_file = random.choice(file_list)
        selected_index = file_list.index(random_file)

  def canvas_capture(self):
    scr_path = '/Users/park-yongseong/Documents/DCW_Automation/Result_Report/screen_shot.png'
    self.screenshot_capture(scr_path)

  def page_max_label(self):
    # return self.get_aria_label(self.locate.canvas_addfull_btn)
    return self.get_text(self.locate.canvas_page_100)

  # 내보내기 버튼 선택
  def export_btn_click(self):
    self.click(self.locate.file_export_btn)


  # 저장 버튼 선택
  def save_btn_click(self):
    self.click(self.locate.save_btn)

  # def save_set(self, save_path, save_filename):
  def save_set(self, save_filename):

    try:
        self.set(self.locate.save_textfield, save_filename)
        time.sleep(5)
        return save_filename

      # elif save_path == 'folder':
      #   folder_list = self.get_element(self.locate.folder_list)
      #   random.shuffle(folder_list)  # // 폴더 리스트 무작위 섞기
      #
      #   ran_num = random.randrange(0, len(folder_list))
      #
      #   print("\r\n" + f'{"출력 결과":=^78}')
      #   print("폴더의 총 갯수는 {}개 입니다.".format(len(folder_list)))
      #
      #   match len(folder_list):
      #     case 0:
      #       print("폴더가 없습니다.")
      #       pass
      #
      #     case 1:
      #       folder_list[0].click()  # 첫번째 폴더 클릭
      #       folder_name = folder_list[0].find_element(By.CSS_SELECTOR, self.locate.click_folder_name).text
      #       print("클릭한 폴더명 : {}".format(folder_name))
      #       time.sleep(5)
      #
      #     case _:
      #       folder_list[ran_num].click()  # 랜덤 한 폴더 클릭
      #       folder_name = folder_list[ran_num].find_element(By.CSS_SELECTOR, self.locate.click_folder_name).text
      #       print("클릭한 폴더명 : {}".format(folder_name))
      #       time.sleep(5)
      #
      #   self.set(self.locate.save_textfield, save_filename)
      #   time.sleep(1)
      #   self.save_confirm_btn_click()
      #   time.sleep(5)
      #   return folder_name, save_filename

    except StaleElementReferenceException:
      pass

  def save_confirm_btn_click(self):
    self.click(self.locate.save_confirm_btn)

  def save_cancel_btn_click(self):
    self.click(self.locate.save_btn)

  def dtms_info(self, file_path, dtms_file_name):

    time1 = None
    latest_item = None

    filelist_json = Drive_api.filebrowser_list_api('ROOT').json()

    for key in filelist_json:
      if type(filelist_json[key]) is list:
        for item in filelist_json[key]:
          if file_path == 'ROOT' and item['FILE_NAME'].find(dtms_file_name) != -1:
            time_str1 = item['MOD_DATE']
            time2 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")
            print(f"\r\n파일명: {item['FILE_NAME']}")

            if time1 is None or time1 < time2:
              time1 = time2
              latest_item = item
              print(f"time1: {time1} 이 최근입니다.")
              time_str = datetime.strftime(time1, "%Y-%m-%d %H:%M:%S.") + str(time1.microsecond)[:1]
              print(f"time_str: {time_str}")
              # print(f"파일명: {item['FILE_NAME']}")

            else:
              print("파일이 없습니다.")

          elif item['FILE_NAME'].find(file_path) != -1:
            time_str1 = item['REG_DATE']
            time2 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")

            if time1 is None or time1 < time2:
                time1 = time2
                print(f"time1: {time1} 이 최근입니다.")
                time_str = datetime.strftime(time1, "%Y-%m-%d %H:%M:%S.") + str(time1.microsecond)[:1]
                print(f"time_str: {time_str}")
                print(f"폴더명: {item['FILE_NAME']}")

            else:
                print("파일이 없습니다.")

            folder_json = Drive_api.filebrowser_list_api(item['FILE_KEY']).json()

            for key in folder_json:
                if type(folder_json[key]) is list:
                    for folder_in_item in folder_json[key]:
                        if folder_in_item['FILE_NAME'] in dtms_file_name:
                            print(f"폴더 filekey: {item['FILE_KEY']}")
                            time_str1 = folder_in_item['MOD_DATE']
                            time2 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")

                            if time1 is None or time1 < time2:
                                time1 = time2
                                latest_item = folder_in_item
                                print(f"time1: {time1} 이 최근입니다.")
                                time_str = datetime.strftime(time1, "%Y-%m-%d %H:%M:%S.") + str(time1.microsecond)[:1]
                                print(f"time_str: {time_str}")

                            else:
                                print("파일이 없습니다.")

                        else:
                            pass

    return latest_item['DTMS_JSON']

  def key_event(self, event):
    # self.click(self.locate.canvas_first_page)
    self.key_input(event)

  def page_length(self):
    page_label = self.get_aria_label(self.locate.canvas_pages)
    print(f"page_label: {page_label}")

  def saveAs_btn_click(self):
    self.click(self.locate.saveAs_btn)

  def pt_btn_click(self, locator):
    self.click(locator)

  def pen_size_list(self, locator):
    pen_size_lst = self.get_element(locator)
    return pen_size_lst

  def grid_btn_click(self, locator):
    self.click(locator)

  def page_description(self, locator, text):
    self.set(locator, text)


