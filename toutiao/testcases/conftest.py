# # import pytest
# # from appium import webdriver
# # import sys
# # from time import sleep
# #
# # sys.path.append(r"C:\自动化测试相关文档\PycharmProjects\toutiao")
# #
# #
# # @pytest.fixture(scope='session')
# # def driver():
# #     # 魅族
# #     # caps = {
# #     #     "platformName": "Android",
# #     #     "platformVersion": "9",
# #     #     "deviceName": "a89cc63b",
# #     #     "appPackage": "com.ss.android.article.lite",
# #     #     "appActivity": ".activity.SplashActivity",
# #     #     "automationName": "UiAutomator2",
# #     #     "noReset": "True",
# #     #     "newCommandTimeout": "600"
# #     # }
# #     # 三星
# #     caps = {
# #         "platformName": "Android",
# #         "platformVersion": "7.0",
# #         "deviceName": "a89cc63b",
# #         "appPackage": "com.ss.android.article.lite",
# #         "appActivity": ".activity.SplashActivity",
# #         "automationName": "UiAutomator2",
# #         "noReset": "True",
# #         "newCommandTimeout": "600"
# #     }
# #     print("启动app")
# #     driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
# #     driver.implicitly_wait(20)
# #     print("启动完成")
# #     yield driver
# #
# #
# # # class Actions(object):
# # #     size = driver.get_window_size()
# # #     width = size['width']
# # #     height = size["height"]
# # #
# # #     def up_swipe(self):
# # #         self.driver.swipe(*self.width / 2, *self.height * 0.9, *self.width / 2, *self.height * 0.2)
# #
# # # if __name__ == "__main__":
# # #     caps = {
# # #         "platformName": "Android",
# # #         "platformVersion": "9",
# # #         "deviceName": "a89cc63b",
# # #         "appPackage": "com.ss.android.article.lite",
# # #         "appActivity": ".activity.SplashActivity",
# # #         "automationName": "UIAutomator2",
# # #         "noReset": "True"
# # #     }
# # #     print("启动app")
# # #     driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
# # #     driver.implicitly_wait(20)
# # #     print("启动完成")
# # #     sleep(5)
# # #     job_ele = driver.find_elements("id", "com.ss.android.article.lite:id/ey5")
# # #     print(job_ele)
# # # print(job_ele[3])
# # # driver.keyevent(4)
# # # driver.implicitly_wait(30)
# # # contect_itm = driver.find_elements("id", "com.ss.android.article.lite:id/z2")
# # # for i in contect_itm:
# # #     i.click()
# # #     driver.implicitly_wait(30)
# # #     driver.back()
#
# # from utils.actions import Actions
#
#
# # @pytest.fixture(scope='session')
# # def act():
# #     act = Actions(driver)
# #     return act
#
#
# class Actions(object):
#     def __init__(self, driver):
#         self.driver = driver
#
#     def window_size(self):
#         size = self.driver.get_window_size()
#         width = size['width']
#         height = size["height"]
#         return width, height
#
#     def up_swipe(self):
#         result = self.window_size()
#         print(result)
#         self.driver.swipe(*self.width / 2, *self.height * 0.9, *self.width / 2, *self.height * 0.2)
#
#
# if __name__ == "__main__":
#     act = Actions()
#     act.up_swipe()
