import random
import time
from selenium.webdriver.common.by import By
from Pages.Base_Page import BasePage
from Pages.Canvas_Page import CanVasPage
from Utilities.Locators import canvas_LocatorFields
from Utilities.json_util import root_file_list_get


class Open_Senario(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.locate = canvas_LocatorFields
    self.canvas_page = CanVasPage(self.driver)


  def open_popup(self):
    self.canvas_page.open_btn_click(self.locate.open_btn)
    time.sleep(5)


  def root_file_open(self):
    # ROOT 경로 내 있는 파일 열기
    self.canvas_page.open_btn_click(self.locate.open_btn)
    file_list = self.canvas_page.file_list(self.locate.file_list)
    ran_num = random.randrange(0, len(file_list)+1)

    print("\r\n" + f'{"출력 결과":=^78}')
    print("파일의 총 갯수는 {}개 입니다.".format(len(file_list)))

    if len(file_list) > 1:  # ROOT 경로 내 파일 갯수가 1개 초과 일 경우
      file_list[ran_num].click()  # 파업 내 임의의 파일 클릭
      file_name = file_list[ran_num].text
      print("클릭한 파일명 : {}".format(file_name))

    else:  # ROOT 경로 내 파일 갯수가 1개 또는 1개 미만일 경우
      file_list[0].click()  # 폴더 내 임의의 파일 클릭
      file_name = file_list[0].text
      print("클릭한 파일명 : {}".format(file_name))

    self.canvas_page.confirm_btn_click(self.locate.confirm_btn)  # // 팝업 내 열기 버튼 클릭

    filelist_json = root_file_list_get('ROOT').json()
    for key in filelist_json:
      if type(filelist_json[key]) is list:
        for i in filelist_json[key]:
          if file_name == i['FILE_NAME']:
            # print("{} : {}".format(key, i['FILE_KEY']))
            return i['FILE_KEY']

    time.sleep(5)

  def folder_file_open(self):
    # 파일 있는 폴더 진입 후 파일 열기
    self.canvas_page.open_btn_click(self.locate.open_btn)
    folder_list = self.canvas_page.folder_list(self.locate.folder_list)

    print("\r\n" + f'{"출력 결과":=^78}')
    print("폴더의 총 갯수는 {}개 입니다.".format(len(folder_list)))

    random.shuffle(folder_list) # // 폴더 리스트 무작위 섞기

    for fl in folder_list: # // 파일이 있는 폴더 클릭 후 파일 선택
      if fl.text.find("0 items") == -1: # 파일 갯수가 0개가 아니라면 해당 로직 진행
        fl.click() # 폴더 클릭
        folder_name = fl.find_element(By.CSS_SELECTOR, self.locate.folder_name).text # 클릭한 폴더명 추출
        folder_item = fl.find_element(By.CSS_SELECTOR, self.locate.folder_items).text # 클릭한 폴더 내 파일 갯수 추출
        print("호루다 네임: {}".format(folder_name))
        print("아이템 걋수: {}".format(folder_item))

        file_list = self.canvas_page.file_list(self.locate.file_list) # 폴더 내 보유 한 파일 리스트 추출

        random.shuffle(file_list) # 폴더 내 보유 한 파일 리스트 무작위 섞기
        ran_num = random.randrange(0, len(file_list))  # // 폴더 내 파일의 총 갯수 중 임의 숫자 설정

        match len(file_list):
          case 0:
            print("파일이 없습니다.")
          case 1:
            file_list[0].click()  # 폴더 내 임의의 파일 클릭
            file_name = file_list[0].text
            print("클릭한 파일명 : {}".format(file_name))
          case _:
            file_list[ran_num].click()  # 폴더 내 임의의 파일 클릭
            file_name = file_list[ran_num].text
            print("클릭한 파일명 : {}".format(file_name))
        break

      else:
        pass

    self.canvas_page.confirm_btn_click(self.locate.confirm_btn)  # // 팝업 내 열기 버튼 클릭
    time.sleep(5)

    folderlist_json = root_file_list_get('ROOT').json()
    for key in folderlist_json:
      if type(folderlist_json[key]) is list:
        for i in folderlist_json[key]:
          if folder_name == i['FILE_NAME']:
            # print("{} : {}".format(key, i['FILE_KEY']))
            filelist_json = root_file_list_get(i['FILE_KEY']).json()

    for key in filelist_json:
      if type(filelist_json[key]) is list:
        for i in filelist_json[key]:
          if file_name == i['FILE_NAME']:
            # print("{} : {}".format(key, i['FILE_KEY']))
            return i['FILE_KEY']

  def file_open_cancel(self):
    self.canvas_page.open_btn_click(self.locate.open_btn)
    self.canvas_page.cancel_btn_click(self.locate.cancel_btn)
    time.sleep(5)