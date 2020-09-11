# -*- coding:utf-8 -*-
from pages.page import Page


class StartPage(Page):
    # 跳转启动页
    jump_btn_loc = ("class name", "android.widget.TextView")

    # def jump_btn(self):
    #     clsName = "android.widget.TextView"
    #     jump_itm = Page.find_element_by_widget(clsName)
    #     jump_itm.click()
