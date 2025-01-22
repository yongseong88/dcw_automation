from Utilities.testresult_json import parse_pytest_json_results, write_to_google_sheet
import pytest
from selenium import webdriver
import datetime
import os


# from seleniumwire import webdriver

# webdriver-manager 패키지 섪치
# from webdriver_manager.chrome import ChromeDriverManager 라이브러리 호출
# from selenium.webdriver.chrome.service import Service 라이브러리 호출

def pytest_addoption(parser):
    parser.addoption(
        "--env",  # 명령줄 옵션 이름
        action="store",  # 옵션 값 저장
        default=None,  # 기본값
        help="Set the environment: dev or prod"  # 옵션 설명
    )

@pytest.fixture
def base_url(pytestconfig):
    # CLI 옵션 > 환경변수 > 기본값 순서로 환경 설정
    env = pytestconfig.getoption("env") or os.getenv("TEST_ENV", "dev")
    if env == "dev":
        return "https://dev-apps.dotincorp.com"
    elif env == "prod":
        return "https://apps-dotincorp.com"
    else:
        raise ValueError(f"Unknown environment: {env}")

@pytest.fixture()
def initialize_driver(request, base_url):

    # // driver 세션 연결
    chrome_options = webdriver.ChromeOptions() # 크롬 브라우저 적용 옵션

    # 브라우즈 설정
    chrome_options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행됩니다.
    chrome_options.add_argument("lang=ko_KR")  # 한국어로 실행
    chrome_options.add_argument("disable-gpu")  # 그래픽 가속 사용 안함
    chrome_options.add_experimental_option("detach", True)  # 창을 닫더라도 드라이버 유지
    # chrome_options.add_argument('--headless')  # headless옵션을 주고 시작하면, 웹브라우저를 열지않고 크롤링
    # chrome_options.add_argument('window-size=1920x1080')
    # options.add_argument('--mute-audio')  # 브라우저에 음소거 옵션을 적용합니다.
    # chrome_options.add_argument("--enable-logging")
    # chrome_options.add_argument("--v=1")
    # chrome_options.add_argument('--proxy-server={0}'.format(proxy_address))
    # chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"}) # 브라우저 로그 설정

    # service = Service() # Webdriver Manager 사용하여 크롬 드라이버 자동 설치하기
    # driver = webdriver.Chrome(service= service, options=chrome_options)

    driver = webdriver.Chrome(options=chrome_options)

    # driver.get("https://dev-apps.dotincorp.com")
    driver.get(base_url)

    # 테스트 클래스에 드라이버 설정
    request.cls.driver = driver

    # 테스트 종료 후 드라이버와 서버 정리
    yield driver

    # # 브라우저 콘솔 로그 가져오기
    # logs = driver.get_log('browser')
    # print("\n--- Console Logs ---")
    # if logs is not None:
    #     for entry in logs:
    #         print(f"Level: {entry['level']}, Message: {entry['message']}")
    # else:
    #     print("No console logs found.")

    driver.close()


# pytest hook to upload results after the session finishes
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    json_report = '/Users/park-yongseong/Documents/DCW_Automation/Result_Report/report.json'  # Pytest 결과 JSON 파일 경로

    today = datetime.datetime.now().strftime('%Y_%m')

    test_result_sheet = today + '_DCW_Automation_Results'

    # Pytest 종료 후 결과 파싱 및 Google 스프레드시트에 업로드
    df = parse_pytest_json_results(json_report)
    write_to_google_sheet(df, test_result_sheet)