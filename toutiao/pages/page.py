from appium import webdriver
from time import sleep


class Page(object):
    def __init__(self, driver: webdriver.Remote):  # 对driver的注释，不影响代码
        self.driver = driver

    def window_size(self):
        size = self.driver.get_window_size()
        print(size)
        width = size['width']
        height = size["height"]
        return width, height

    # 上滑
    def up_swipe(self):
        width, height = self.window_size()
        print("width:%s, height:%s" % (width, height))
        self.driver.swipe(width / 2, height * 0.9, width / 2, height * 0.1)

    # 下滑
    def down_swipe(self):
        width, height = self.window_size()
        print("width:%s, height:%s" % (width, height))
        self.driver.swipe(width / 2, height * 0.2, width / 2, height * 0.8)

    # 左滑
    def left_swipe(self):
        width, height = self.window_size()
        print("width:%s, height:%s" % (width, height))
        self.driver.swipe(width * 0.9, height / 2, width * 0.2, height / 2)

    # 右滑
    def right_swipe(self):
        width, height = self.window_size()
        print("width:%s, height:%s" % (width, height))
        self.driver.swipe(width * 0.2, height / 2, width * 0.9, height / 2)

    def find_element_by_text(self, text):
        xpath = f'//*[@text="{text}"]'
        return self.driver.find_element('xpath', xpath)

    def find_element_by_widget(self, widget):
        if widget not in ['button', 'text', 'input']:
            raise ValueError("widget只支持button, text, input")
        if widget == 'button':
            class_name = 'android.widget.Button'
        elif widget == 'text':
            class_name = 'android.widget.TextView'
        else:
            class_name = 'android.widget.EditText'
        return self.driver.find_element('class name', class_name)
