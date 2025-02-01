from datetime import datetime
from Utilities.configreaderutil import readConfig
import requests


class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.env = "dev" if "dev" in base_url else "prod"
        self.config = self._load_config()

    def _load_config(self):
        return {
            "SITE_NO": readConfig("USER_INFO", f"{self.env}_SITE_NO"),
            "USER_NO": readConfig("USER_INFO", f"{self.env}_USER_NO"),
            "COMP_NO": readConfig("USER_INFO", "COMP_NO"),
        }

    def _build_url(self):
        return f"{self.base_url}"

class User_api(BaseApi):
    def login_check_api(self, id, pwd):  # 로그인은 POST 방식으로

        if "dev" in self.env:
            login_url = f"https://dev-account.dotincorp.com/user-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/login"
        else:
            login_url = f"https://account.dotincorp.com/user-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/login"

        data = {
            'USER_ID': id,
            'PASSWD': pwd
        }

        login_info = requests.post(url=login_url, data=data)

        return login_info

    def user_status_api(self, base_url):
        user_url = f"{base_url}/user-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/language"

        param_info = {
            "USER_NO": self.config['USER_NO'],
            "SITE_NO": self.config['SITE_NO'],
            "COMP_NO": self.config['COMP_NO'],
            "LANGUAGE_TYPE": "1"
        }

        user_url_api = requests.get(url=user_url, params=param_info)

        return user_url_api

        # if "dev" in base_url:
        #
        #     user_url = "{}/user-app/v1/sites/{}-{}/users/{}/language".format(
        #         base_url,
        #         readConfig("USER_INFO", "dev_SITE_NO"),
        #         readConfig("USER_INFO", "dev_USER_NO"),
        #         readConfig("USER_INFO", "COMP_NO"))
        #
        #     param_info = {
        #         "USER_NO": readConfig("USER_INFO", "dev_USER_NO"),
        #         "SITE_NO": readConfig("USER_INFO", "dev_SITE_NO"),
        #         "COMP_NO": readConfig("USER_INFO", "COMP_NO"),
        #         "LANGUAGE_TYPE": "1"
        #     }
        #
        # elif "dev" not in base_url:
        #     user_url = "{}/user-app/v1/sites/{}-{}/users/{}/language".format(
        #         base_url,
        #         readConfig("USER_INFO", "prod_SITE_NO"),
        #         readConfig("USER_INFO", "prod_USER_NO"),
        #         readConfig("USER_INFO", "COMP_NO"))
        #
        #     param_info = {
        #         "USER_NO": readConfig("USER_INFO", "prod_USER_NO"),
        #         "SITE_NO": readConfig("USER_INFO", "prod_SITE_NO"),
        #         "COMP_NO": readConfig("USER_INFO", "COMP_NO"),
        #         "LANGUAGE_TYPE": "1"
        #     }

        # if "dev" in self.env:
        #     user_url = f"{base_url}/user-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/language"
        # else:
        #     user_url = f"{base_url}/user-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/language"



    def menus_api(self, base_url):
        menus_url = f"{base_url}/site-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/menus"

        user_menus_api = requests.get(url=menus_url)

        return user_menus_api

        # if "dev" in self.env:
        #     menus_url = f"{base_url}/site-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/menus"
        # else:
        #     menus_url = f"{base_url}/site-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/menus"



    def BrailleLanguage_change_api(self, base_url, lang, lang_option):
        BrLanguage_url = f"{base_url}/user-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/language"

        change_data = {
            "USER_NO": self.config['USER_NO'],
            "SITE_NO": self.config['SITE_NO'],
            "COMP_NO": self.config['COMP_NO'],
            "ENGINE": "0",
            "LANGUAGE_TYPE": "1",
            "LANGUAGE": lang,
            "LANGUAGE_OPTION": lang_option,
            "PIN": 6
        }

        headers = {
            "Content-Type": "application/json"
        }

        BrLanguage_info = requests.put(url=BrLanguage_url, json=change_data, headers=headers)

        return BrLanguage_info

        # if "dev" in base_url:
        #     BrLanguage_url = f"{base_url}/user-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/language"
        #
        #
        # elif "dev" not in base_url:
        #     BrLanguage_url = f"{base_url}/user-app/v1/sites/{self.config['SITE_NO']}-{self.config['COMP_NO']}/users/{self.config['USER_NO']}/language"



