from selenium.webdriver.common.by import By


class main_LocatorFields:  #메인 페이지 내 요소

    # GNB 버튼
    canvas_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > nav > ul > li:nth-child(2) > a")
    book_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > nav > ul > li:nth-child(3) > a")
    cloud_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > nav > ul > li:nth-child(4) > a")
    support_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > nav > ul > li:nth-child(5) > a")
    language_dropdown_btn = (By.CSS_SELECTOR,  "#languageDropdown")
    language_dropdown_btn = (By.CSS_SELECTOR, "#brailleLanguageDropdown")
    login_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > div > button")


    # 중간 카드 버튼
    canvas_cont_btn = (By.CSS_SELECTOR, "# app > div.row > div.container > div.row.row-cols-auto > div > button:nth-child(1)")
    book_cont_btn = (By.CSS_SELECTOR, "# app > div.row > div.container > div.row.row-cols-auto > div > button:nth-child(2)")
    cloud_cont_btn = (By.CSS_SELECTOR, "# app > div.row > div.container > div.row.row-cols-auto > div > button:nth-child(3)")
    support_cont_btn = (By.CSS_SELECTOR, "# app > div.row > div.container > div.row.row-cols-auto > div > button:nth-child(4)")

    # Footer 버튼
    service_btn = (By.CSS_SELECTOR, "#app > div.row > footer > ul > li:nth-child(1) > a")
    Privacy_btn =  (By.CSS_SELECTOR, "#app > div.row > footer > ul > li:nth-child(2) > a")


class login_LocatorFields: # 로그인 페이지 내 요소

    # 로그인 페이지 요소 값
    # login_button = (By.CSS_SELECTOR, "#app > div.container-fluid > header > div > button")
    id_field = (By.ID, "user-id")
    pwd_field = (By.ID, "passwd")
    submit_button = (By.CSS_SELECTOR, "#app > div.container > form > div:nth-child(7) > button")
    warning_message = (By.CSS_SELECTOR, "#app > div.container > form > div.check.red")

class canvas_LocatorFields: # CanVas 페이지 내 요소

    # 새로 만들기 버튼
    New_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.navCont > div.nav > ul > li:nth-child(1) > a")

    # 파일 열기 관련 버튼
    open_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div > div.nav > ul > li:nth-child(2) > a")

    # 파일 추가하기 관련 버튼
    file_add_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.navCont > div.nav > ul > li.nav-item.dropdown")
    file_add_dotcloud = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.navCont > div.nav > ul > li.nav-item.dropdown > ul > li:nth-child(1) > a")

    # 파일 열기/추가 관련 폴더, 파일 관련 버튼
    folder_list = (By.CLASS_NAME, "folder")
    folder_name = "#gridTable > tr > td > div > p.name.text-center"
    folder_items = "#gridTable > tr > td > div > p.item-count.text-center"
    file_list = (By.CLASS_NAME, "file")
    file_name = "#gridTable > tr > td > div > p.name.text-center"

    # 내보내기 버튼
    file_export_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.navCont > div.nav > ul > li:nth-child(4) > a")

    # 저장 관련 버튼
    save_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div > div.nav > ul > li:nth-child(5) > a")

    # 다른 이름 저장 관련 버튼
    saveAs_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.navCont > div.nav > ul > li:nth-child(6) > a")

    # 저장 팝업 텍스트 버튼
    save_textfield = (By.CSS_SELECTOR, "#fileBrowser > div > div > div > form > div.div-button-area > div:nth-child(1) > input")

    # 팝업 내 취소/열기
    confirm_btn = (By.CSS_SELECTOR, ".btn.btn-action.flex-fill")
    cancel_btn = (By.CSS_SELECTOR, ".btn.btn-cancel.flex-fill")

    # 도구 관련 버튼
    tool_list = (By.CSS_SELECTOR, "#tools-container > li")

    # 그리드 버튼
    grid_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.container-fluid.content-area.clearfix > div > main > div.left-column > div.pageCont > div.btn-grid.d-flex.align-items-center.justify-content-center.on")

    # 발표모드 버튼
    Presentation_btn = (By.CSS_SELECTOR, "# app > div.row > div > div > div > div.header > nav > div > div.btn.position-absolute.top-50.translate-middle-y.btn.bg-white.border-0.rounded-5.text-truncate")

    # 페이지 추가 관련 버튼
    canvas_add_btn = (By.CSS_SELECTOR, "#pages > div.page-item.page-item-plus.width.focus > button")

    # 페이지 관련 설명 버튼
    canvas_description_btn = (By.ID, "altText")

