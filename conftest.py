import pytest
import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# webdriver-manager 패키지 섪치
# from webdriver_manager.chrome import ChromeDriverManager 라이브러리 호출
# from selenium.webdriver.chrome.service import Service 라이브러리 호출

@pytest.fixture()
def initialize_driver(request):

    # // driver 세션 연결
    chrome_options = webdriver.ChromeOptions() # 크롬 브라우저 적용 옵션
    # chrome_options.add_argument('--headless')  # headless옵션을 주고 시작하면, 웹브라우저를 열지않고 크롤링
    chrome_options.add_argument('--start-maximized') # 브라우저가 최대화된 상태로 실행됩니다.
    chrome_options.add_argument("lang=ko_KR")# 한국어로 실행
    chrome_options.add_argument("disable-gpu")  # 그래픽 가속 사용 안함
    # chrome_options.add_argument('window-size=1920x1080')
    # options.add_argument('--mute-audio')  # 브라우저에 음소거 옵션을 적용합니다.
    chrome_options.add_experimental_option("detach", True) # 창을 닫더라도 드라이버 유지

    service = Service() # Webdriver Manager 사용하여 크롬 드라이버 자동 설치하기

    driver = webdriver.Chrome(service= service, options=chrome_options)

    driver.get("https://dev-apps.dotincorp.com")

    request.cls.driver = driver

    yield

    driver.close()