class Drive_api(BaseApi):
    def filebrowser_list_api(self, base_url, group_no):
        file_list_url = f"{base_url}/drive-app/v1/dtms/groups"

        param_info = {
            "PARENT_GROUP_NO": group_no,
            "COMP_NO": self.config['COMP_NO'],
            "DRIVER_KIND": "P",
            "USER_NO": self.config['USER_NO']
        }

        popup_list_api = requests.get(url=file_list_url, params=param_info)

        return popup_list_api

        # if "dev" in self.env:
        #     file_list_url = f"{base_url}/drive-app/v1/dtms/groups"
        # else:
        #     file_list_url = f"{base_url}/drive-app/v1/dtms/groups"



    def file_open_api(self, base_url, filekey):
        file_open_url = f"{base_url}/drive-app/v1/dtm/images/{filekey}/device/300/to-dtms"

        file_open_api = requests.get(url=file_open_url)

        return file_open_api


    def file_key_search(self, base_url, file_name, folder_in_filename=None):

        filelist_json = self.filebrowser_list_api(base_url, 'ROOT').json()

        for key in filelist_json:
            if type(filelist_json[key]) is list:
                for item in filelist_json[key]:
                    # 선택한게 파일인지 폴더인지 구분 하는 로직
                    if item['FILE_NAME'] == file_name and 'D' in item['FILE_KEY']:
                        print(f"ROOT 내 파일: {item['FILE_NAME']}")

                        return item['FILE_KEY']

                    elif item['FILE_NAME'] == file_name and 'G' in item['FILE_KEY']:
                        # print(f"폴더명: {item['FILE_NAME']}")

                        folder_json = self.filebrowser_list_api(base_url, item['FILE_KEY']).json()

                        # 폴더 내 파일 클릭 했을 때의 status 값
                        for key in folder_json:
                            if type(folder_json[key]) is list:
                                for folder_in_item in folder_json[key]:
                                    if folder_in_item['FILE_NAME'] == folder_in_filename:
                                        print(f"우히히 폴더명: {item['FILE_NAME']}")
                                        print(f"폴더 내 파일명: {folder_in_item['FILE_NAME']}")
                                        return item['FILE_KEY'], folder_in_item['FILE_KEY']
                                    else:
                                        pass

    def dtms_data(self, base_url, file_name, dtms_file_name=None):
    # def dtms_data(self, file_path, dtms_file_name):
        time1 = None
        folder_time1 = None
        latest_item = None

        filelist_json = self.filebrowser_list_api(base_url, 'ROOT').json()

        for key in filelist_json:
            if type(filelist_json[key]) is list:
                for item in filelist_json[key]:
                    if file_name == item['FILE_NAME'] and 'D' in item['FILE_KEY']:
                        time_str1 = item['MOD_DATE']
                        time2 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")
                        print(f"파일명: {item['FILE_NAME']}")

                        if time1 is None or time1 < time2:
                            time1 = time2
                            latest_item = item
                            print(f"time1: {time1} 이 최근입니다.")
                            time_str = datetime.strftime(time1, "%Y-%m-%d %H:%M:%S.") + str(time1.microsecond)[:1]
                            print(f"time_str: {time_str}")
                            return latest_item['DTMS_JSON']

                        else:
                            print("파일이 없습니다.")

                    elif file_name == item['FILE_NAME'] and 'G' in item['FILE_KEY']:
                        folder_json = self.filebrowser_list_api(base_url, item['FILE_KEY']).json()

                        for key in folder_json:
                            if type(folder_json[key]) is list:
                                for folder_in_item in folder_json[key]:
                                    if dtms_file_name == folder_in_item['FILE_NAME']:

                                        folder_time_str1 = folder_in_item['MOD_DATE']
                                        folder_time2 = datetime.strptime(folder_time_str1, "%Y-%m-%d %H:%M:%S.%f")

                                        if folder_time1 is None or folder_time1 < folder_time2:
                                            folder_time1 = folder_time2
                                            latest_item = folder_in_item
                                            print(f"folder_time1: {folder_time1} 이 최근입니다.")
                                            folder_time_str = datetime.strftime(folder_time1,
                                                                                "%Y-%m-%d %H:%M:%S.") + str(
                                                folder_time1.microsecond)[:1]
                                            print(f"folder_time_str: {folder_time_str}")
                                            return latest_item['DTMS_JSON']

                                        else:
                                            print("파일이 없습니다.")

                                    else:
                                        pass

    def dtms_save_api(self, base_url, file_name, dtms, internal_file=None):  # DTMS 파일 저장 POST 200
    # def dtms_save_api(self, save_path, file_name, dtms):  # DTMS 파일 저장 POST 200

        save_file_key = self.file_key_search(base_url, file_name, internal_file)

        if save_file_key is None:
            print("파일 키를 찾을 수 없습니다.")
            return None  # 파일 키를 찾지 못했을 경우 None 반환

        if isinstance(save_file_key, str):
            save_url = f"{base_url}/drive-app/v1/dtm/images/{save_file_key}/from-dtms"

            save_data = {
                "USER_NO": self.config['USER_NO'],
                "DTM_GROUP_NO": "ROOT",
                "DTMS_JSON": dtms,
                "DTM_NAME": file_name,
                "DTM_DESC": "",
                "DEVICE_KIND": "300",
                "DTMS_TYPE": "dtms",
                "DTMS_GROUP_NO": "ROOT"

            }

            save_info = requests.post(url=save_url, data=save_data)

            return save_info

            # save_file_key = self.file_key_searchi(base_url, file_name)
            # if "dev" in self.env:
            #     save_url = f"{base_url}/drive-app/v1/dtm/images/{save_file_key[0]}/from-dtms"
            # else:
            #     save_url = f"{base_url}/drive-app/v1/dtm/images/{save_file_key[0]}/from-dtms"



        elif isinstance(save_file_key, (list, tuple)):

            save_url = f"{base_url}/drive-app/v1/dtm/images/{save_file_key[1]}/from-dtms"

            save_data = {
                "USER_NO": self.config['USER_NO'],
                "DTM_GROUP_NO": save_file_key[0],
                "DTMS_JSON": dtms,
                "DTM_NAME": file_name,
                "DTM_DESC": "",
                "DEVICE_KIND": "300",
                "DTMS_TYPE": "dtms",
                "DTMS_GROUP_NO": save_file_key[0]

            }

            save_info = requests.post(url=save_url, data=save_data)

            return save_info

        else:
            # 처리할 수 없는 경우 에러 메시지를 출력
            print(f"save_file_key 길이는 {len(save_file_key)}입니다.")
            return None

        # if "dev" in self.env:
        #     save_url = f"{base_url}/drive-app/v1/dtm/images/{save_file_key[1]}/from-dtms"
        # else:
        #     save_url = f"{base_url}/drive-app/v1/dtm/images/{save_file_key[1]}/from-dtms"

    # def file_key_searchi(self, base_url, filename):
    #
    #     try:
    #
    #         filelist_json = self.filebrowser_list_api(base_url, 'ROOT').json()
    #
    #         found_item_file_key = None
    #         found_folder_file_key = None
    #
    #         for key in filelist_json:
    #             if type(filelist_json[key]) is list:
    #                 for item in filelist_json[key]:
    #
    #                     # 선택한게 파일인지 폴더인지 구분 하는 로직
    #                     if 'D' in item['FILE_KEY']:
    #                         # print(f"ROOT 내 파일: {item['FILE_NAME']}")
    #
    #                         if filename == item['FILE_NAME']:
    #                             print(f"{item['FILE_NAME']}은 일치 하는 파일 입니다.")
    #                             # found_item_file_key = item['FILE_KEY']
    #                             return item['FILE_KEY']
    #
    #                         else:
    #                             print(f"{item['FILE_NAME']}는 찾는 파일이 아닙니다.")
    #
    #                         # return item['FILE_KEY']
    #
    #                     elif 'G' in item['FILE_KEY']:
    #                         folder_json = self.filebrowser_list_api(base_url, item['FILE_KEY']).json()
    #
    #                         # 폴더 내 파일 클릭 했을 때의 status 값
    #                         for key in folder_json:
    #                             if type(folder_json[key]) is list:
    #                                 for folder_in_item in folder_json[key]:
    #                                     if filename == folder_in_item['FILE_NAME']:
    #                                         print(f"우히히 폴더명: {item['FILE_NAME']}")
    #                                         print(f"폴더 내 파일명: {folder_in_item['FILE_NAME']}")
    #                                         # found_item_file_key = item['FILE_KEY']
    #                                         # found_folder_file_key = folder_in_item['FILE_KEY']
    #                                         return item['FILE_KEY'], folder_in_item['FILE_KEY']
    #
    #                                     else:
    #                                         # print(f"{item['FILE_NAME']} 없습니다.")
    #                                         print(f"탐색 중인 폴더: {item['FILE_NAME']}")
    #                                         print(f"{folder_in_item['FILE_NAME']}는 찾는 파일이 아닙니다.")
    #
    #     except UnboundLocalError:
    #         print("folder_in_item이 정의되지 않았습니다.")

    # def dtms_create_api(self, create_path, file_name, dtms):  # DTMS 파일 저장 POST 201
    #
    #     create_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/from-dtms'
    #
    #     if create_path == 'ROOT':
    #
    #         create_data = {
    #             "USER_NO": readConfig("USER_INFO", "USER_NO"),
    #             "DTM_GROUP_NO": 'ROOT',
    #             "DTMS_JSON": dtms,
    #             "DTM_NAME": file_name,
    #             "DTM_DESC": "",
    #             "DEVICE_KIND": "300",
    #             "DTMS_TYPE": "dtms"
    #         }
    #
    #         print(f"최신 파일명_post201: {file_name}")
    #         print(f"최신 파일 DTMS_JSON값_post201: {dtms}")
    #
    #     elif create_path != 'ROOT':
    #
    #         folder_file_key, folder_in_file_key = self.file_key_search(create_path, file_name)
    #         print(f"dd: {folder_file_key}")
    #         print(f"tt: {folder_in_file_key}")
    #
    #         create_data = {
    #             "USER_NO": readConfig("USER_INFO", "USER_NO"),
    #             "DTM_GROUP_NO": folder_file_key,
    #             "DTMS_JSON": dtms,
    #             "DTM_NAME": file_name,
    #             "DTM_DESC": "",
    #             "DEVICE_KIND": "300",
    #             "DTMS_TYPE": "dtms"
    #         }
    #
    #         print(f"최신 파일명_post201: {file_name}")
    #         print(f"최신 파일 DTMS_JSON값_post201: {dtms}")
    #
    #         # print(f"Preparing to send POST request for file: {latest_item['FILE_NAME']}")
    #         # print(f"DTMS_JSON: {latest_item['DTMS_JSON']}")
    #
    #     else:
    #         print("No latest item found for POST request.")
    #         return None
    #
    #     create_info = requests.post(url=create_url, json=create_data)
    #     return create_info

        # save_url과 save_data가 유효한 경우에만 POST 요청 수행
        # if save_url and save_data:
        #     save_info = requests.post(url=save_url, data=save_data)
        #     return save_info
        # else:
        #     print("save_url 또는 save_data가 올바르지 않습니다.")
        #     return None

        # if save_path == 'ROOT':
        #
        #     root_file_key = self.file_key_search(file_name)
        #
        #     save_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/from-dtms'.format(root_file_key)
        #
        #     save_data = {
        #         "USER_NO": readConfig("USER_INFO", "USER_NO"),
        #         "DTM_GROUP_NO": "ROOT",
        #         "DTMS_JSON": dtms,
        #         "DTM_NAME": file_name,
        #         "DTM_DESC": "",
        #         "DEVICE_KIND": "300",
        #         "DTMS_TYPE": "dtms",
        #         "DTMS_GROUP_NO": "ROOT"
        #
        #     }
        #
        #     # print(f"최신 시간_post200: {time1}")
        #     print(f"최신 파일명_post200: {file_name}")
        #     print(f"최신 파일 DTMS_JSON값_post200: {dtms}")
        #     # print(f"최신 파일 저장 시간_post200: {latest_item['MOD_DATE']}")
        #
        # elif save_path != 'ROOT':
        #
        #     folder_key, folder_in_key = self.file_key_search(save_path, file_name)
        #
        #     save_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/from-dtms'.format(folder_in_key)
        #
        #     save_data = {
        #         "USER_NO": readConfig("USER_INFO", "USER_NO"),
        #         "DTM_GROUP_NO": folder_key,
        #         "DTMS_JSON": dtms,
        #         "DTM_NAME": file_name,
        #         "DTM_DESC": "",
        #         "DEVICE_KIND": "300",
        #         "DTMS_TYPE": "dtms",
        #         "DTMS_GROUP_NO": folder_key
        #
        #     }
        #
        #     # print(f"최신 시간_post200: {time1}")
        #     print(f"최신 파일명_post200: {file_name}")
        #     print(f"최신 파일 DTMS_JSON값_post200: {dtms}")
        #     # print(f"최신 파일 저장 시간_post200: {latest_item['MOD_DATE']}")
        #
        # else:
        #     print("최신 항목이 없습니다.")

        # save_info = requests.post(url=save_url, data=save_data)
        # return save_info



