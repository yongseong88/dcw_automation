from TestCase.base_test import BaseTest
from Pages.Canvas_Page import CanVasPage
from Pages.Login_page import LoginPage
from Pages.Main_Page import MainPage
from Test_Senario.CanVas.FileOpen import Open_Senario
from Test_Senario.CanVas.PageAdd import PageAdd_Senario
from Utilities.configreaderutil import readConfig
from Utilities.json_util import root_file_open_get, GNB_CanVas_get, root_file_list_get


class TestCanvas(BaseTest):

  def test_canvas_click(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      main_page = MainPage(self.driver)
      main_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      main_page.canvas_btn_click()

      http_status = GNB_CanVas_get()
      print(f"\r\nStatus Code: {http_status}")
      assert http_status == 200, "CanVas Click Failed"

  def test_canvas_open_popup(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      main_page = MainPage(self.driver)
      open_senario = Open_Senario(self.driver)

      main_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      main_page.canvas_btn_click()
      open_senario.open_popup()

      http_status = root_file_list_get('ROOT')
      print(f"\r\nStatus Code: {http_status.status_code}")
      assert http_status.status_code == 200, "failed"

  def test_canvas_open_cancel(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      main_page = MainPage(self.driver)
      open_senario = Open_Senario(self.driver)

      main_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      main_page.canvas_btn_click()
      open_senario.file_open_cancel()

  def test_canvas_rootfile_open(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      main_page = MainPage(self.driver)
      open_senario = Open_Senario(self.driver)

      main_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      main_page.canvas_btn_click()

      http_status = root_file_open_get(open_senario.root_file_open())
      print(f"\r\nStatus Code: {http_status}")
      assert http_status == 200, "failed"

  def test_canvas_folderfile_open(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      main_page = MainPage(self.driver)
      open_senario = Open_Senario(self.driver)

      main_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      main_page.canvas_btn_click()

      http_status = root_file_open_get(open_senario.folder_file_open())
      print(f"\r\nStatus Code: {http_status}")
      assert http_status == 200, "failed"

  def test_tool(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      main_page = MainPage(self.driver)
      pageadd_senario = PageAdd_Senario(self.driver)

      main_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      main_page.canvas_btn_click()
      pageadd_senario.DTMS_create()

  def tesot_canvas_rootfile_add(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      canvas_page = CanVasPage(self.driver)
      login_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      canvas_page.canvas_btn_click()
      canvas_page.root_file_add()

  def tesot_canvas_folderfile_add(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      canvas_page = CanVasPage(self.driver)
      login_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      canvas_page.canvas_btn_click()
      canvas_page.folder_file_add()

  def tesot_canvas_tool(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      canvas_page = CanVasPage(self.driver)
      login_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      canvas_page.canvas_btn_click()
      canvas_page.tool_btn_click()
      canvas_page.drawing_drag()

  def tesot_canvas_pageadd(self):
      user_id = readConfig("Account", "id")
      user_pwd = readConfig("Account", "password")

      login_page = LoginPage(self.driver)
      canvas_page = CanVasPage(self.driver)
      login_page.login_btn_click()
      login_page.set_id(user_id)
      login_page.set_pwd(user_pwd)
      login_page.login_submit()
      canvas_page.canvas_btn_click()
      canvas_page.page_add()

  def tesot_canvas_save(self):
    user_id = readConfig("Account", "id")
    user_pwd = readConfig("Account", "password")

    login_page = LoginPage(self.driver)
    canvas_page = CanVasPage(self.driver)
    login_page.login_btn_click()
    login_page.set_id(user_id)
    login_page.set_pwd(user_pwd)
    login_page.login_submit()
    canvas_page.canvas_btn_click()
    canvas_page.tool_btn_click()
    canvas_page.drawing_drag()
    canvas_page.description_btn_click("나는 행복 합니다.")
    canvas_page.DTMS_Save("test1234")
    # assert message == "The username or password do not match.", "Asser error"

  def tesot_canvas_saveAs(self):
    user_id = readConfig("Account", "id")
    user_pwd = readConfig("Account", "password")

    login_page = LoginPage(self.driver)
    canvas_page = CanVasPage(self.driver)
    login_page.login_btn_click()
    login_page.set_id(user_id)
    login_page.set_pwd(user_pwd)
    login_page.login_submit()
    canvas_page.canvas_btn_click()
    canvas_page.tool_btn_click()
    canvas_page.drawing_drag()
    canvas_page.description_btn_click("나는 행복 합니다.")
    canvas_page.DTMS_Save("test1234")
    canvas_page.page_add()
    canvas_page.DTMS_SaveAs("dobbu")

  def tesot_Dotpad_connect(self):
    canvas_page = CanVasPage(self.driver)
    canvas_page.add_dotpad()