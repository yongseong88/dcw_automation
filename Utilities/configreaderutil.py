import json
from configparser import ConfigParser

def readConfig(section, key):
    config = ConfigParser() #객체 생성
    config.read("/Users/park-yongseong/Documents/DCW_Automation/Config/config.ini") #ini 파일 읽어오기
    return config.get(section, key) #section과 key로 value 리턴


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            # print("JSON 데이터:", data)
            return data
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"JSON 디코딩 오류가 발생했습니다: {file_path}")
        return None
