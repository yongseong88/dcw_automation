import base64
from selenium.common import StaleElementReferenceException
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

  def __init__(self, driver):
    self.driver = driver

  def get_element(self, locator):

      element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator)))

      return element

  def get_elements(self, locator):
      element = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((locator)))

      return element

  def click(self, locator):
      try:
          element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator)))

          element.click()

      except StaleElementReferenceException:

          element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator)))

          element.click()

  def double_click(self, locator):
      actions = ActionChains(self.driver)

      actions.double_click(locator).perform()


  def get_text(self, locator):
      element = WebDriverWait(self.driver, 20).until(
          EC.visibility_of_element_located(
              (locator))
      )

      msg = element.text
      return msg

  def get_aria_label(self, locator):
      try:
          element = WebDriverWait(self.driver, 25).until(
              EC.visibility_of_element_located((locator))
              # EC.presence_of_element_located((locator))
          )

          label = element.get_attribute("aria-label")

          if label is None:
              print("aria-label 값이 None입니다. 요소가 올바르게 로드되었는지 확인해주세요.")
          return label

      except Exception as e:
            print(f"오류 발생: {e}")
            return None

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
      pyautogui.click(x, y, duration=2)

  def mouse_drag(self, x, y):
      self.driver.implicitly_wait(3)
      pyautogui.dragTo(x, y, duration=3, button='left')

  def key_input(self, value):
      pyautogui.press(value)

  def element_scroll(self, locator):
      actions = ActionChains(self.driver)

      actions.move_to_element(locator).perform()

  def page_refresh(self):
      self.driver.refresh()

  def screenshot_capture(self):
      page_rect = self.driver.execute_cdp_cmd('Page.getLayoutMetrics', {})

      screenshot_config = {'captureBeyondViewport': True,
                           'fromSurface': True,
                           'clip': {'width': page_rect['cssContentSize']['width'],
                                    'height': page_rect['cssContentSize']['height'],  # contentSize -> cssContentSize
                                    'x': 0,
                                    'y': 0,
                                    'scale': 1},
                           }
      # Dictionary with 1 key: data
      base_64_png = self.driver.execute_cdp_cmd('Page.captureScreenshot', screenshot_config)
      # driver.execute_script("document.body.style.zoom='80%'")

      # Write img to file
      with open("/Users/park-yongseong/Documents/DCW_Automation/Result_Report/chrome-devtools-protocol.png", "wb") as fh:
          fh.write(base64.urlsafe_b64decode(base_64_png['data']))

      # 자바스크립트를 실행하여 웹페이지의 총 높이를 가져오기.
      # total_height = self.driver.execute_script("return document.body.parentNode.scrollHeight")
      #
      # 브라우저 창을 페이지 하단으로 스크롤 하기.
      # self.driver.execute_script("window.scrollTo(0, document.body.parentNode.scrollHeight);")
      #
      # time.sleep(1)  # 1초 동안 대기.
      #
      # 창의 크기를 설정하여 전체 웹페이지를 캡처 (너비: 1920 픽셀, 높이: total_height 픽셀)
      # self.driver.set_window_size("1920", total_height)
      #
      # time.sleep(1)  # 1초 동안 대기.
      # self.driver.save_screenshot(output_path)  # 스크린샷을 지정된 출력 경로에 저장.


  def get_location(self, value, locator):
      if value == 'ID':
          self.driver.find_element(By.ID, locator).location
      elif value == 'CLASS_NAME':
          self.driver.find_element(By.CLASS_NAME, locator).location
      elif value == 'XPATH':
          self.driver.find_element(By.XPATH, locator).location
      elif value == 'CSS_SELECTOR':
        self.driver.find_element(By.CSS_SELECTOR, locator).location

  def scroll_location(self):
    # scroll_x = self.driver.execute_script("return window.scrollX;")
    scroll_y = self.driver.execute_script("return window.scrollY;")

    # print(f"Horizontal scroll position: {scroll_x}")
    print(f"Vertical scroll position: {scroll_y}")

    return scroll_y

