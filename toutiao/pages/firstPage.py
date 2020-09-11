# -*- coding:utf-8 -*-
from pages.page import Page


class FirstPage(Page):
    content_itm_loc = ("id", "com.ss.android.article.lite:id/z2")

    def content_itm(self):
        self.driver.find_elements(*self.content_itm_loc)
        print("跳过启动页界面")
