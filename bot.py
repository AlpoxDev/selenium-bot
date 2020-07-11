import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

"""
[By]

ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
"""
class InstaBot:
    def __init__(self):
        self.messages = []
        self.to_directs = []
        self.tags = []

    def init(self):
        self.username = input('아이디를 입력해주세요 : ')
        self.password = input('비밀번호를 입력해주세요 : ')

        # 모바일 에뮬레이터
        mobile_emulation = {
            "deviceMetrics": {"width": 500, "height": 600, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(600, 1000)
        return True

    def menu(self):
        print('1. 태그 좋아요 봇', end='\n')
        print('2. 다이렉트 다중 전송 봇', end='\n')
        menu = input('어떤 역할을 수행하고 싶으신가요? : ')

        if menu == '1':
            print('태그 좋아요 봇 실행중...')
            self.input_directs()
        if menu == '2':
            print('다이렉트 다중 전송 봇 실행중...')
            self.input_directs()

    def login(self):
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")

            username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
            username_input.send_keys(self.username)

            password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
            password_input.send_keys(self.password)

            login_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button')))
            login_button.click()

            later1_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/button')))
            later1_button.click()

            later_button2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
            later_button2.click()

            later_button3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
            later_button3.click()
            return True
        except:
            print('Authorizatoin Failure')
            # self.quit()
            return False


    def input_directs(self):
        # 메시지 입
        message_count = input('메세지 개수를 입력해주세요 : ')
        try:
            message_count = int(message_count)
        except:
            print('메세지 개수 입력이 올바르지 않습니다')
            self.quit()

        for i in range(0, message_count):
            message = input('%s번째 메시지 : '.format(i+1))
            self.messages.append(message)

        # 아이디들 입
        print('\n보낼 사람의 아이디를 다중 입력합니다...')
        print('종료하고자 하면 0을 입력하세요')

        while True:
            to_direct = input('아이디를 입력해주세요 : ')
            if to_direct == '0':
                break

            self.to_directs.append(to_direct)

        print('보낼 메시지 : ', end="")
        print(self.messages)
        print('보낼 사람들 : ', end="")
        print(self.to_directs)

        self.directs()

    def directs(self):
        try:
            self.driver.get('https://www.instagram.com/direct/inbox/')
            time.sleep(2)

        except(Exception):
            logging.warn(Exception)
            print('다이렉트 전송 실패')
            # self.quit()

    def input_tags(self):
        pass

    def quit(self):
        self.driver.quit()


instabot = InstaBot()
isLogined = False

instabot.init()
isLogined = instabot.login()

if isLogined == True:
    instabot.menu()




