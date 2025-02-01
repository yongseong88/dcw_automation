from selenium.webdriver.common.by import By


class main_LocatorFields:  #메인 페이지 내 요소

    # GNB 버튼
    canvas_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > nav > ul > li:nth-child(2) > a")
    book_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > nav > ul > li:nth-child(3) > a")
    cloud_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > nav > ul > li:nth-child(4) > a")
    support_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > nav > ul > li:nth-child(5) > a")
    language_dropdown_btn = (By.CSS_SELECTOR,  "#languageDropdown")
    braille_language_dropdown_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > div > div:nth-child(2)")
    braille_languages = (By.CSS_SELECTOR, "#app > div.container-fluid > header > div > div:nth-child(2) > ul > li > a")

    login_btn = (By.CSS_SELECTOR, "#app > div.container-fluid > header > div > button")


    #  버튼
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

    # 파일명 확인
    filename_catch = (By.CLASS_NAME, "my-auto")

    # 새로 만들기 버튼
    New_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.navCont > div.nav > ul > li:nth-child(1) > a")

    # 파일 열기 관련 버튼
    #open_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div > div.nav > ul > li:nth-child(2) > a")
    open_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.nav > ul > li:nth-child(2)")

    # 파일 추가하기 관련 버튼
    # file_add_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.nav > ul > li:nth-child(3)")
    # file_add_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.nav > ul > li.nav-item.dropdown")
    # file_add_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.nav > ul > li.nav-item.dropdown > a")
    file_add_btn = (By.CLASS_NAME, "nav-item.dropdown")
    file_add_dotcloud = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.nav > ul > li.nav-item.dropdown > ul > li:nth-child(1)")

    # 파일 열기/추가 관련 폴더, 파일 관련 버튼
    folder_list = (By.CLASS_NAME, "folder")
    click_folder_name = "#gridTable > tr > td > div > p.name.text-center"
    click_folder_items = "#gridTable > tr > td > div > p.item-count.text-center"
    file_list = (By.CLASS_NAME, "file")
    file_name = "#gridTable > tr > td > div > p.name.text-center"

    # 내보내기 버튼
    file_export_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.navCont > div.nav > ul > li:nth-child(4) > a")

    # 저장 관련 버튼
    save_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.nav > ul > li:nth-child(5) > a")

    # 다른 이름 저장 관련 버튼
    saveAs_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.header > nav > div > div.navCont > div.nav > ul > li:nth-child(6) > a")

    # 저장 팝업 내 텍스트 박스
    save_textfield = (By.CSS_SELECTOR, "#fileBrowser > div > div > div > form > div.div-button-area > div:nth-child(1) > input")

    # 저장 팝업 내 저장/취소 버튼
    # save_confirm_btn = (By.CSS_SELECTOR, "#fileBrowser > div > div > div > form > div.div-button-area > div.div-active > button.btn.btn-action.flex-fill")
    # save_cancel_btn = (By.CSS_SELECTOR, "#fileBrowser > div > div > div > form > div.div-button-area > div.div-active > button.btn.btn-cancel.flex-fill")
    save_confirm_btn = (By.CLASS_NAME, "btn.btn-action.flex-fill")
    save_cancel_btn = (By.CLASS_NAME, "btn.btn-cancelflex.fill")


    # 팝업 내 취소/열기
    confirm_btn = (By.CSS_SELECTOR, ".btn.btn-action.flex-fill")
    cancel_btn = (By.CSS_SELECTOR, ".btn.btn-cancel.flex-fill")

    # 저장 여부 팝업 내 취소/저장
    edit_save_cancel = (By.CLASS_NAME, "swal2-cancel.swal2-styled")


    # 도구 관련 버튼
    tool_list = (By.CSS_SELECTOR, "#tools-container > li")

    undo_btn = (By.CSS_SELECTOR, "#sidebarMenu > div > div > div.actions.d-flex.justify-content-center > button.action-undo")
    redo_btn = (By.CSS_SELECTOR, "#sidebarMenu > div > div > div.actions.d-flex.justify-content-center > button.action-redo")

    # pen_size1 = (By.CSS_SELECTOR, "# sidebarMenu > div > div > div.pen-size-container.size-picker-container.d-flex > div.pen-size-option.size-picker-option.selected.ms-auto")
    pen_size1 = (By.CSS_SELECTOR, f"[aria-label='Pen Size 1px']")
    pen_size2 = (By.CSS_SELECTOR, "#sidebarMenu > div > div > div.pen-size-container.size-picker-container.d-flex > div:nth-child(2)")
    pen_size3 = (By.CSS_SELECTOR, "#sidebarMenu > div > div > div.pen-size-container.size-picker-container.d-flex > div:nth-child(3)")
    pen_size4 = (By.CSS_SELECTOR, "#sidebarMenu > div > div > div.pen-size-container.size-picker-container.d-flex > div.pen-size-option.size-picker-option.me-auto")

    # 그리드 버튼
    grid_btn = (By.CSS_SELECTOR, "#app > div.row > div > div > div > div.container-fluid.content-area.clearfix > div > main > div.left-column > div.pageCont > div.btn-grid.d-flex.align-items-center.justify-content-center.on")

    # 발표모드 버튼
    Presentation_btn = (By.CSS_SELECTOR, "# app > div.row > div > div > div > div.header > nav > div > div.btn.position-absolute.top-50.translate-middle-y.btn.bg-white.border-0.rounded-5.text-truncate")

    foucs_page = (By.CSS_SELECTOR, "# pages > div.page-item.width.d-flex.align-items-center.justify-content-center.active.focus")

    # 페이지 추가 관련 버튼
    canvas_add_btn = (By.CSS_SELECTOR, "#pages > div.page-item.page-item-plus.width > button")
    # canvas_addfull_btn = (By.CSS_SELECTOR, "#pages > div.page-item.page-item-plus.width.disable > button > span.text")
    # canvas_addfull_btn = (By.CSS_SELECTOR, "#pages > div.page-item.page-item-plus.width.disable > button")
    # canvas_addfull_btn = (By.CSS_SELECTOR, "button.btn-icon[aria-label]")
    canvas_addfull_btn = (By.CSS_SELECTOR, f"[aria-label='마지막 페이지입니다.']")
    canvas_page_100 = (By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-backdrop-show")
    # canvas_first_page = (By.CSS_SELECTOR, "#pages > div:nth-child({})".format("1"))
    # canvas_pages = (By.CLASS_NAME, "#pages")
    canvas_pages = (By.CSS_SELECTOR, "#pages > div.page-item.width.d-flex.align-items-center.justify-content-center.active.focus")

    # canvas_pages = (By.CSS_SELECTOR, "#pages > div.page-item.width.d-flex.align-items-center.justify-content-center.active")
    # canvas_pages = (By.CSS_SELECTOR, "#pages > div.page-item.width.d-flex.align-items-center.justify-content-center.active.focus")

    # swal2-title
    # body > div.swal2 - container.swal2 - center.swal2 - backdrop - hide

    # 페이지 관련 설명 버튼
    canvas_description_btn = (By.ID, "altText")

class cloud_LocatorFields:  # CanVas 페이지 내 요소

    # 닷 클라우드
    # cloud_file_list = (By.CLASS_NAME, "grid-table")
    cloud_file_list = (By.CLASS_NAME, "grid-cell") # 닷 클라우드 파일 전체 리스트
    cloud_file_name = "#gridTable > tr > td > div > div > p > span.text-ellipsis" # 파일명, 폴더명
    cloud_file_date = "#gridTable > tr > td > div > div > p.card-text.text-center" # 파일 생성일자, 폴더 갯수
    cloud_page_btn = (By.CSS_SELECTOR, "#app > div.p-2.rounded-4 > div:nth-child(2) > div.d-flex.m-1.px-3.rounded-pill.align-items-center.justify-content-center > nav > ol > li")
    cloud_page_selected_btn = (By.CSS_SELECTOR, "button[class='selected']")
    cloud_context_presentation_btn = (By.CSS_SELECTOR, "# app > div.p-2.rounded-4 > div:nth-child(2) > div.dropdown > ul > li:nth-child(1) > button")
    cloud_context_open_btn = (By.CSS_SELECTOR, "#app > div.p-2.rounded-4 > div:nth-child(2) > div.dropdown > ul > li:nth-child(2) > button")


    # By.CSS_SELECTOR, 'input[tabindex="12"]'
