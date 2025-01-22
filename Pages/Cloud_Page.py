import time
from Pages.Base_Page import BasePage
from Utilities.Locators import cloud_LocatorFields
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class CloudPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locate = cloud_LocatorFields

    def file_info(self):
        cloud_all_list = self.get_element(self.locate.cloud_file_list)

        print("\r\n" + f'{"출력 결과":=^78}')
        print("파일의 총 갯수는 {}개 입니다.".format(len(cloud_all_list)))

        random.shuffle(cloud_all_list)

        for cl in cloud_all_list:
            if cl.get_attribute('aria-label').find("FILE") != -1:
                self.double_click(cl)
                # print(f"\r\n 클라우드 파일 리스트: {cl.text}")
                # print(f"\r\n 클라우드 파일 레이블: {cl.get_attribute('aria-label')}")

                double_click_file_name = cl.find_element(By.CSS_SELECTOR, self.locate.cloud_file_name).text
                double_click_file_date = cl.find_element(By.CSS_SELECTOR, self.locate.cloud_file_date).text
                print("더블 클릭 파일명: {}".format(double_click_file_name))
                print("더블 클릭 파일 생성일: {}".format(double_click_file_date))
                time.sleep(8)
                break