class Braille_api(BaseApi):
    def multiline_api(self, page_num, description, base_url):
        translation_multiline_info = f"{base_url}/braille-app/v1/braille/translation-multiline"

        user_api = User_api(base_url)
        user_info = user_api.user_status_api(base_url).json()
        # print(f"user_info.json(): {user_info}")

        multiline_data = {
            "LANGUAGE": user_info['LANGUAGE'],
            "OPTION": user_info['LANGUAGE_OPTION'],
            "CELL": "20",
            "TEXT": "{current_page_num}p/{total_page_num}p {text}".format(current_page_num=page_num,
                                                                          total_page_num=page_num, text=description)
        }

        multiline_info = requests.post(url=translation_multiline_info, data=multiline_data)

        return multiline_info



class File_group_api(BaseApi):
    def cloud_group_path_api(self, base_url):
        cloud_group_path_url = f"{base_url}/drive-app/v1/dtms/group/path"

        param_info = {
            "DRIVER_KIND": "P",
            "USER_NO": self.config['USER_NO']
        }

        cloud_group_path_url_api = requests.get(url=cloud_group_path_url, params=param_info)

        return cloud_group_path_url_api

        # if "dev" in base_url:
        #     cloud_group_path_url = "{}/drive-app/v1/dtms/group/path".format(base_url)
        #
        #     param_info = {
        #         "DRIVER_KIND": "P",
        #         "USER_NO": "dev_USER_NO"
        #     }
        #
        # elif "dev" not in base_url:
        #     cloud_group_path_url = "{}/drive-app/v1/dtms/group/path".format(base_url)
        #
        #     param_info = {
        #         "DRIVER_KIND": "P",
        #         "USER_NO": "prod_USER_NO"
        #     }



    def cloud_group_list_api(self, base_url, current_page, group_no):
        cloud_group_list_url = f"{base_url}/drive-app/v1/dtms/groups"

        param_info = {
            "PAGE_NO": current_page,
            "PAGE_SIZE": "18",
            "COMP_NO": self.config['COMP_NO'],
            "PARENT_GROUP_NO": group_no,
            "DRIVER_KIND": "P",
            "USER_NO": self.config['USER_NO'],
            "APP_TYPE": "A"
        }

        cloud_group_list_url_api = requests.get(url=cloud_group_list_url, params=param_info)

        return cloud_group_list_url_api

        # if "dev" in base_url:
        #     cloud_group_list_url = "{}/drive-app/v1/dtms/groups".format(base_url)
        #
        #     param_info = {
        #         "PAGE_NO": "1",
        #         "PAGE_SIZE": "18",
        #         "COMP_NO": readConfig("USER_INFO", "COMP_NO"),
        #         "PARENT_GROUP_NO": "ROOT",
        #         "DRIVER_KIND": "P",
        #         "USER_NO": readConfig("USER_INFO", "dev_USER_NO"),
        #         "APP_TYPE": "A"
        #     }
        #
        # elif "dev" not in base_url:
        #     cloud_group_list_url = "{}/drive-app/v1/dtms/groups".format(base_url)
        #
        #     param_info = {
        #         # "PAGE_NO": "1",
        #         # "PAGE_SIZE": "18",
        #         "COMP_NO": readConfig("USER_INFO", "COMP_NO"),
        #         "PARENT_GROUP_NO": "ROOT",
        #         "DRIVER_KIND": "P",
        #         "USER_NO": readConfig("USER_INFO", "prod_USER_NO"),
        #         "APP_TYPE": "A"
        #     }




























    # filelist_json = filebrowser_list_api('ROOT').json()
    # time1 = None
    #
    # for key in filelist_json:
    #     if type(filelist_json[key]) is list:
    #         for item in filelist_json[key]:
    #             if item['FILE_NAME'] in file_name and save_path == 'ROOT':
    #                 time_str1 = item['MOD_DATE']
    #                 time2 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")
    #
    #                 if time1 is None or time1 < time2:
    #                     time1 = time2
    #                     latest_item = item
    #                     print(f"time1: {time1} 이 최근입니다.")
    #                     time_str = datetime.strftime(time1, "%Y-%m-%d %H:%M:%S.") + str(time1.microsecond)[:1]
    #                     print(f"time_str: {time_str}")
    #                     print(f"파일명: {item['FILE_NAME']}")
    #                 else:
    #                     print("파일이 없습니다.")
    #
    #             elif save_path != 'ROOT':
    #                 if item['FILE_NAME'] in save_path:
    #                     time_str1 = item['REG_DATE']
    #                     time2 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")
    #
    #                     if time1 is None or time1 < time2:
    #                         time1 = time2
    #                         # latest_item = item
    #                         print(f"time1: {time1} 이 최근입니다.")
    #                         time_str = datetime.strftime(time1, "%Y-%m-%d %H:%M:%S.") + str(time1.microsecond)[:1]
    #                         print(f"time_str: {time_str}")
    #                         print(f"폴더명: {item['FILE_NAME']}")
    #                     else:
    #                         print("파일이 없습니다.")
    #
    #                     folder_json = filebrowser_list_api(item['FILE_KEY']).json()
    #
    #                     for key in folder_json:
    #                         if type(folder_json[key]) is list:
    #                             for folder_in_item in folder_json[key]:
    #                                 if folder_in_item['FILE_NAME'] in file_name:
    #                                     print(f"폴더 filekey: {item['FILE_KEY']}")
    #                                     time_str1 = folder_in_item['MOD_DATE']
    #                                     time2 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")
    #
    #                                     if time1 is None or time1 < time2:
    #                                         time1 = time2
    #                                         latest_item = folder_in_item
    #                                         print(f"time1: {time1} 이 최근입니다.")
    #                                         time_str = datetime.strftime(time1, "%Y-%m-%d %H:%M:%S.") + str(
    #                                             time1.microsecond)[:1]
    #                                         print(f"time_str: {time_str}")
    #                                     else:
    #                                         print("파일이 없습니다.")
    #                                 else:
    #                                     pass

                    # save_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/from-dtms'.format(item['FILE_KEY'])
                    #
                    # save_data = {
                    #     "USER_NO": readConfig("USER_INFO", "USER_NO"),
                    #     "DTM_GROUP_NO": "ROOT",
                    #     "DTMS_JSON": item['DTMS_JSON'],
                    #     "DTM_NAME": file_name,
                    #     "DTM_DESC": "",
                    #     "DEVICE_KIND": "300",
                    #     "DTMS_TYPE": "dtms",
                    #     "DTMS_GROUP_NO": "ROOT"
                    #
                    # }
                    #
                    # print(f"최신 시간_post200: {time_str}")
                    # print(f"최신 파일명_post200: {item['FILE_NAME']}")
                    # print(f"최신 파일 DTMS_JSON값_post200: {item['DTMS_JSON']}")
                    # print(f"최신 파일 저장 시간_post200: {item['MOD_DATE']}")

                    # save_info = requests.post(url=save_url, data=save_data)
                    # return save_info



                    # save_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/from-dtms'.format(folder_in_item['FILE_KEY'])
                    #
                    # save_data = {
                    #     "USER_NO": readConfig("USER_INFO", "USER_NO"),
                    #     "DTM_GROUP_NO": item['FILE_KEY'],
                    #     "DTMS_JSON": folder_in_item['DTMS_JSON'],
                    #     "DTM_NAME": file_name,
                    #     "DTM_DESC": "",
                    #     "DEVICE_KIND": "300",
                    #     "DTMS_TYPE": "dtms",
                    #     "DTMS_GROUP_NO": item['FILE_KEY']
                    #
                    # }
                    #
                    # print(f"최신 시간_post200: {time_str}")
                    # print(f"최신 파일명_post200: {item['FILE_NAME']}")
                    # print(f"최신 파일 DTMS_JSON값_post200: {item['DTMS_JSON']}")
                    # print(f"최신 파일 저장 시간_post200: {item['MOD_DATE']}")

    # if latest_item:
    #
    #     if save_path == 'ROOT':
    #
    #         save_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/from-dtms'.format(latest_item['FILE_KEY'])
    #
    #         save_data = {
    #             "USER_NO": readConfig("USER_INFO", "USER_NO"),
    #             "DTM_GROUP_NO": "ROOT",
    #             "DTMS_JSON": latest_item['DTMS_JSON'],
    #             "DTM_NAME": latest_item['FILE_NAME'],
    #             "DTM_DESC": "",
    #             "DEVICE_KIND": "300",
    #             "DTMS_TYPE": "dtms",
    #             "DTMS_GROUP_NO": "ROOT"
    #
    #         }
    #
    #         print(f"최신 시간_post200: {time1}")
    #         print(f"최신 파일명_post200: {latest_item['FILE_NAME']}")
    #         print(f"최신 파일 DTMS_JSON값_post200: {latest_item['DTMS_JSON']}")
    #         print(f"최신 파일 저장 시간_post200: {latest_item['MOD_DATE']}")
    #
    #     elif save_path != 'ROOT':
    #
    #         save_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/from-dtms'.format(latest_item['FILE_KEY'])
    #
    #         save_data = {
    #                     "USER_NO": readConfig("USER_INFO", "USER_NO"),
    #                     "DTM_GROUP_NO": item['FILE_KEY'],
    #                     "DTMS_JSON": latest_item['DTMS_JSON'],
    #                     "DTM_NAME": latest_item['FILE_NAME'],
    #                     "DTM_DESC": "",
    #                     "DEVICE_KIND": "300",
    #                     "DTMS_TYPE": "dtms",
    #                     "DTMS_GROUP_NO": item['FILE_KEY']
    #
    #         }
    #
    #         print(f"최신 시간_post200: {time1}")
    #         print(f"최신 파일명_post200: {latest_item['FILE_NAME']}")
    #         print(f"최신 파일 DTMS_JSON값_post200: {latest_item['DTMS_JSON']}")
    #         print(f"최신 파일 저장 시간_post200: {latest_item['MOD_DATE']}")
    #
    # else:
    #     print("최신 항목이 없습니다.")
    #
    # save_info = requests.post(url=save_url, data=save_data)
    # return save_info



    # if latest_item:
    #     print(f"최신 시간_post200: {time_str}")
    #     print(f"최신 파일명_post200: {latest_item['FILE_NAME']}")
    #     print(f"최신 파일 DTMS_JSON값_post200: {latest_item['DTMS_JSON']}")
    #     print(f"최신 파일 저장 시간_post200: {latest_item['MOD_DATE']}")
    #
    #     save_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/from-dtms'.format(latest_item['FILE_KEY'])
    #
    #     save_data = {
    #         "USER_NO": readConfig("USER_INFO", "USER_NO"),
    #         "DTM_GROUP_NO": file_path,
    #         "DTMS_JSON": latest_item['DTMS_JSON'],
    #         "DTM_NAME": file_name,
    #         "DTM_DESC": "",
    #         "DEVICE_KIND": "300",
    #         "DTMS_TYPE": "dtms",
    #         "DTMS_GROUP_NO": file_path
    #
    #     }
    # else:
    #     pass

    # save_info = requests.post(url=save_url, data=save_data)
    # return save_info

    # for key in filelist_json:
    #     if type(filelist_json[key]) is list:
    #         for item in filelist_json[key]:
    #             if file_name in item['FILE_NAME']:
    #                 # print("FILE_NAME값: {}".format(item['FILE_NAME']))
    #                 # print("DTMS_JSON값: {}".format(item['DTMS_JSON']))
    #                 # print("REG_DATE값: {}".format(item['REG_DATE']))
    #
    #                 time_str1 = item['REG_DATE']
    #                 time2 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")
    #
    #                 if time1 is None or time1 < time2:
    #                     time1 = time2
    #                     latest_item = item
    #                     print(f"time1: {time1} 이 최근입니다.")
    #
    #                 time_str = datetime.strftime(time1, "%Y-%m-%d %H:%M:%S.") + str(time1.microsecond)[:1]
    #                 print(f"time_str: {time_str}")
    #
    #             else:
    #                 pass
    #
    # if latest_item:
    #     print(f"최신 시간_post200: {time_str}")
    #     print(f"최신 파일명_post200: {latest_item['FILE_NAME']}")
    #     print(f"최신 파일 DTMS_JSON값_post200: {latest_item['DTMS_JSON']}")
    #     print(f"최신 파일 저장 시간_post200: {latest_item['REG_DATE']}")
    #
    #     save_url = 'https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/from-dtms'.format(item['FILE_KEY'])
    #
    #     save_data = {
    #         "USER_NO": readConfig("USER_INFO", "USER_NO"),
    #         "DTM_GROUP_NO": file_path,
    #         "DTMS_JSON": item['DTMS_JSON'],
    #         "DTM_NAME": file_name,
    #         "DTM_DESC": "",
    #         "DEVICE_KIND": "300",
    #         "DTMS_TYPE": "dtms",
    #         "DTMS_GROUP_NO": file_path
    #
    #     }
    # else:
    #     pass
    #
    #
    # save_info = requests.post(url=save_url, data=save_data)
    # return save_info
