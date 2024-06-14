from Utilities.configreaderutil import readConfig
import requests
import pprint

def login_post(id, pwd):

    login_url = 'https://dev-account.dotincorp.com/user-app/v1/sites/{}-{}/login'.format(readConfig("USER_INFO", "SITE_NO"), readConfig("USER_INFO", "COMP_NO"))

    data = {
        # 'USER_ID': readConfig("Account", "id"),
        # 'PASSWD': readConfig("Account", "password"),
        'USER_ID': id,
        'PASSWD': pwd
    }

    login_api = requests.post(url=login_url, data=data)

    return login_api.status_code


def GNB_CanVas_get():

    user_url = "https://dev-apps.dotincorp.com/user-app/v1/sites/{}-{}/users/{}/language".format(readConfig("USER_INFO", "SITE_NO"), readConfig("USER_INFO", "COMP_NO"), readConfig("USER_INFO", "USER_NO"))

    param_info = {
        "USER_NO": readConfig("USER_INFO", "USER_NO"),
        "SITE_NO": readConfig("USER_INFO", "SITE_NO"),
        "COMP_NO": readConfig("USER_INFO", "COMP_NO"),
        "LANGUAGE_TYPE": "1"
    }

    user_url_api = requests.get(url=user_url, params=param_info)

    return user_url_api.status_code

def root_file_list_get(group_no):

    file_list_url = "https://dev-apps.dotincorp.com/drive-app/v1/dtms/groups"

    if group_no == 'ROOT':
        param_info = {
            "PARENT_GROUP_NO": "ROOT",
            "COMP_NO": readConfig("USER_INFO", "COMP_NO"),
            "DRIVER_KIND": "P",
            "USER_NO": readConfig("USER_INFO", "USER_NO")
        }

    else:
        param_info = {
            "PARENT_GROUP_NO": group_no,
            "COMP_NO": readConfig("USER_INFO", "COMP_NO"),
            "DRIVER_KIND": "P",
            "USER_NO": readConfig("USER_INFO", "USER_NO")
        }

    file_open_api = requests.get(url=file_list_url, params=param_info)

    return file_open_api

def root_file_open_get(filekey):

    file_open_url = "https://dev-apps.dotincorp.com/drive-app/v1/dtm/images/{}/device/300/to-dtms".format(filekey)

    file_open_api = requests.get(url=file_open_url)

    return file_open_api.status_code