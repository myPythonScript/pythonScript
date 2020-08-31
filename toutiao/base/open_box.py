# -*- coding:utf-8 -*-
import pytest
from time import sleep


@pytest.mark.web
def open_box(driver, job_page):
    # 跳转到任务界面
    job_page.job_itm()
    driver.implicitly_wait(30)
    # 宝箱
    job_page.box_itm()
    driver.implicitly_wait(30)
    # 点击看视频
    job_page.box_video()
    sleep(20)
    driver.back()
