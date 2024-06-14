from configparser import ConfigParser

def readConfig(section, key):
    config = ConfigParser() #객체 생성
    config.read("/Users/park-yongseong/PycharmProjects/Automation_web/Config/config.ini") #ini 파일 읽어오기
    return config.get(section, key) #section과 key로 value 리턴