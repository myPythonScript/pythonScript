# -*- coding:utf-8 -*-


class FirstPage(object):
    def __init__(self, driver):
        self.driver = driver

    content_itm_loc = ("id", "com.ss.android.article.lite:id/z2")

    def content_itm(self):
        self.driver.find_elements(*self.content_itm_loc)
