import re
import time
import math
from selenium.common import NoSuchElementException, TimeoutException
from Pages.Base_Page import BasePage
from Utilities.Locators import cloud_LocatorFields
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from Utilities.json_util import File_group_api


class CloudPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locate = cloud_LocatorFields

    def click_filetype(self, base_url, value, file_type):
        try:
            file_group = File_group_api(base_url)

            paging_list = self.get_elements(self.locate.cloud_page_btn)

            # all_file_count = self.cloud_file_count(base_url)

            # if all_file_count is None:
            #     print(f"file_cnt가 {all_file_count}입니다.")
            #
            # elif len(all_file_count) == 3:
            #     folder_total_page_cnt = all_file_count[0]
            #     dtms_total_file_cnt = all_file_count[1]
            #     dtma_total_file_cnt = all_file_count[2]
            #
            #     print(f"folder_cnt: {folder_total_page_cnt}")
            #     print(f"dtms_file_cnt: {dtms_total_file_cnt}")
            #     print(f"dtma_file_cnt: {dtma_total_file_cnt}")
            #
            # else:
            #     print("아무고토 모타죠")

            for idx, pl in enumerate(paging_list):

                print(f"\nidx: {idx}")

                if idx == 0:
                    random.shuffle(paging_list)
                    print(f"page_list_test: {[elem.text for elem in paging_list]}")

                else:
                    pass

                pl = paging_list[idx] # pl은 이미 paging_list[idx]를 가리킴
                click_page_info = pl.text

                if click_page_info.strip() in {'«', '‹', '›', '»'}:
                    continue

                print(f"page_number: {click_page_info}")

                # if idx == 0:
                #     random.shuffle(paging_list)
                # print(f"페이지 번호 길이: {len(paging_list)}")
                # print(f"page_list_test: {[elem.text for elem in paging_list]}")
                #
                # click_page_info = pl.text
                # if click_page_info.strip() in {'«', '‹', '›', '»'}:
                #     continue

                # match all_file_count:
                #     case [folder_total_page_cnt, dtms_total_file_cnt, dtma_total_file_cnt]:
                #         # folder_page_cnt 설정
                #         folder_page_cnt = 1 if folder_total_page_cnt == 1 else random.randint(1, page_len+1)
                #
                #         # dtms_file_cnt와 dtma_file_cnt 설정 (1 이상이면 랜덤값)
                #         dtms_file_cnt = random.randint(1, page_len+1) if dtms_total_file_cnt >= 1 else 1
                #         dtma_file_cnt = random.randint(1, page_len+1) if dtma_total_file_cnt >= 1 else 1

                # if value == "file" and file_type == "DTMS":
                #     file_search_json = file_group.cloud_group_list_api(base_url, dtms_file_cnt, "ROOT").json()
                # elif value == "file" and file_type == "DTMS":
                #     file_search_json = file_group.cloud_group_list_api(base_url, dtma_file_cnt, "ROOT").json()
                # elif value == "folder":
                #     file_search_json = file_group.cloud_group_list_api(base_url, folder_page_cnt, "ROOT").json()

                file_search_json = file_group.cloud_group_list_api(base_url, int(click_page_info), "ROOT").json()

                for key in file_search_json:
                    if type(file_search_json[key]) is list:
                        random.shuffle(file_search_json[key])

                        for item in file_search_json[key]:
                            # DTMS 파일 값 리턴
                            if 'D' in item['FILE_KEY'] and value == "file" and file_type == "DTMS" and 'audioPath' in item['DTMS_JSON'] and item['DTMS_JSON']['audioPath'] == "":
                                print(f"DTMS 파일명: {item['FILE_NAME']}")
                                return item['FILE_NAME']

                            elif 'D' in item['FILE_KEY'] and value == "file" and file_type == "DTMA" and 'audioPath' in item['DTMS_JSON'] and item['DTMS_JSON']['audioPath'] != "":
                                print(f"DTMA 파일명: {item['FILE_NAME']}")
                                return item['FILE_NAME']

                            elif value == "folder" and 'G' in item['FILE_KEY'] and item["FILE_COUNT"] != "0":
                                folder_in_file_cnt = item['FILE_COUNT']
                                folder_in_page_cnt = math.ceil(int(folder_in_file_cnt) / 18)
                                print(f"item['FILE_NAME']: {item['FILE_NAME']}")
                                print(f"folder_in_page_cnt: {folder_in_page_cnt}")

                                match folder_in_page_cnt:
                                    case 1:
                                        folder_in_pg_ran = folder_in_page_cnt
                                        print(f"folder_in_pg_ran: {folder_in_pg_ran}")
                                    case _:
                                        folder_in_pg_ran = random.randrange(1, folder_in_page_cnt)
                                        print(f"folder_in_pg_ran: {folder_in_pg_ran}")

                                for folder_in_pg_ran in range(1, folder_in_page_cnt + 1):

                                    folder_json = file_group.cloud_group_list_api(base_url, folder_in_pg_ran, item['FILE_KEY']).json()

                                    # 폴더 내 파일 클릭 했을 때의 status 값
                                    for key in folder_json:
                                        if type(folder_json[key]) is list:
                                            random.shuffle(folder_json[key])
                                            for folder_in_item in folder_json[key]:
                                                if file_type == "DTMS" and 'audioPath' in folder_in_item['DTMS_JSON'] and \
                                                        folder_in_item['DTMS_JSON']['audioPath'] == "":

                                                    print(f"click_filetype_폴더명: {item['FILE_NAME']}")
                                                    print(f"click_filetype_파일명: {folder_in_item['FILE_NAME']}")
                                                    return item['FILE_NAME'], folder_in_item['FILE_NAME']

                                                elif file_type == "DTMA" and 'audioPath' in folder_in_item['DTMS_JSON'] and \
                                                        folder_in_item['DTMS_JSON']['audioPath'] != "":

                                                    print(f"click_filetype_폴더명: {item['FILE_NAME']}")
                                                    print(f"click_filetype_파일명: {folder_in_item['FILE_NAME']}")
                                                    return item['FILE_NAME'], folder_in_item['FILE_NAME']

                                                else:
                                                    pass

        except Exception as e:
            print(f"{item['FILE_NAME']}, {folder_in_item['FILE_NAME']} 값 return 중 에러가 발생했습니다: {e}")


    def file_double_click(self, base_url, file_type, file_value):
        try:
            file_group = File_group_api(base_url)
            file_list = file_group.cloud_group_list_api(base_url, 1, "ROOT").json()
            paging_list = self.get_elements(self.locate.cloud_page_btn)
            clickable_page = self.click_filetype(base_url, file_type, file_value)

            list_total_cnt = file_list['TOTAL_COUNT']
            page_len = math.ceil(list_total_cnt / 18)

            print(f"\r\n총 파일 갯수: {list_total_cnt}")
            print(f"총 페이지 수: {page_len}")

            for idx, pl in enumerate(paging_list):
                print(f"page_index: {idx}")

                if idx == 0:
                    random.shuffle(paging_list)
                    print(f"page_list_test: {[elem.text for elem in paging_list]}")

                else:
                    pass

                pl = paging_list[idx] # pl은 이미 paging_list[idx]를 가리킴
                click_page_info = pl.text
                print(f"page_number: {click_page_info}")

                if paging_list[0].text.strip() in {'«', '‹', '1'}:
                    random.shuffle(paging_list)
                    print(f"page_list_test_reshuffle: {[pgl.text for pgl in paging_list]}")
                    time.sleep(2)
                    pl.click()

                pl.click()
                time.sleep(0.5)
                selected_page = WebDriverWait(self.driver, 20).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='selected']"))).text
                print(f"선택된 페이지: {selected_page}")
                time.sleep(6)
                page_file_list = self.get_elements(self.locate.cloud_file_list)

                for pfl in page_file_list:
                    page_in_filename = pfl.text
                    # print(f"page_in_filename: {page_in_filename}")

                    if clickable_page is None:
                        print(f"clickable_page: {clickable_page}입니다. 다음으로 이동 합니다.")

                    elif len(clickable_page) == 2:
                        print(f"clickable_page 길이: {len(clickable_page)}")
                        clickable_folder = clickable_page[0]
                        clickable_folder_in_file = clickable_page[1]
                        click_folder_name = re.sub(r"\s*\d+\s*items", "", page_in_filename)

                        print(f"clickable_folder: {clickable_folder}")
                        print(f"clickable_file: {clickable_folder_in_file}")

                        if clickable_folder == click_folder_name:
                            self.double_click(pfl)
                            time.sleep(5)
                            print(f"clickable_folder: {clickable_folder}")
                            print(f"click_folder_name: {click_folder_name}")
                            print(f"clickable_folder_in_file: {clickable_folder_in_file}")

                            time.sleep(6)
                            cloud_folder_in_list = self.get_elements(self.locate.cloud_file_list)

                            for cfl in cloud_folder_in_list:
                                final_file_name = cfl.text[0:(cfl.text.find("."))]
                                if final_file_name == clickable_folder_in_file:
                                    self.double_click(cfl)
                                    print(f"clickable_folder_in_file: {clickable_folder_in_file}")
                                    print(f"더블 클릭 폴더명: {click_folder_name}")
                                    print(f"더블 클릭 파일명: {final_file_name}")
                                    # print(f"더블 클릭 파일 생성일: {double_click_file_date}")
                                    return clickable_folder, clickable_folder_in_file, selected_page


                        else:
                            print(f"{click_folder_name}과 {clickable_folder}이 일치 하지 않습니다.")

                    else:
                        clickable_file = clickable_page
                        click_file_name = page_in_filename[0:(page_in_filename.find("."))]

                        # print(f"clickable_page 길이: {len(clickable_page)}")
                        # print(f"page_in_filename: {page_in_filename}")
                        # print(f"clickable_file: {clickable_file}")

                        if clickable_file == click_file_name:
                            self.double_click(pfl)
                            time.sleep(5)
                            print(f"clickable_file: {clickable_file}")
                            print(f"click_file_name: {click_file_name}")

                            return clickable_file, selected_page

                        else:
                            print(f"{click_file_name}과 {clickable_file}이 일치 하지 않습니다.")

        except NoSuchElementException as e:
            print(f"요소를 찾을 수 없습니다: {e}")

    def file_context_click(self, base_url, file_type, file_value):
        try:
            file_group = File_group_api(base_url)
            file_list = file_group.cloud_group_list_api(base_url, 1, "ROOT").json()
            paging_list = self.get_elements(self.locate.cloud_page_btn)
            clickable_page = self.click_filetype(base_url, file_type, file_value)

            list_total_cnt = file_list['TOTAL_COUNT']
            page_len = math.ceil(list_total_cnt / 18)

            print(f"\r\n총 파일 갯수: {list_total_cnt}")
            print(f"총 페이지 수: {page_len}")

            for idx, pl in enumerate(paging_list):
                print(f"page_index: {idx}")

                if idx == 0:
                    random.shuffle(paging_list)
                    print(f"page_list_test: {[elem.text for elem in paging_list]}")

                else:
                    pass

                pl = paging_list[idx]  # pl은 이미 paging_list[idx]를 가리킴
                click_page_info = pl.text
                print(f"page_number: {click_page_info}")

                if paging_list[0].text.strip() in {'«', '‹', '1'}:
                    random.shuffle(paging_list)
                    print(f"page_list_test_reshuffle: {[pgl.text for pgl in paging_list]}")
                    time.sleep(2)
                    pl.click()

                pl.click()
                time.sleep(0.5)
                selected_page = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='selected']"))).text
                print(f"선택된 페이지: {selected_page}")
                time.sleep(6)
                page_file_list = self.get_elements(self.locate.cloud_file_list)

                for pfl in page_file_list:
                    page_in_filename = pfl.text
                    # print(f"page_in_filename: {page_in_filename}")

                    if clickable_page is None:
                        print(f"clickable_page: {clickable_page}입니다. 다음으로 이동 합니다.")

                    elif len(clickable_page) == 2:
                        print(f"clickable_page 길이: {len(clickable_page)}")
                        clickable_folder = clickable_page[0]
                        clickable_folder_in_file = clickable_page[1]
                        click_folder_name = re.sub(r"\s*\d+\s*items", "", page_in_filename)

                        print(f"clickable_folder: {clickable_folder}")
                        print(f"clickable_file: {clickable_folder_in_file}")

                        if clickable_folder == click_folder_name:
                            self.context_click(pfl)
                            time.sleep(1)
                            self.click(self.locate.cloud_context_open_btn)
                            time.sleep(5)
                            print(f"clickable_folder: {clickable_folder}")
                            print(f"click_folder_name: {click_folder_name}")
                            print(f"clickable_folder_in_file: {clickable_folder_in_file}")

                            time.sleep(6)
                            cloud_folder_in_list = self.get_elements(self.locate.cloud_file_list)

                            for cfl in cloud_folder_in_list:
                                final_file_name = cfl.text[0:(cfl.text.find("."))]
                                if final_file_name == clickable_folder_in_file:
                                    self.context_click(cfl)
                                    time.sleep(1)
                                    self.click(self.locate.cloud_context_open_btn)
                                    print(f"clickable_folder_in_file: {clickable_folder_in_file}")
                                    print(f"더블 클릭 폴더명: {click_folder_name}")
                                    print(f"더블 클릭 파일명: {final_file_name}")
                                    # print(f"더블 클릭 파일 생성일: {double_click_file_date}")
                                    return clickable_folder, clickable_folder_in_file, selected_page


                        else:
                            print(f"{click_folder_name}과 {clickable_folder}이 일치 하지 않습니다.")

                    else:
                        clickable_file = clickable_page
                        click_file_name = page_in_filename[0:(page_in_filename.find("."))]

                        # print(f"clickable_page 길이: {len(clickable_page)}")
                        # print(f"page_in_filename: {page_in_filename}")
                        # print(f"clickable_file: {clickable_file}")

                        if clickable_file == click_file_name:
                            self.context_click(pfl)
                            time.sleep(1)
                            self.click(self.locate.cloud_context_open_btn)
                            time.sleep(5)
                            print(f"clickable_file: {clickable_file}")
                            print(f"click_file_name: {click_file_name}")

                            return clickable_file, selected_page

                        else:
                            print(f"{click_file_name}과 {clickable_file}이 일치 하지 않습니다.")

        except NoSuchElementException as e:
            print(f"요소를 찾을 수 없습니다: {e}")



























    # def cloud_file_count(self, base_url):
    #     try:
    #         file_group = File_group_api(base_url)
    #         list_json = file_group.cloud_group_list_api(base_url, 1, "ROOT").json()
    #
    #         list_total_cnt = list_json['TOTAL_COUNT']
    #         page_len = math.ceil(list_total_cnt / 18)
    #         paging_list = self.get_elements(self.locate.cloud_page_btn)
    #
    #         folder_cnt = 0
    #         folder_dtms_cnt = 0
    #         folder_dtma_cnt = 0
    #         root_dtms_cnt = 0
    #         root_dtma_cnt = 0
    #
    #         for idx, pl in enumerate(paging_list):
    #
    #             print(f"\nidx: {idx}")
    #             # print(f"페이지 번호 길이: {len(paging_list)}")
    #             # print(f"page_list_test: {[elem.text for elem in paging_list]}")
    #
    #             click_page_info = pl.text
    #             if click_page_info.strip() in {'«', '‹', '›', '»'}:
    #                 continue
    #
    #             # print(f"page_number: {click_page_info}")
    #             time.sleep(4)
    #
    #             file_list_json = file_group.cloud_group_list_api(base_url, click_page_info.strip(), "ROOT").json()
    #
    #             for key in file_list_json:
    #                 if type(file_list_json[key]) is list:
    #                     # random.shuffle(file_list_json[key])
    #                     for item in file_list_json[key]:
    #                         # DTMS 파일 값 리턴
    #                         if 'D' in item['FILE_KEY'] and 'audioPath' in item[
    #                             'DTMS_JSON'] and item['DTMS_JSON']['audioPath'] == "":
    #                             # print(f"DTMS 파일명: {item['FILE_NAME']}")
    #                             root_dtms_cnt += 1
    #                             # return dtms_cnt
    #                             # return item['FILE_NAME']
    #
    #                         elif 'D' in item['FILE_KEY'] and 'audioPath' in item[
    #                             'DTMS_JSON'] and item['DTMS_JSON']['audioPath'] != "":
    #                             root_dtma_cnt += 1
    #                             # print(f"DTMA 파일명: {item['FILE_NAME']}")
    #                             # return dtma_cnt
    #                             # return item['FILE_NAME']
    #
    #                         elif 'G' in item['FILE_KEY'] and item["FILE_COUNT"] != "0":
    #                             folder_cnt += 1
    #                             folder_json = file_group.cloud_group_list_api(base_url, click_page_info.strip(), item['FILE_KEY']).json()
    #
    #                             # 폴더 내 파일 클릭 했을 때의 status 값
    #                             for key in folder_json:
    #                                 if type(folder_json[key]) is list:
    #                                     random.shuffle(folder_json[key])
    #                                     for folder_in_item in folder_json[key]:
    #                                         if 'audioPath' in folder_in_item['DTMS_JSON'] and \
    #                                                 folder_in_item['DTMS_JSON']['audioPath'] == "":
    #
    #                                             folder_dtms_cnt += 1
    #                                             # print(f"click_filetype_폴더명: {item['FILE_NAME']}")
    #                                             # print(f"click_filetype_파일명: {folder_in_item['FILE_NAME']}")
    #                                             # return folder_cnt, dtms_cnt
    #                                             # return item['FILE_NAME'], folder_in_item['FILE_NAME']
    #
    #                                         elif 'audioPath' in folder_in_item['DTMS_JSON'] and \
    #                                                 folder_in_item['DTMS_JSON']['audioPath'] != "":
    #
    #                                             folder_dtma_cnt += 1
    #                                             # print(f"click_filetype_폴더명: {item['FILE_NAME']}")
    #                                             # print(f"click_filetype_파일명: {folder_in_item['FILE_NAME']}")
    #                                             # return folder_cnt, dtma_cnt
    #                                             # return item['FILE_NAME'], folder_in_item['FILE_NAME']
    #
    #                                         else:
    #                                             pass
    #
    #         folder_page_totalcnt = math.ceil(folder_cnt / 18)
    #
    #         return folder_page_totalcnt, root_dtms_cnt, root_dtma_cnt
    #
    #     except Exception as e:
    #         print(f"오류 발생: {e}")










