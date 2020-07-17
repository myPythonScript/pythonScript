# -*- coding:utf-8 -*-

import pytest
from time import sleep
from pages.testItemsPage import TestItemsPage


def test_items(selenium, data):
    selenium.get("http://115.28.108.130/control.html")
    selenium.maximize_window()
    text = data
    test_items_page = TestItemsPage(selenium)
    test_items_page.input_username(text)
    sleep(3)
