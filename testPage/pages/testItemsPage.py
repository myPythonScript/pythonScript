# -*- coding:utf-8 -*-
from selenium import webdriver

class TestItemsPage(object):
    def __init__(self, driver):
        self.driver = driver

    username_ipt_loc = ("id", "accountID")
    passwordID_ipt_loc = ("id", "passwordID")

    def input_username(self, text):
        username_ipt = self.driver.find_element(*self.username_ipt_loc)
        username_ipt.clear()
        username_ipt.send_keys(text)