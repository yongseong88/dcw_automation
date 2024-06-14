from Utilities.Locators import main_LocatorFields
from Pages.Base_Page import BasePage
import time
import random
from selenium.webdriver.common.by import By

class MainPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.locate = main_LocatorFields

  def canvas_btn_click(self):
    # 캔버스 진입 시나리오
    self.click(self.locate.canvas_btn) # GNB 내 캔버스 버튼 클릭
    time.sleep(5)

  def book_btn_click(self):
    # 캔버스 진입 시나리오
    self.click(self.locate.book_btn) # GNB 내 캔버스 버튼 클릭

  def cloud_btn_click(self):
    # 캔버스 진입 시나리오
    self.click(self.locate.cloud_btn) # GNB 내 캔버스 버튼 클릭

  def support_btn_click(self):
    # 캔버스 진입 시나리오
    self.click(self.locate.support_btn) # GNB 내 캔버스 버튼 클릭

  def login_btn_click(self):
    # 캔버스 진입 시나리오
    self.click(self.locate.login_btn) # GNB 내 캔버스 버튼 클릭
    time.sleep(2)
