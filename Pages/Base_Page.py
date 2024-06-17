import random
from selenium.common import StaleElementReferenceException
import pyautogui
from selenium.webdriver.chromium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

  def __init__(self, driver):
    self.driver = driver

  def get_element(self, locator):
      match locator:
          case (_, keyword) \
              if str(keyword).find('folder') != -1\
              or str(keyword).find('file') != -1\
              or str(keyword).find('tool') != -1:
              element = WebDriverWait(self.driver, 20).until(
                  EC.visibility_of_all_elements_located((locator))
              )

              return element

          case _:
              element = WebDriverWait(self.driver, 20).until(
                  EC.visibility_of_element_located((locator))
              )

              return element

  def click(self, locator):
      try:
          if type(self.get_element(locator)) is not list:
              element = WebDriverWait(self.driver, 20).until(
                  EC.visibility_of_element_located((locator))
              )
              element.click()
      except StaleElementReferenceException:
          if type(self.get_element(locator)) is not list:
              element = WebDriverWait(self.driver, 20).until(
                  EC.visibility_of_element_located((locator))
              )
              element.click()

  def get_text(self, locator):
      element = WebDriverWait(self.driver, 20).until(
          EC.visibility_of_element_located((locator))
      )
      msg = element.text
      return msg

  def set(self, locator, value):
      element = WebDriverWait(self.driver, 20).until(
          EC.visibility_of_element_located((locator))
      )

      element.send_keys(value)

  def get_title(self):
      return self.driver.title

  def mouse_click(self, x, y):
      self.driver.implicitly_wait(3)
      pyautogui.moveTo(x, y, duration=1)
      pyautogui.click(x, y, duration=1)

  def mouse_drag(self, x, y):
      self.driver.implicitly_wait(3)
      pyautogui.dragTo(x, y, duration=1, button='left')

  def key_input(self, value):
      match value:
          case "Control":
            webdriver.ActionChains(self.driver).key_down(keys.CONTROL).send_keys("a").perform()
          case "Shift":
            webdriver.ActionChains(self.driver).key_down(keys.SHIFT).send_keys("a").perform()


