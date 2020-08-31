import pytest
from appium import webdriver
import sys

sys.path.append(r"C:\自动化测试相关文档\PycharmProjects\toutiao")


@pytest.fixture(scope='session')
def driver():
    # 魅族
    caps = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "a89cc63b",
        "appPackage": "com.ss.android.article.lite",
        "appActivity": ".activity.SplashActivity",
        "automationName": "UiAutomator2",
        "noReset": "True",
        "newCommandTimeout": "60000",
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    # 三星
    # caps = {
    #     "platformName": "Android",
    #     "platformVersion": "7.0",
    #     "deviceName": "a89cc63b",
    #     "appPackage": "com.ss.android.article.lite",
    #     "appActivity": ".activity.SplashActivity",
    #     "automationName": "UiAutomator2",
    #     "noReset": "True",
    #     "newCommandTimeout": "60000"
    # }
    print("启动app")
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    driver.implicitly_wait(20)
    print("启动完成")
    yield driver
