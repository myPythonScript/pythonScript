import pytest
import sys
from time import sleep
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.page import Page
from pages.startPage import StartPage
from pages.firstPage import FirstPage
from pages.jobPage import JobPage
from pages.videoPage import VideoPage
from pages.myPage import MyPage

sys.path.append(r"C:\自动化测试相关文档\PycharmProjects\toutiao")


@pytest.fixture(scope='session')
def driver():
    caps = {
        # 魅族
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "a89cc63b",
        # 三星
        #     "platformVersion": "7.0",
        #     "deviceName": "a89cc63b",
        "appPackage": "com.ss.android.article.lite",
        "appActivity": ".activity.SplashActivity",
        "automationName": "UiAutomator2",
        "noReset": "True",
        "newCommandTimeout": "150000",
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    print("\n启动APP")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    sleep(6)
    return driver
    # yield driver
    # print("关闭APP")
    # driver.quit()


@pytest.fixture(scope='session')
def job_page(driver):
    return JobPage(driver)


@pytest.fixture(scope='session')
def my_page(driver):
    return MyPage(driver)


@pytest.fixture(scope='session')
def video_page(driver):
    return VideoPage(driver)


@pytest.fixture(scope="session")
def assert_open_box(job_page, my_page, video_page):
    try:
        for i in range(1, 10):
            result = job_page.is_time_to_open()
            if result is True:
                print("已完成")
                job_page.job_itm()
                job_page.open_box()
            else:
                print("未完成")
                # job_page.my_itm()
                # sleep(5)
                # my_page.read_book_func()
                job_page.video_itm()
                sleep(5)
                video_page.play_video()
        # job_page.video_itm()
        # sleep(5)
        # video_page.play_video()
    except Exception as error:
        print(error)